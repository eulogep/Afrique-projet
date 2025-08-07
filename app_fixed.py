#!/usr/bin/env python3
"""
Version corrigée de l'application Solutions Afrique
"""

from flask import Flask, jsonify, request, send_from_directory, render_template_string
from flask_cors import CORS
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdf#FGSgvasgf$5$WGT'

# Enable CORS for all routes
CORS(app)

# Données d'exemple en mémoire
problems = [
    {
        'id': 1,
        'title': 'Insécurité alimentaire et agriculture peu productive',
        'description': 'Malgré l\'immense potentiel agricole du continent, une part significative de la population souffre de sous-alimentation chronique.',
        'category': 'socio-economic',
        'country': 'République Démocratique du Congo',
        'region': 'Afrique Centrale',
        'severity_level': 5,
        'affected_population': 50000000
    },
    {
        'id': 2,
        'title': 'Manque d\'industrialisation',
        'description': 'L\'économie africaine reste largement dépendante de l\'exportation de matières premières brutes.',
        'category': 'socio-economic',
        'country': 'Nigeria',
        'region': 'Afrique de l\'Ouest',
        'severity_level': 4,
        'affected_population': 30000000
    },
    {
        'id': 3,
        'title': 'Accès limité à l\'eau potable',
        'description': 'L\'accès à l\'eau potable reste un défi majeur pour des millions d\'Africains.',
        'category': 'socio-economic',
        'country': 'Éthiopie',
        'region': 'Afrique de l\'Est',
        'severity_level': 5,
        'affected_population': 40000000
    }
]

projects = [
    {
        'id': 1,
        'title': 'Centres de Formation Agricole',
        'description': 'Créer des centres de formation pour les agriculteurs locaux sur les techniques agricoles modernes.',
        'status': 'proposed',
        'required_budget': 500000,
        'expected_roi': 25,
        'implementation_timeline': '18 mois',
        'target_beneficiaries': 10000,
        'country': 'République Démocratique du Congo'
    },
    {
        'id': 2,
        'title': 'Fermes Aquaponiques Urbaines',
        'description': 'Développer des fermes aquaponiques en milieu urbain pour produire des légumes et du poisson.',
        'status': 'proposed',
        'required_budget': 300000,
        'expected_roi': 30,
        'implementation_timeline': '12 mois',
        'target_beneficiaries': 5000,
        'country': 'Kenya'
    }
]

investments = [
    {
        'id': 1,
        'amount': 100000,
        'currency': 'USD',
        'investment_type': 'grant',
        'status': 'approved',
        'expected_return': 0,
        'project_id': 1
    },
    {
        'id': 2,
        'amount': 250000,
        'currency': 'USD',
        'investment_type': 'loan',
        'status': 'disbursed',
        'expected_return': 5,
        'project_id': 2
    }
]

# Route pour servir les fichiers statiques
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('src/static', filename)

# Route pour servir les fichiers CSS et JS directement
@app.route('/<path:filename>')
def serve_static(filename):
    if filename.endswith('.css') or filename.endswith('.js'):
        return send_from_directory('src/static', filename)
    return "File not found", 404

# Route principale
@app.route('/')
def index():
    try:
        with open('src/static/index.html', 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "index.html not found", 404

@app.route('/api/health', methods=['GET'])
def health_check():
    """Point de contrôle de santé de l'API"""
    return {'status': 'healthy', 'message': 'Africa Solutions Platform API is running'}

@app.route('/api/problems', methods=['GET'])
def get_problems():
    """Récupérer tous les problèmes"""
    return jsonify(problems)

@app.route('/api/problems', methods=['POST'])
def create_problem():
    """Créer un nouveau problème"""
    data = request.get_json()
    
    if not data or not data.get('title'):
        return jsonify({'error': 'Title is required'}), 400
    
    new_problem = {
        'id': len(problems) + 1,
        'title': data['title'],
        'description': data.get('description', ''),
        'category': data.get('category', 'socio-economic'),
        'country': data.get('country', ''),
        'region': data.get('region', ''),
        'severity_level': data.get('severity_level', 1),
        'affected_population': data.get('affected_population', 0)
    }
    
    problems.append(new_problem)
    return jsonify(new_problem), 201

@app.route('/api/projects', methods=['GET'])
def get_projects():
    """Récupérer tous les projets"""
    return jsonify(projects)

@app.route('/api/projects', methods=['POST'])
def create_project():
    """Créer un nouveau projet"""
    data = request.get_json()
    
    if not data or not data.get('title'):
        return jsonify({'error': 'Title is required'}), 400
    
    new_project = {
        'id': len(projects) + 1,
        'title': data['title'],
        'description': data.get('description', ''),
        'status': data.get('status', 'proposed'),
        'required_budget': data.get('required_budget', 0),
        'expected_roi': data.get('expected_roi', 0),
        'implementation_timeline': data.get('implementation_timeline', ''),
        'target_beneficiaries': data.get('target_beneficiaries', 0),
        'country': data.get('country', '')
    }
    
    projects.append(new_project)
    return jsonify(new_project), 201

@app.route('/api/investments', methods=['GET'])
def get_investments():
    """Récupérer tous les investissements"""
    return jsonify(investments)

@app.route('/api/investments', methods=['POST'])
def create_investment():
    """Créer un nouvel investissement"""
    data = request.get_json()
    
    if not data or not data.get('amount'):
        return jsonify({'error': 'Amount is required'}), 400
    
    new_investment = {
        'id': len(investments) + 1,
        'amount': data['amount'],
        'currency': data.get('currency', 'USD'),
        'investment_type': data.get('investment_type', 'grant'),
        'status': data.get('status', 'pending'),
        'expected_return': data.get('expected_return', 0),
        'project_id': data.get('project_id', 1)
    }
    
    investments.append(new_investment)
    return jsonify(new_investment), 201

if __name__ == '__main__':
    print("🚀 Démarrage de la plateforme Solutions Afrique (Version Corrigée)...")
    print("📱 Accédez à http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=True) 