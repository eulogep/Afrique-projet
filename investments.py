from flask import Blueprint, request, jsonify
from src.models.user import db, User
from src.models.investment import Investment
from src.models.project import Project

investments_bp = Blueprint('investments', __name__)

@investments_bp.route('/investments', methods=['GET'])
def get_investments():
    """Récupérer tous les investissements avec filtres optionnels"""
    try:
        # Paramètres de filtrage
        investor_id = request.args.get('investor_id', type=int)
        project_id = request.args.get('project_id', type=int)
        status = request.args.get('status')
        investment_type = request.args.get('investment_type')
        
        # Construction de la requête
        query = Investment.query
        
        if investor_id:
            query = query.filter(Investment.investor_id == investor_id)
        if project_id:
            query = query.filter(Investment.project_id == project_id)
        if status:
            query = query.filter(Investment.status == status)
        if investment_type:
            query = query.filter(Investment.investment_type == investment_type)
        
        investments = query.all()
        return jsonify([investment.to_dict() for investment in investments])
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@investments_bp.route('/investments/<int:investment_id>', methods=['GET'])
def get_investment(investment_id):
    """Récupérer un investissement spécifique"""
    try:
        investment = Investment.query.get_or_404(investment_id)
        investment_data = investment.to_dict()
        
        # Ajouter les informations du projet et de l'investisseur
        project = Project.query.get(investment.project_id)
        investor = User.query.get(investment.investor_id)
        
        if project:
            investment_data['project'] = project.to_dict()
        if investor:
            investment_data['investor'] = {
                'id': investor.id,
                'username': investor.username,
                'first_name': investor.first_name,
                'last_name': investor.last_name,
                'user_type': investor.user_type
            }
        
        return jsonify(investment_data)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@investments_bp.route('/investments', methods=['POST'])
def create_investment():
    """Créer un nouvel investissement"""
    try:
        data = request.get_json()
        
        required_fields = ['amount', 'investment_type', 'investor_id', 'project_id']
        if not data or not all(field in data for field in required_fields):
            return jsonify({'error': 'Amount, investment_type, investor_id, and project_id are required'}), 400
        
        # Vérifier que l'investisseur et le projet existent
        investor = User.query.get(data['investor_id'])
        project = Project.query.get(data['project_id'])
        
        if not investor:
            return jsonify({'error': 'Investor not found'}), 404
        if not project:
            return jsonify({'error': 'Project not found'}), 404
        
        investment = Investment(
            amount=data['amount'],
            currency=data.get('currency', 'USD'),
            investment_type=data['investment_type'],
            status=data.get('status', 'pending'),
            terms=data.get('terms'),
            expected_return=data.get('expected_return'),
            maturity_date=data.get('maturity_date'),
            investor_id=data['investor_id'],
            project_id=data['project_id']
        )
        
        db.session.add(investment)
        db.session.commit()
        
        return jsonify(investment.to_dict()), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@investments_bp.route('/investments/<int:investment_id>', methods=['PUT'])
def update_investment(investment_id):
    """Mettre à jour un investissement"""
    try:
        investment = Investment.query.get_or_404(investment_id)
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Mise à jour des champs
        updatable_fields = [
            'amount', 'currency', 'investment_type', 'status', 'terms',
            'expected_return', 'maturity_date'
        ]
        
        for field in updatable_fields:
            if field in data:
                setattr(investment, field, data[field])
        
        db.session.commit()
        return jsonify(investment.to_dict())
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@investments_bp.route('/investments/<int:investment_id>', methods=['DELETE'])
def delete_investment(investment_id):
    """Supprimer un investissement"""
    try:
        investment = Investment.query.get_or_404(investment_id)
        db.session.delete(investment)
        db.session.commit()
        
        return jsonify({'message': 'Investment deleted successfully'})
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@investments_bp.route('/investments/types', methods=['GET'])
def get_investment_types():
    """Récupérer les types d'investissement disponibles"""
    types = ['loan', 'grant', 'equity', 'donation']
    return jsonify(types)

@investments_bp.route('/investments/stats', methods=['GET'])
def get_investments_stats():
    """Récupérer les statistiques des investissements"""
    try:
        total_investments = Investment.query.count()
        
        # Total des montants par statut
        by_status = db.session.query(
            Investment.status, 
            db.func.count(Investment.id),
            db.func.sum(Investment.amount)
        ).group_by(Investment.status).all()
        
        # Total des montants par type
        by_type = db.session.query(
            Investment.investment_type,
            db.func.count(Investment.id),
            db.func.sum(Investment.amount)
        ).group_by(Investment.investment_type).all()
        
        # Montant total investi
        total_amount_result = db.session.query(db.func.sum(Investment.amount)).scalar()
        total_amount = total_amount_result if total_amount_result else 0
        
        stats = {
            'total_investments': total_investments,
            'total_amount': total_amount,
            'by_status': [{'status': s[0], 'count': s[1], 'amount': s[2] or 0} for s in by_status],
            'by_type': [{'type': t[0], 'count': t[1], 'amount': t[2] or 0} for t in by_type]
        }
        
        return jsonify(stats)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@investments_bp.route('/investments/project/<int:project_id>/summary', methods=['GET'])
def get_project_investment_summary(project_id):
    """Récupérer le résumé des investissements pour un projet"""
    try:
        project = Project.query.get_or_404(project_id)
        investments = Investment.query.filter_by(project_id=project_id).all()
        
        total_invested = sum([inv.amount for inv in investments])
        funding_gap = (project.required_budget or 0) - total_invested
        funding_percentage = (total_invested / project.required_budget * 100) if project.required_budget else 0
        
        summary = {
            'project_id': project_id,
            'project_title': project.title,
            'required_budget': project.required_budget,
            'total_invested': total_invested,
            'funding_gap': max(0, funding_gap),
            'funding_percentage': min(100, funding_percentage),
            'investments_count': len(investments),
            'investments': [inv.to_dict() for inv in investments]
        }
        
        return jsonify(summary)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

