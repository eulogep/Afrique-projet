from flask import Blueprint, request, jsonify
from src.models.user import db
from src.models.project import Project
from src.models.problem import Problem

projects_bp = Blueprint('projects', __name__)

@projects_bp.route('/projects', methods=['GET'])
def get_projects():
    """Récupérer tous les projets avec filtres optionnels"""
    try:
        # Paramètres de filtrage
        status = request.args.get('status')
        country = request.args.get('country')
        region = request.args.get('region')
        min_budget = request.args.get('min_budget', type=float)
        max_budget = request.args.get('max_budget', type=float)
        problem_id = request.args.get('problem_id', type=int)
        
        # Construction de la requête
        query = Project.query
        
        if status:
            query = query.filter(Project.status == status)
        if country:
            query = query.filter(Project.country == country)
        if region:
            query = query.filter(Project.region == region)
        if min_budget:
            query = query.filter(Project.required_budget >= min_budget)
        if max_budget:
            query = query.filter(Project.required_budget <= max_budget)
        if problem_id:
            query = query.filter(Project.problem_id == problem_id)
        
        projects = query.all()
        return jsonify([project.to_dict() for project in projects])
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@projects_bp.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    """Récupérer un projet spécifique"""
    try:
        project = Project.query.get_or_404(project_id)
        project_data = project.to_dict()
        
        # Ajouter les informations du problème associé
        if project.problem_id:
            problem = Problem.query.get(project.problem_id)
            if problem:
                project_data['related_problem'] = problem.to_dict()
        
        return jsonify(project_data)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@projects_bp.route('/projects', methods=['POST'])
def create_project():
    """Créer un nouveau projet"""
    try:
        data = request.get_json()
        
        if not data or not data.get('title') or not data.get('description'):
            return jsonify({'error': 'Title and description are required'}), 400
        
        project = Project(
            title=data['title'],
            description=data['description'],
            economic_model=data.get('economic_model'),
            profitability_analysis=data.get('profitability_analysis'),
            required_budget=data.get('required_budget'),
            expected_roi=data.get('expected_roi'),
            implementation_timeline=data.get('implementation_timeline'),
            target_beneficiaries=data.get('target_beneficiaries'),
            status=data.get('status', 'proposed'),
            country=data.get('country'),
            region=data.get('region'),
            created_by=data.get('created_by'),
            problem_id=data.get('problem_id')
        )
        
        db.session.add(project)
        db.session.commit()
        
        return jsonify(project.to_dict()), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@projects_bp.route('/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    """Mettre à jour un projet"""
    try:
        project = Project.query.get_or_404(project_id)
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Mise à jour des champs
        updatable_fields = [
            'title', 'description', 'economic_model', 'profitability_analysis',
            'required_budget', 'expected_roi', 'implementation_timeline',
            'target_beneficiaries', 'status', 'country', 'region', 'problem_id'
        ]
        
        for field in updatable_fields:
            if field in data:
                setattr(project, field, data[field])
        
        db.session.commit()
        return jsonify(project.to_dict())
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@projects_bp.route('/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    """Supprimer un projet"""
    try:
        project = Project.query.get_or_404(project_id)
        db.session.delete(project)
        db.session.commit()
        
        return jsonify({'message': 'Project deleted successfully'})
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@projects_bp.route('/projects/status-options', methods=['GET'])
def get_status_options():
    """Récupérer les options de statut disponibles"""
    statuses = ['proposed', 'funded', 'in_progress', 'completed', 'cancelled']
    return jsonify(statuses)

@projects_bp.route('/projects/stats', methods=['GET'])
def get_projects_stats():
    """Récupérer les statistiques des projets"""
    try:
        total_projects = Project.query.count()
        by_status = db.session.query(Project.status, db.func.count(Project.id)).group_by(Project.status).all()
        by_country = db.session.query(Project.country, db.func.count(Project.id)).group_by(Project.country).all()
        
        # Calcul du budget total requis
        total_budget_result = db.session.query(db.func.sum(Project.required_budget)).scalar()
        total_budget = total_budget_result if total_budget_result else 0
        
        stats = {
            'total_projects': total_projects,
            'by_status': dict(by_status),
            'by_country': dict(by_country),
            'total_required_budget': total_budget
        }
        
        return jsonify(stats)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@projects_bp.route('/projects/matching/<int:problem_id>', methods=['GET'])
def get_matching_projects(problem_id):
    """Récupérer les projets qui correspondent à un problème spécifique"""
    try:
        problem = Problem.query.get_or_404(problem_id)
        
        # Recherche des projets liés directement
        direct_projects = Project.query.filter_by(problem_id=problem_id).all()
        
        # Recherche des projets dans la même région/pays
        related_projects = Project.query.filter(
            Project.problem_id != problem_id,
            Project.country == problem.country
        ).limit(5).all()
        
        result = {
            'problem': problem.to_dict(),
            'direct_projects': [p.to_dict() for p in direct_projects],
            'related_projects': [p.to_dict() for p in related_projects]
        }
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

