from flask import Blueprint, request, jsonify
from src.models.user import db
from src.models.problem import Problem

problems_bp = Blueprint('problems', __name__)

@problems_bp.route('/problems', methods=['GET'])
def get_problems():
    """Récupérer tous les problèmes avec filtres optionnels"""
    try:
        # Paramètres de filtrage
        category = request.args.get('category')
        country = request.args.get('country')
        region = request.args.get('region')
        severity_min = request.args.get('severity_min', type=int)
        
        # Construction de la requête
        query = Problem.query
        
        if category:
            query = query.filter(Problem.category == category)
        if country:
            query = query.filter(Problem.country == country)
        if region:
            query = query.filter(Problem.region == region)
        if severity_min:
            query = query.filter(Problem.severity_level >= severity_min)
        
        problems = query.all()
        return jsonify([problem.to_dict() for problem in problems])
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@problems_bp.route('/problems/<int:problem_id>', methods=['GET'])
def get_problem(problem_id):
    """Récupérer un problème spécifique"""
    try:
        problem = Problem.query.get_or_404(problem_id)
        return jsonify(problem.to_dict())
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@problems_bp.route('/problems', methods=['POST'])
def create_problem():
    """Créer un nouveau problème"""
    try:
        data = request.get_json()
        
        if not data or not data.get('title') or not data.get('description'):
            return jsonify({'error': 'Title and description are required'}), 400
        
        problem = Problem(
            title=data['title'],
            description=data['description'],
            category=data.get('category', 'socio-economic'),
            subcategory=data.get('subcategory'),
            country=data.get('country'),
            region=data.get('region'),
            severity_level=data.get('severity_level', 1),
            affected_population=data.get('affected_population'),
            created_by=data.get('created_by')
        )
        
        db.session.add(problem)
        db.session.commit()
        
        return jsonify(problem.to_dict()), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@problems_bp.route('/problems/<int:problem_id>', methods=['PUT'])
def update_problem(problem_id):
    """Mettre à jour un problème"""
    try:
        problem = Problem.query.get_or_404(problem_id)
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Mise à jour des champs
        for field in ['title', 'description', 'category', 'subcategory', 'country', 'region', 'severity_level', 'affected_population']:
            if field in data:
                setattr(problem, field, data[field])
        
        db.session.commit()
        return jsonify(problem.to_dict())
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@problems_bp.route('/problems/<int:problem_id>', methods=['DELETE'])
def delete_problem(problem_id):
    """Supprimer un problème"""
    try:
        problem = Problem.query.get_or_404(problem_id)
        db.session.delete(problem)
        db.session.commit()
        
        return jsonify({'message': 'Problem deleted successfully'})
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@problems_bp.route('/problems/categories', methods=['GET'])
def get_categories():
    """Récupérer les catégories de problèmes disponibles"""
    categories = {
        'socio-economic': [
            'agriculture',
            'industrialization',
            'water-access',
            'energy-access',
            'unemployment',
            'poverty',
            'structural-issues'
        ],
        'security-stability': [
            'conflicts',
            'insecurity',
            'mineral-predation'
        ]
    }
    return jsonify(categories)

@problems_bp.route('/problems/stats', methods=['GET'])
def get_problems_stats():
    """Récupérer les statistiques des problèmes"""
    try:
        total_problems = Problem.query.count()
        by_category = db.session.query(Problem.category, db.func.count(Problem.id)).group_by(Problem.category).all()
        by_country = db.session.query(Problem.country, db.func.count(Problem.id)).group_by(Problem.country).all()
        
        stats = {
            'total_problems': total_problems,
            'by_category': dict(by_category),
            'by_country': dict(by_country)
        }
        
        return jsonify(stats)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

