Script pour peupler la base de données avec des données d'exemple
basées sur le contenu analysé des problèmes africains et des projets solutions.
"""

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
            'investment_capacity': 500000.0,
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
            'expertise_areas': '["agriculture", "irrigation", "formation"]',
            'verified': True
        },
        {
            'username': 'ngo_development',
            'email': 'contact@ngo-dev.org',
            'first_name': 'Organisation',
            'last_name': 'Développement',