#!/usr/bin/env python3
"""
Script de test pour vérifier les fonctionnalités de l'API
"""

import requests
import json

BASE_URL = "http://localhost:5000"

def test_health_check():
    """Test du point de contrôle de santé"""
    print("🔍 Test du point de contrôle de santé...")
    try:
        response = requests.get(f"{BASE_URL}/api/health")
        if response.status_code == 200:
            print("✅ API en ligne")
            print(f"   Réponse: {response.json()}")
            return True
        else:
            print(f"❌ Erreur: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Erreur de connexion: {e}")
        return False

def test_get_problems():
    """Test de récupération des problèmes"""
    print("\n🔍 Test de récupération des problèmes...")
    try:
        response = requests.get(f"{BASE_URL}/api/problems")
        if response.status_code == 200:
            problems = response.json()
            print(f"✅ {len(problems)} problèmes récupérés")
            for problem in problems:
                print(f"   - {problem['title']} ({problem['country']})")
            return True
        else:
            print(f"❌ Erreur: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Erreur: {e}")
        return False

def test_get_projects():
    """Test de récupération des projets"""
    print("\n🔍 Test de récupération des projets...")
    try:
        response = requests.get(f"{BASE_URL}/api/projects")
        if response.status_code == 200:
            projects = response.json()
            print(f"✅ {len(projects)} projets récupérés")
            for project in projects:
                print(f"   - {project['title']} (Budget: ${project['required_budget']:,})")
            return True
        else:
            print(f"❌ Erreur: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Erreur: {e}")
        return False

def test_get_investments():
    """Test de récupération des investissements"""
    print("\n🔍 Test de récupération des investissements...")
    try:
        response = requests.get(f"{BASE_URL}/api/investments")
        if response.status_code == 200:
            investments = response.json()
            print(f"✅ {len(investments)} investissements récupérés")
            for investment in investments:
                print(f"   - ${investment['amount']:,} ({investment['investment_type']})")
            return True
        else:
            print(f"❌ Erreur: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Erreur: {e}")
        return False

def test_add_problem():
    """Test d'ajout d'un problème"""
    print("\n🔍 Test d'ajout d'un problème...")
    new_problem = {
        "title": "Test Problème API",
        "description": "Problème de test créé via API",
        "category": "socio-economic",
        "country": "Pays de Test",
        "region": "Région de Test",
        "severity_level": 3,
        "affected_population": 5000
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/api/problems",
            headers={"Content-Type": "application/json"},
            data=json.dumps(new_problem)
        )
        
        if response.status_code == 201:
            created_problem = response.json()
            print(f"✅ Problème créé avec succès (ID: {created_problem['id']})")
            print(f"   Titre: {created_problem['title']}")
            return True
        else:
            print(f"❌ Erreur: {response.status_code}")
            print(f"   Réponse: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Erreur: {e}")
        return False

def test_add_project():
    """Test d'ajout d'un projet"""
    print("\n🔍 Test d'ajout d'un projet...")
    new_project = {
        "title": "Test Projet API",
        "description": "Projet de test créé via API",
        "status": "proposed",
        "required_budget": 75000,
        "expected_roi": 15,
        "implementation_timeline": "6 mois",
        "target_beneficiaries": 2000,
        "country": "Pays de Test"
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/api/projects",
            headers={"Content-Type": "application/json"},
            data=json.dumps(new_project)
        )
        
        if response.status_code == 201:
            created_project = response.json()
            print(f"✅ Projet créé avec succès (ID: {created_project['id']})")
            print(f"   Titre: {created_project['title']}")
            print(f"   Budget: ${created_project['required_budget']:,}")
            return True
        else:
            print(f"❌ Erreur: {response.status_code}")
            print(f"   Réponse: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Erreur: {e}")
        return False

def test_add_investment():
    """Test d'ajout d'un investissement"""
    print("\n🔍 Test d'ajout d'un investissement...")
    new_investment = {
        "amount": 25000,
        "currency": "USD",
        "investment_type": "grant",
        "status": "pending",
        "expected_return": 0,
        "project_id": 1
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/api/investments",
            headers={"Content-Type": "application/json"},
            data=json.dumps(new_investment)
        )
        
        if response.status_code == 201:
            created_investment = response.json()
            print(f"✅ Investissement créé avec succès (ID: {created_investment['id']})")
            print(f"   Montant: ${created_investment['amount']:,}")
            print(f"   Type: {created_investment['investment_type']}")
            return True
        else:
            print(f"❌ Erreur: {response.status_code}")
            print(f"   Réponse: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Erreur: {e}")
        return False

def main():
    """Fonction principale de test"""
    print("🚀 Démarrage des tests de l'API Solutions Afrique")
    print("=" * 50)
    
    tests = [
        test_health_check,
        test_get_problems,
        test_get_projects,
        test_get_investments,
        test_add_problem,
        test_add_project,
        test_add_investment
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print("\n" + "=" * 50)
    print(f"📊 Résultats des tests: {passed}/{total} réussis")
    
    if passed == total:
        print("🎉 Tous les tests sont passés avec succès!")
    else:
        print("⚠️  Certains tests ont échoué")
    
    print("\n✅ L'API est fonctionnelle et prête à être utilisée!")

if __name__ == "__main__":
    main() 