#!/usr/bin/env python3
"""
Script simple pour initialiser la base de données
"""

import os
import sys

# Ajouter le répertoire courant au path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from main import app, db

def init_database():
    """Initialiser la base de données"""
    print("🌍 Initialisation de la base de données Solutions Afrique...")
    
    # Créer le dossier database s'il n'existe pas
    if not os.path.exists('database'):
        os.makedirs('database')
        print("📁 Dossier database créé")
    
    with app.app_context():
        try:
            db.create_all()
            print("✅ Base de données initialisée avec succès!")
            print("📊 Tables créées:")
            print("   - users")
            print("   - problems") 
            print("   - projects")
            print("   - investments")
        except Exception as e:
            print(f"❌ Erreur lors de l'initialisation: {e}")

if __name__ == '__main__':
    init_database() 