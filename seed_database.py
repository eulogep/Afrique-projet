#!/usr/bin/env python3
"""
Script pour peupler la base de données avec des données d'exemple
basées sur le contenu analysé des problèmes africains et des projets solutions.
"""

import sys
import os
from datetime import datetime

# Ajouter le répertoire courant au path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from main import app
from src.models.user import db, User
from src.models.problem import Problem
from src.models.project import Project
from src.models.investment import Investment

def seed_users():
    """Créer des utilisateurs d'exemple"""
    users = [
        {
            'username': 'entrepreneur_congo',
            'email': 'entrepreneur@congo.cd',
            'first_name': 'Jean',
            'last_name': 'Mukendi',
            'user_type': 'entrepreneur',
            'country': 'République Démocratique du Congo',
            'bio': 'Entrepreneur passionné par le développement agricole en RDC',
            'verified': True
        },
        {
            'username': 'investor_europe',
            'email': 'investor@europe.eu',
            'first_name': 'Marie',
            'last_name': 'Dubois',
            'user_type': 'investor',
            'country': 'France',
            'bio': 'Investisseur impact spécialisé dans les projets africains',
            'verified': True
        },
        {
            'username': 'expert_agriculture',
            'email': 'expert@agri.org',
            'first_name': 'Dr. Amadou',
            'last_name': 'Diallo',
            'user_type': 'expert',
            'country': 'Sénégal',
            'bio': 'Expert en agriculture durable et sécurité alimentaire',
            'verified': True
        }
    ]
    
    for user_data in users:
        user = User(**user_data)
        db.session.add(user)
    
    db.session.commit()
    print(f"✅ {len(users)} utilisateurs créés")

def seed_problems():
    """Créer des problèmes d'exemple"""
    problems = [
        {
            'title': 'Insécurité alimentaire et agriculture peu productive',
            'description': 'Malgré l\'immense potentiel agricole du continent, une part significative de la population souffre de sous-alimentation chronique. Les pratiques agricoles traditionnelles et le manque d\'accès aux technologies limitent les rendements.',
            'category': 'socio-economic',
            'subcategory': 'agriculture',
            'country': 'République Démocratique du Congo',
            'region': 'Afrique Centrale',
            'severity_level': 5,
            'affected_population': 50000000,
            'created_by': 1
        },
        {
            'title': 'Manque d\'industrialisation',
            'description': 'L\'économie africaine reste largement dépendante de l\'exportation de matières premières brutes. Le manque d\'industrialisation limite la création d\'emplois qualifiés.',
            'category': 'socio-economic',
            'subcategory': 'industrie',
            'country': 'Nigeria',
            'region': 'Afrique de l\'Ouest',
            'severity_level': 4,
            'affected_population': 30000000,
            'created_by': 1
        },
        {
            'title': 'Accès limité à l\'eau potable',
            'description': 'L\'accès à l\'eau potable reste un défi majeur pour des millions d\'Africains, en particulier dans les zones rurales.',
            'category': 'socio-economic',
            'subcategory': 'eau',
            'country': 'Éthiopie',
            'region': 'Afrique de l\'Est',
            'severity_level': 5,
            'affected_population': 40000000,
            'created_by': 1
        },
        {
            'title': 'Chômage endémique des jeunes',
            'description': 'Le manque d\'opportunités d\'emploi, combiné à un système éducatif qui ne prépare pas adéquatement aux besoins du marché du travail.',
            'category': 'socio-economic',
            'subcategory': 'emploi',
            'country': 'République Démocratique du Congo',
            'region': 'Afrique Centrale',
            'severity_level': 5,
            'affected_population': 20000000,
            'created_by': 1
        },
        {
            'title': 'Conflits armés et insécurité',
            'description': 'L\'Est de la RDC est le théâtre de conflits armés persistants impliquant de nombreux groupes armés locaux et étrangers.',
            'category': 'security-stability',
            'subcategory': 'conflits',
            'country': 'République Démocratique du Congo',
            'region': 'Afrique Centrale',
            'severity_level': 5,
            'affected_population': 15000000,
            'created_by': 1
        },
        {
            'title': 'Prédation minière militarisée',
            'description': 'Des groupes armés financent leurs activités par l\'exploitation illégale et le trafic de minerais.',
            'category': 'security-stability',
            'subcategory': 'exploitation',
            'country': 'République Démocratique du Congo',
            'region': 'Afrique Centrale',
            'severity_level': 4,
            'affected_population': 5000000,
            'created_by': 1
        }
    ]
    
    for problem_data in problems:
        problem = Problem(**problem_data)
        db.session.add(problem)
    
    db.session.commit()
    print(f"✅ {len(problems)} problèmes créés")

def seed_projects():
    """Créer des projets d'exemple"""
    projects = [
        {
            'title': 'Centres de Formation Agricole et Distribution de Technologies',
            'description': 'Créer des centres de formation pour les agriculteurs locaux sur les techniques agricoles modernes. Mise en place d\'un système de distribution de semences améliorées et d\'équipements agricoles.',
            'economic_model': 'Vente de formations, semences et équipements. Partenariats avec ONG et programmes gouvernementaux.',
            'profitability_analysis': 'Forte demande pour l\'amélioration de la productivité agricole. Marché en croissance.',
            'required_budget': 500000,
            'expected_roi': 25,
            'implementation_timeline': '18 mois',
            'target_beneficiaries': 10000,
            'status': 'proposed',
            'country': 'République Démocratique du Congo',
            'region': 'Afrique Centrale',
            'created_by': 1,
            'problem_id': 1
        },
        {
            'title': 'Fermes Aquaponiques/Hydroponiques Urbaines',
            'description': 'Développer des fermes aquaponiques en milieu urbain pour produire des légumes et du poisson avec une consommation d\'eau minimale.',
            'economic_model': 'Vente directe aux consommateurs, abonnements pour des paniers de légumes frais.',
            'profitability_analysis': 'Production rapide et de haute qualité, faible empreinte écologique.',
            'required_budget': 300000,
            'expected_roi': 30,
            'implementation_timeline': '12 mois',
            'target_beneficiaries': 5000,
            'status': 'proposed',
            'country': 'Kenya',
            'region': 'Afrique de l\'Est',
            'created_by': 1,
            'problem_id': 1
        },
        {
            'title': 'Unités de Transformation de Matières Premières Locales',
            'description': 'Mettre en place de petites et moyennes unités de transformation pour des matières premières locales (fruits, légumes, manioc, cacao).',
            'economic_model': 'Vente de produits finis sur les marchés locaux et nationaux. Création de marques locales.',
            'profitability_analysis': 'Ajout de valeur significative aux produits bruts, réduction de la dépendance aux importations.',
            'required_budget': 750000,
            'expected_roi': 35,
            'implementation_timeline': '24 mois',
            'target_beneficiaries': 15000,
            'status': 'proposed',
            'country': 'Nigeria',
            'region': 'Afrique de l\'Ouest',
            'created_by': 1,
            'problem_id': 2
        },
        {
            'title': 'Solutions d\'Accès à l\'Eau Potable Décentralisées',
            'description': 'Déployer des systèmes de purification d\'eau à petite échelle dans les communautés rurales et périurbaines.',
            'economic_model': 'Vente d\'eau purifiée à un prix abordable, vente et maintenance des équipements.',
            'profitability_analysis': 'La demande en eau potable est universelle et constante.',
            'required_budget': 400000,
            'expected_roi': 20,
            'implementation_timeline': '15 mois',
            'target_beneficiaries': 25000,
            'status': 'proposed',
            'country': 'Éthiopie',
            'region': 'Afrique de l\'Est',
            'created_by': 1,
            'problem_id': 3
        },
        {
            'title': 'Plateformes de Mise en Relation Compétences-Emplois',
            'description': 'Créer une plateforme numérique qui met en relation les demandeurs d\'emploi avec les entreprises locales.',
            'economic_model': 'Frais d\'inscription pour les entreprises, commissions sur les placements réussis.',
            'profitability_analysis': 'Répond à un besoin criant de main-d\'œuvre qualifiée et de réduction du chômage.',
            'required_budget': 200000,
            'expected_roi': 40,
            'implementation_timeline': '9 mois',
            'target_beneficiaries': 8000,
            'status': 'proposed',
            'country': 'République Démocratique du Congo',
            'region': 'Afrique Centrale',
            'created_by': 1,
            'problem_id': 4
        },
        {
            'title': 'Plateformes de Médiation et de Résolution de Conflits',
            'description': 'Créer des centres communautaires équipés pour la médiation et la résolution pacifique des conflits locaux.',
            'economic_model': 'Financement par des organisations internationales, services de médiation payants.',
            'profitability_analysis': 'La stabilité et la paix sont des prérequis essentiels au développement économique.',
            'required_budget': 600000,
            'expected_roi': 15,
            'implementation_timeline': '30 mois',
            'target_beneficiaries': 12000,
            'status': 'proposed',
            'country': 'République Démocratique du Congo',
            'region': 'Afrique Centrale',
            'created_by': 1,
            'problem_id': 5
        }
    ]
    
    for project_data in projects:
        project = Project(**project_data)
        db.session.add(project)
    
    db.session.commit()
    print(f"✅ {len(projects)} projets créés")

def seed_investments():
    """Créer des investissements d'exemple"""
    investments = [
        {
            'amount': 100000,
            'currency': 'USD',
            'investment_type': 'grant',
            'status': 'approved',
            'terms': 'Subvention pour le développement de centres de formation agricole',
            'expected_return': 0,
            'maturity_date': '2025-12-31',
            'investor_id': 2,
            'project_id': 1
        },
        {
            'amount': 250000,
            'currency': 'USD',
            'investment_type': 'loan',
            'status': 'disbursed',
            'terms': 'Prêt à 5% d\'intérêt annuel pour les fermes aquaponiques',
            'expected_return': 5,
            'maturity_date': '2026-06-30',
            'investor_id': 2,
            'project_id': 2
        },
        {
            'amount': 150000,
            'currency': 'USD',
            'investment_type': 'equity',
            'status': 'pending',
            'terms': 'Participation de 20% dans les unités de transformation',
            'expected_return': 25,
            'maturity_date': '2027-03-31',
            'investor_id': 2,
            'project_id': 3
        }
    ]
    
    for investment_data in investments:
        investment = Investment(**investment_data)
        db.session.add(investment)
    
    db.session.commit()
    print(f"✅ {len(investments)} investissements créés")

def main():
    """Fonction principale pour peupler la base de données"""
    print("🌍 Peuplement de la base de données Solutions Afrique...")
    
    with app.app_context():
        # Vider la base de données existante
        db.drop_all()
        db.create_all()
        print("🗑️ Base de données vidée et recréée")
        
        # Peupler avec les données d'exemple
        seed_users()
        seed_problems()
        seed_projects()
        seed_investments()
        
        print("\n🎉 Base de données peuplée avec succès!")
        print("📊 Statistiques:")
        print(f"   - {User.query.count()} utilisateurs")
        print(f"   - {Problem.query.count()} problèmes")
        print(f"   - {Project.query.count()} projets")
        print(f"   - {Investment.query.count()} investissements")

if __name__ == '__main__':
    main() 