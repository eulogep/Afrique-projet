#!/usr/bin/env python3
"""
🌍 Solutions Afrique - Version Complète UIVERSE.IO
Application moderne avec toutes les fonctionnalités intégrées
"""

from flask import Flask, jsonify, request, render_template_string
from flask_cors import CORS
import os
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'solutions-afrique-complete-2025'

# Enable CORS
CORS(app)

# Données enrichies avec plus de contenu
problems = [
    {
        'id': 1,
        'title': 'Insécurité alimentaire et agriculture peu productive',
        'description': 'Malgré l\'immense potentiel agricole du continent, une part significative de la population souffre de sous-alimentation chronique.',
        'category': 'socio-economic',
        'country': 'République Démocratique du Congo',
        'region': 'Afrique Centrale',
        'severity_level': 5,
        'affected_population': 50000000,
        'icon': '🌾',
        'color': '#FF6B6B',
        'solutions': ['Formation agricole', 'Irrigation moderne', 'Semences améliorées'],
        'created_date': '2025-01-15'
    },
    {
        'id': 2,
        'title': 'Manque d\'industrialisation',
        'description': 'L\'économie africaine reste largement dépendante de l\'exportation de matières premières brutes.',
        'category': 'socio-economic',
        'country': 'Nigeria',
        'region': 'Afrique de l\'Ouest',
        'severity_level': 4,
        'affected_population': 30000000,
        'icon': '🏭',
        'color': '#4ECDC4',
        'solutions': ['Zones économiques spéciales', 'Formation technique', 'Investissement étranger'],
        'created_date': '2025-01-10'
    },
    {
        'id': 3,
        'title': 'Accès limité à l\'eau potable',
        'description': 'L\'accès à l\'eau potable reste un défi majeur pour des millions d\'Africains.',
        'category': 'socio-economic',
        'country': 'Éthiopie',
        'region': 'Afrique de l\'Est',
        'severity_level': 5,
        'affected_population': 40000000,
        'icon': '💧',
        'color': '#45B7D1',
        'solutions': ['Forages d\'eau', 'Systèmes de purification', 'Infrastructure hydraulique'],
        'created_date': '2025-01-12'
    },
    {
        'id': 4,
        'title': 'Accès limité à l\'éducation',
        'description': 'De nombreux enfants n\'ont pas accès à une éducation de qualité.',
        'category': 'education',
        'country': 'Mali',
        'region': 'Afrique de l\'Ouest',
        'severity_level': 4,
        'affected_population': 25000000,
        'icon': '📚',
        'color': '#FFA726',
        'solutions': ['Écoles mobiles', 'Formation des enseignants', 'Technologie éducative'],
        'created_date': '2025-01-08'
    },
    {
        'id': 5,
        'title': 'Infrastructure énergétique insuffisante',
        'description': 'Le manque d\'infrastructure énergétique limite le développement économique.',
        'category': 'infrastructure',
        'country': 'Kenya',
        'region': 'Afrique de l\'Est',
        'severity_level': 3,
        'affected_population': 20000000,
        'icon': '⚡',
        'color': '#FFD54F',
        'solutions': ['Énergies renouvelables', 'Réseaux intelligents', 'Micro-grids'],
        'created_date': '2025-01-05'
    }
]

projects = [
    {
        'id': 1,
        'title': 'Centres de Formation Agricole',
        'description': 'Créer des centres de formation pour les agriculteurs locaux sur les techniques agricoles modernes.',
        'status': 'active',
        'required_budget': 500000,
        'expected_roi': 25,
        'implementation_timeline': '18 mois',
        'target_beneficiaries': 10000,
        'country': 'République Démocratique du Congo',
        'icon': '🎓',
        'color': '#96CEB4',
        'progress': 75,
        'start_date': '2024-06-01',
        'end_date': '2025-12-01',
        'partners': ['FAO', 'Banque Mondiale'],
        'category': 'agriculture'
    },
    {
        'id': 2,
        'title': 'Fermes Aquaponiques Urbaines',
        'description': 'Développer des fermes aquaponiques en milieu urbain pour produire des légumes et du poisson.',
        'status': 'active',
        'required_budget': 300000,
        'expected_roi': 30,
        'implementation_timeline': '12 mois',
        'target_beneficiaries': 5000,
        'country': 'Kenya',
        'icon': '🐟',
        'color': '#FFEAA7',
        'progress': 60,
        'start_date': '2024-08-01',
        'end_date': '2025-08-01',
        'partners': ['USAID', 'GIZ'],
        'category': 'agriculture'
    },
    {
        'id': 3,
        'title': 'Centres de Formation Technique',
        'description': 'Créer des centres de formation technique pour l\'industrialisation.',
        'status': 'proposed',
        'required_budget': 800000,
        'expected_roi': 20,
        'implementation_timeline': '24 mois',
        'target_beneficiaries': 15000,
        'country': 'Nigeria',
        'icon': '🔧',
        'color': '#DDA0DD',
        'progress': 0,
        'start_date': '2025-03-01',
        'end_date': '2027-03-01',
        'partners': ['Banque Africaine de Développement'],
        'category': 'education'
    },
    {
        'id': 4,
        'title': 'Systèmes de Purification d\'Eau',
        'description': 'Installer des systèmes de purification d\'eau dans les zones rurales.',
        'status': 'active',
        'required_budget': 400000,
        'expected_roi': 15,
        'implementation_timeline': '15 mois',
        'target_beneficiaries': 8000,
        'country': 'Éthiopie',
        'icon': '🚰',
        'color': '#98D8C8',
        'progress': 45,
        'start_date': '2024-09-01',
        'end_date': '2025-12-01',
        'partners': ['UNICEF', 'OMS'],
        'category': 'infrastructure'
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
        'project_id': 1,
        'icon': '💰',
        'color': '#DDA0DD',
        'investor': 'Fondation Bill & Melinda Gates',
        'date': '2024-06-15',
        'description': 'Subvention pour la formation agricole'
    },
    {
        'id': 2,
        'amount': 250000,
        'currency': 'USD',
        'investment_type': 'loan',
        'status': 'disbursed',
        'expected_return': 5,
        'project_id': 2,
        'icon': '🏦',
        'color': '#98D8C8',
        'investor': 'Banque Mondiale',
        'date': '2024-08-20',
        'description': 'Prêt pour les fermes aquaponiques'
    },
    {
        'id': 3,
        'amount': 150000,
        'currency': 'USD',
        'investment_type': 'grant',
        'status': 'pending',
        'expected_return': 0,
        'project_id': 4,
        'icon': '🌍',
        'color': '#FFB6C1',
        'investor': 'Union Européenne',
        'date': '2025-01-20',
        'description': 'Subvention pour l\'accès à l\'eau'
    }
]

# Statistiques globales
statistics = {
    'total_problems': len(problems),
    'total_projects': len(projects),
    'total_investments': len(investments),
    'total_budget': sum(p['required_budget'] for p in projects),
    'total_beneficiaries': sum(p['target_beneficiaries'] for p in projects),
    'active_projects': len([p for p in projects if p['status'] == 'active']),
    'total_investment_amount': sum(i['amount'] for i in investments),
    'countries_involved': len(set(p['country'] for p in projects))
}

# Template HTML complet avec toutes les fonctionnalités
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🌍 Solutions Afrique - Plateforme Complète UIVERSE.IO</title>
    
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Inter', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            overflow-x: hidden;
        }
        
        /* Animations UIVERSE.IO */
        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-20px); }
        }
        
        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
        }
        
        @keyframes slideInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        
        @keyframes shimmer {
            0% { background-position: -200px 0; }
            100% { background-position: calc(200px + 100%) 0; }
        }
        
        /* Classes d'animation */
        .float-animation {
            animation: float 6s ease-in-out infinite;
        }
        
        .pulse-animation {
            animation: pulse 2s ease-in-out infinite;
        }
        
        .slide-in-up {
            animation: slideInUp 0.8s ease-out;
        }
        
        .fade-in {
            animation: fadeIn 1s ease-out;
        }
        
        .shimmer {
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
            background-size: 200px 100%;
            animation: shimmer 2s infinite;
        }
        
        /* Glassmorphism */
        .glass {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 20px;
        }
        
        /* Cards modernes */
        .modern-card {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 20px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }
        
        .modern-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
        }
        
        /* Navigation moderne */
        .nav-item {
            position: relative;
            transition: all 0.3s ease;
        }
        
        .nav-item::after {
            content: '';
            position: absolute;
            bottom: -5px;
            left: 0;
            width: 0;
            height: 2px;
            background: linear-gradient(90deg, #667eea, #764ba2);
            transition: width 0.3s ease;
        }
        
        .nav-item:hover::after {
            width: 100%;
        }
        
        /* Boutons modernes */
        .btn-modern {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 50px;
            font-weight: 600;
            transition: all 0.3s ease;
            cursor: pointer;
            position: relative;
            overflow: hidden;
        }
        
        .btn-modern:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 25px rgba(102, 126, 234, 0.4);
        }
        
        .btn-modern::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
            transition: left 0.5s;
        }
        
        .btn-modern:hover::before {
            left: 100%;
        }
        
        /* Particules flottantes */
        .particles {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: -1;
        }
        
        .particle {
            position: absolute;
            width: 4px;
            height: 4px;
            background: rgba(255, 255, 255, 0.5);
            border-radius: 50%;
            animation: float 8s infinite linear;
        }
        
        /* Progress bars */
        .progress-bar {
            width: 100%;
            height: 8px;
            background: rgba(0, 0, 0, 0.1);
            border-radius: 4px;
            overflow: hidden;
        }
        
        .progress-fill {
            height: 100%;
            background: linear-gradient(90deg, #667eea, #764ba2);
            border-radius: 4px;
            transition: width 0.3s ease;
        }
        
        /* Responsive */
        @media (max-width: 768px) {
            .glass {
                margin: 10px;
            }
            
            .modern-card {
                margin: 10px 0;
            }
        }
    </style>
</head>

<body>
    <!-- Particules de fond -->
    <div class="particles" id="particles"></div>
    
    <!-- Navigation -->
    <nav class="glass fixed top-0 left-0 right-0 z-50 m-4">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center h-16">
                <!-- Logo -->
                <div class="flex items-center space-x-3">
                    <div class="w-12 h-12 bg-gradient-to-r from-blue-500 to-purple-600 rounded-2xl flex items-center justify-center float-animation">
                        <i class="fas fa-globe-africa text-white text-xl"></i>
                    </div>
                    <h1 class="text-2xl font-bold text-white">Solutions Afrique</h1>
                </div>
                
                <!-- Navigation Links -->
                <div class="hidden md:flex space-x-8">
                    <button class="nav-item text-white font-medium hover:text-blue-200 transition-colors" onclick="showSection('home')">
                        <i class="fas fa-home mr-2"></i>Accueil
                    </button>
                    <button class="nav-item text-white font-medium hover:text-blue-200 transition-colors" onclick="showSection('problems')">
                        <i class="fas fa-exclamation-triangle mr-2"></i>Problèmes
                    </button>
                    <button class="nav-item text-white font-medium hover:text-blue-200 transition-colors" onclick="showSection('projects')">
                        <i class="fas fa-project-diagram mr-2"></i>Projets
                    </button>
                    <button class="nav-item text-white font-medium hover:text-blue-200 transition-colors" onclick="showSection('investments')">
                        <i class="fas fa-chart-line mr-2"></i>Investissements
                    </button>
                    <button class="nav-item text-white font-medium hover:text-blue-200 transition-colors" onclick="showSection('dashboard')">
                        <i class="fas fa-tachometer-alt mr-2"></i>Tableau de Bord
                    </button>
                </div>
                
                <!-- Mobile menu button -->
                <div class="md:hidden">
                    <button class="text-white" onclick="toggleMobileMenu()">
                        <i class="fas fa-bars text-xl"></i>
                    </button>
                </div>
            </div>
        </div>
    </nav>
    
    <!-- Mobile Menu -->
    <div id="mobileMenu" class="md:hidden fixed top-0 left-0 right-0 bg-black bg-opacity-50 z-40 hidden">
        <div class="glass m-4 mt-20 p-4">
            <div class="flex flex-col space-y-4">
                <button class="text-white font-medium" onclick="showSection('home'); toggleMobileMenu()">
                    <i class="fas fa-home mr-2"></i>Accueil
                </button>
                <button class="text-white font-medium" onclick="showSection('problems'); toggleMobileMenu()">
                    <i class="fas fa-exclamation-triangle mr-2"></i>Problèmes
                </button>
                <button class="text-white font-medium" onclick="showSection('projects'); toggleMobileMenu()">
                    <i class="fas fa-project-diagram mr-2"></i>Projets
                </button>
                <button class="text-white font-medium" onclick="showSection('investments'); toggleMobileMenu()">
                    <i class="fas fa-chart-line mr-2"></i>Investissements
                </button>
                <button class="text-white font-medium" onclick="showSection('dashboard'); toggleMobileMenu()">
                    <i class="fas fa-tachometer-alt mr-2"></i>Tableau de Bord
                </button>
            </div>
        </div>
    </div>
    
    <!-- Main Content -->
    <main class="pt-24 pb-8">
        <!-- Section Accueil -->
        <section id="home" class="section active">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <!-- Hero Section -->
                <div class="text-center mb-16 slide-in-up">
                    <h1 class="text-5xl md:text-7xl font-bold text-white mb-6">
                        🌍 Solutions Afrique
                    </h1>
                    <p class="text-xl md:text-2xl text-blue-100 mb-8 max-w-3xl mx-auto">
                        Connecter les Problèmes aux Solutions pour un Développement Durable
                    </p>
                    <div class="flex flex-wrap justify-center gap-4">
                        <button class="btn-modern pulse-animation" onclick="showSection('problems')">
                            <i class="fas fa-search mr-2"></i>Explorer les Problèmes
                        </button>
                        <button class="btn-modern pulse-animation" onclick="showSection('projects')">
                            <i class="fas fa-rocket mr-2"></i>Découvrir les Solutions
                        </button>
                    </div>
                </div>
                
                <!-- Stats Cards -->
                <div class="grid grid-cols-1 md:grid-cols-4 gap-8 mb-16">
                    <div class="modern-card p-6 text-center fade-in" style="animation-delay: 0.1s;">
                        <div class="text-4xl mb-4">🌍</div>
                        <h3 class="text-xl font-bold text-gray-800 mb-2">Problèmes Identifiés</h3>
                        <p class="text-3xl font-bold text-blue-600" id="problemsCount">0</p>
                    </div>
                    <div class="modern-card p-6 text-center fade-in" style="animation-delay: 0.2s;">
                        <div class="text-4xl mb-4">🚀</div>
                        <h3 class="text-xl font-bold text-gray-800 mb-2">Projets Actifs</h3>
                        <p class="text-3xl font-bold text-green-600" id="projectsCount">0</p>
                    </div>
                    <div class="modern-card p-6 text-center fade-in" style="animation-delay: 0.3s;">
                        <div class="text-4xl mb-4">💰</div>
                        <h3 class="text-xl font-bold text-gray-800 mb-2">Investissements</h3>
                        <p class="text-3xl font-bold text-purple-600" id="investmentsCount">0</p>
                    </div>
                    <div class="modern-card p-6 text-center fade-in" style="animation-delay: 0.4s;">
                        <div class="text-4xl mb-4">👥</div>
                        <h3 class="text-xl font-bold text-gray-800 mb-2">Bénéficiaires</h3>
                        <p class="text-3xl font-bold text-orange-600" id="beneficiariesCount">0</p>
                    </div>
                </div>
                
                <!-- Mission Section -->
                <div class="glass p-8 mb-16 fade-in">
                    <h2 class="text-3xl font-bold text-white mb-6 text-center">Notre Mission</h2>
                    <p class="text-lg text-blue-100 text-center leading-relaxed">
                        Cette plateforme a été conçue pour créer un pont entre les problèmes récurrents en Afrique 
                        et les solutions innovantes qui peuvent les résoudre. Notre mission est de faciliter la 
                        connexion entre les entrepreneurs, les investisseurs et les experts pour créer un impact 
                        positif durable.
                    </p>
                </div>
            </div>
        </section>
        
        <!-- Section Problèmes -->
        <section id="problems" class="section hidden">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="text-center mb-12 slide-in-up">
                    <h2 class="text-4xl font-bold text-white mb-4">Problèmes Identifiés</h2>
                    <p class="text-xl text-blue-100">Découvrez les défis majeurs auxquels fait face l'Afrique</p>
                </div>
                
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8" id="problemsContainer">
                    <!-- Les problèmes seront chargés ici -->
                </div>
            </div>
        </section>
        
        <!-- Section Projets -->
        <section id="projects" class="section hidden">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="text-center mb-12 slide-in-up">
                    <h2 class="text-4xl font-bold text-white mb-4">Projets Solutions</h2>
                    <p class="text-xl text-blue-100">Des solutions concrètes et innovantes</p>
                </div>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8" id="projectsContainer">
                    <!-- Les projets seront chargés ici -->
                </div>
            </div>
        </section>
        
        <!-- Section Investissements -->
        <section id="investments" class="section hidden">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="text-center mb-12 slide-in-up">
                    <h2 class="text-4xl font-bold text-white mb-4">Investissements</h2>
                    <p class="text-xl text-blue-100">Suivi des financements et retours sur investissement</p>
                </div>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8" id="investmentsContainer">
                    <!-- Les investissements seront chargés ici -->
                </div>
            </div>
        </section>
        
        <!-- Section Tableau de Bord -->
        <section id="dashboard" class="section hidden">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="text-center mb-12 slide-in-up">
                    <h2 class="text-4xl font-bold text-white mb-4">Tableau de Bord</h2>
                    <p class="text-xl text-blue-100">Vue d'ensemble et statistiques</p>
                </div>
                
                <!-- Statistiques détaillées -->
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 mb-12">
                    <div class="modern-card p-6 text-center">
                        <div class="text-3xl mb-2">📊</div>
                        <h3 class="text-lg font-bold text-gray-800">Budget Total</h3>
                        <p class="text-2xl font-bold text-blue-600" id="totalBudget">$0</p>
                    </div>
                    <div class="modern-card p-6 text-center">
                        <div class="text-3xl mb-2">🎯</div>
                        <h3 class="text-lg font-bold text-gray-800">Projets Actifs</h3>
                        <p class="text-2xl font-bold text-green-600" id="activeProjects">0</p>
                    </div>
                    <div class="modern-card p-6 text-center">
                        <div class="text-3xl mb-2">🌍</div>
                        <h3 class="text-lg font-bold text-gray-800">Pays Impliqués</h3>
                        <p class="text-2xl font-bold text-purple-600" id="countriesInvolved">0</p>
                    </div>
                    <div class="modern-card p-6 text-center">
                        <div class="text-3xl mb-2">💼</div>
                        <h3 class="text-lg font-bold text-gray-800">Investissements</h3>
                        <p class="text-2xl font-bold text-orange-600" id="totalInvestments">$0</p>
                    </div>
                </div>
                
                <!-- Graphiques et visualisations -->
                <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
                    <div class="modern-card p-6">
                        <h3 class="text-xl font-bold text-gray-800 mb-4">Répartition par Catégorie</h3>
                        <div id="categoryChart" class="h-64 flex items-center justify-center text-gray-500">
                            <i class="fas fa-chart-pie text-4xl"></i>
                        </div>
                    </div>
                    <div class="modern-card p-6">
                        <h3 class="text-xl font-bold text-gray-800 mb-4">Progression des Projets</h3>
                        <div id="progressChart" class="space-y-4">
                            <!-- Les barres de progression seront générées ici -->
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </main>
    
    <!-- Footer -->
    <footer class="glass m-4 mt-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
            <div class="text-center">
                <p class="text-white">&copy; 2025 Solutions Afrique. Tous droits réservés.</p>
                <p class="text-blue-200 mt-2">🌍 Connecter les problèmes aux solutions pour un développement durable de l'Afrique</p>
            </div>
        </div>
    </footer>
    
    <script>
        // Gestionnaire d'animations UIVERSE.IO complet
        class CompleteUiverseManager {
            constructor() {
                this.init();
            }
            
            init() {
                this.createParticles();
                this.setupAnimations();
                this.loadData();
                this.setupEventListeners();
            }
            
            createParticles() {
                const particlesContainer = document.getElementById('particles');
                for (let i = 0; i < 50; i++) {
                    const particle = document.createElement('div');
                    particle.className = 'particle';
                    particle.style.left = Math.random() * 100 + '%';
                    particle.style.top = Math.random() * 100 + '%';
                    particle.style.animationDelay = Math.random() * 8 + 's';
                    particle.style.animationDuration = (Math.random() * 4 + 4) + 's';
                    particlesContainer.appendChild(particle);
                }
            }
            
            setupAnimations() {
                this.animateCounters();
                this.setupScrollAnimations();
            }
            
            setupEventListeners() {
                // Écouter les changements de section
                window.addEventListener('hashchange', () => {
                    const hash = window.location.hash.slice(1);
                    if (hash) {
                        showSection(hash);
                    }
                });
            }
            
            animateCounters() {
                const counters = document.querySelectorAll('[id$="Count"]');
                counters.forEach(counter => {
                    const target = parseInt(counter.textContent);
                    let current = 0;
                    const increment = target / 50;
                    const timer = setInterval(() => {
                        current += increment;
                        if (current >= target) {
                            current = target;
                            clearInterval(timer);
                        }
                        counter.textContent = Math.floor(current);
                    }, 50);
                });
            }
            
            setupScrollAnimations() {
                const observer = new IntersectionObserver((entries) => {
                    entries.forEach(entry => {
                        if (entry.isIntersecting) {
                            entry.target.classList.add('fade-in');
                        }
                    });
                });
                
                document.querySelectorAll('.modern-card').forEach(card => {
                    observer.observe(card);
                });
            }
            
            async loadData() {
                try {
                    // Charger les problèmes
                    const problemsResponse = await fetch('/api/problems');
                    const problems = await problemsResponse.json();
                    this.renderProblems(problems);
                    
                    // Charger les projets
                    const projectsResponse = await fetch('/api/projects');
                    const projects = await projectsResponse.json();
                    this.renderProjects(projects);
                    
                    // Charger les investissements
                    const investmentsResponse = await fetch('/api/investments');
                    const investments = await investmentsResponse.json();
                    this.renderInvestments(investments);
                    
                    // Charger les statistiques
                    const statsResponse = await fetch('/api/statistics');
                    const stats = await statsResponse.json();
                    this.updateDashboard(stats);
                    
                    // Mettre à jour les compteurs
                    this.updateCounters(stats);
                    
                } catch (error) {
                    console.error('Erreur lors du chargement des données:', error);
                }
            }
            
            renderProblems(problems) {
                const container = document.getElementById('problemsContainer');
                container.innerHTML = problems.map(problem => `
                    <div class="modern-card p-6 slide-in-up" style="animation-delay: ${Math.random() * 0.5}s;">
                        <div class="flex items-center mb-4">
                            <div class="text-3xl mr-3">${problem.icon}</div>
                            <div>
                                <h3 class="text-xl font-bold text-gray-800">${problem.title}</h3>
                                <p class="text-gray-600">${problem.country}</p>
                            </div>
                        </div>
                        <p class="text-gray-700 mb-4">${problem.description}</p>
                        <div class="flex justify-between items-center mb-3">
                            <span class="px-3 py-1 bg-red-100 text-red-800 rounded-full text-sm">
                                Niveau ${problem.severity_level}/5
                            </span>
                            <span class="text-gray-500 text-sm">
                                ${problem.affected_population.toLocaleString()} personnes
                            </span>
                        </div>
                        <div class="text-sm text-gray-600">
                            <strong>Solutions proposées:</strong>
                            <ul class="mt-2 space-y-1">
                                ${problem.solutions.map(s => `<li>• ${s}</li>`).join('')}
                            </ul>
                        </div>
                    </div>
                `).join('');
            }
            
            renderProjects(projects) {
                const container = document.getElementById('projectsContainer');
                container.innerHTML = projects.map(project => `
                    <div class="modern-card p-6 slide-in-up" style="animation-delay: ${Math.random() * 0.5}s;">
                        <div class="flex items-center mb-4">
                            <div class="text-3xl mr-3">${project.icon}</div>
                            <div>
                                <h3 class="text-xl font-bold text-gray-800">${project.title}</h3>
                                <p class="text-gray-600">${project.country}</p>
                            </div>
                        </div>
                        <p class="text-gray-700 mb-4">${project.description}</p>
                        
                        <!-- Barre de progression -->
                        <div class="mb-4">
                            <div class="flex justify-between text-sm text-gray-600 mb-1">
                                <span>Progression</span>
                                <span>${project.progress}%</span>
                            </div>
                            <div class="progress-bar">
                                <div class="progress-fill" style="width: ${project.progress}%"></div>
                            </div>
                        </div>
                        
                        <div class="grid grid-cols-2 gap-4 text-sm mb-4">
                            <div>
                                <span class="text-gray-500">Budget:</span>
                                <span class="font-bold">$${project.required_budget.toLocaleString()}</span>
                            </div>
                            <div>
                                <span class="text-gray-500">ROI:</span>
                                <span class="font-bold text-green-600">${project.expected_roi}%</span>
                            </div>
                        </div>
                        
                        <div class="flex justify-between items-center">
                            <span class="px-3 py-1 bg-blue-100 text-blue-800 rounded-full text-sm">
                                ${project.status}
                            </span>
                            <span class="text-gray-500 text-sm">
                                ${project.target_beneficiaries.toLocaleString()} bénéficiaires
                            </span>
                        </div>
                    </div>
                `).join('');
            }
            
            renderInvestments(investments) {
                const container = document.getElementById('investmentsContainer');
                container.innerHTML = investments.map(investment => `
                    <div class="modern-card p-6 slide-in-up" style="animation-delay: ${Math.random() * 0.5}s;">
                        <div class="flex items-center mb-4">
                            <div class="text-3xl mr-3">${investment.icon}</div>
                            <div>
                                <h3 class="text-xl font-bold text-gray-800">
                                    ${investment.investment_type === 'grant' ? 'Subvention' : 'Prêt'}
                                </h3>
                                <p class="text-gray-600">${investment.investor}</p>
                            </div>
                        </div>
                        <p class="text-gray-700 mb-4">${investment.description}</p>
                        <div class="grid grid-cols-2 gap-4 text-sm">
                            <div>
                                <span class="text-gray-500">Montant:</span>
                                <span class="font-bold">$${investment.amount.toLocaleString()}</span>
                            </div>
                            <div>
                                <span class="text-gray-500">Retour:</span>
                                <span class="font-bold text-green-600">${investment.expected_return}%</span>
                            </div>
                        </div>
                        <div class="mt-4 flex justify-between items-center">
                            <span class="px-3 py-1 bg-green-100 text-green-800 rounded-full text-sm">
                                ${investment.status}
                            </span>
                            <span class="text-gray-500 text-sm">
                                ${new Date(investment.date).toLocaleDateString()}
                            </span>
                        </div>
                    </div>
                `).join('');
            }
            
            updateDashboard(stats) {
                document.getElementById('totalBudget').textContent = `$${stats.total_budget.toLocaleString()}`;
                document.getElementById('activeProjects').textContent = stats.active_projects;
                document.getElementById('countriesInvolved').textContent = stats.countries_involved;
                document.getElementById('totalInvestments').textContent = `$${stats.total_investment_amount.toLocaleString()}`;
            }
            
            updateCounters(stats) {
                document.getElementById('problemsCount').textContent = stats.total_problems;
                document.getElementById('projectsCount').textContent = stats.total_projects;
                document.getElementById('investmentsCount').textContent = stats.total_investments;
                document.getElementById('beneficiariesCount').textContent = stats.total_beneficiaries.toLocaleString();
            }
        }
        
        // Navigation
        function showSection(sectionId) {
            // Masquer toutes les sections
            document.querySelectorAll('.section').forEach(section => {
                section.classList.add('hidden');
                section.classList.remove('active');
            });
            
            // Afficher la section sélectionnée
            const targetSection = document.getElementById(sectionId);
            targetSection.classList.remove('hidden');
            targetSection.classList.add('active');
            
            // Mettre à jour l'URL
            window.location.hash = sectionId;
        }
        
        function toggleMobileMenu() {
            const menu = document.getElementById('mobileMenu');
            menu.classList.toggle('hidden');
        }
        
        // Initialisation
        document.addEventListener('DOMContentLoaded', () => {
            new CompleteUiverseManager();
            
            // Vérifier l'URL au chargement
            const hash = window.location.hash.slice(1);
            if (hash) {
                showSection(hash);
            }
        });
    </script>
</body>
</html>
'''

# Routes API complètes
@app.route('/')
def index():
    return HTML_TEMPLATE

@app.route('/api/problems')
def get_problems():
    return jsonify(problems)

@app.route('/api/projects')
def get_projects():
    return jsonify(projects)

@app.route('/api/investments')
def get_investments():
    return jsonify(investments)

@app.route('/api/statistics')
def get_statistics():
    return jsonify(statistics)

@app.route('/api/health')
def health_check():
    return {'status': 'healthy', 'message': 'Solutions Afrique Complete API', 'timestamp': datetime.now().isoformat()}

# Routes pour les nouvelles fonctionnalités
@app.route('/api/problems/<int:problem_id>')
def get_problem(problem_id):
    problem = next((p for p in problems if p['id'] == problem_id), None)
    if problem:
        return jsonify(problem)
    return jsonify({'error': 'Problème non trouvé'}), 404

@app.route('/api/projects/<int:project_id>')
def get_project(project_id):
    project = next((p for p in projects if p['id'] == project_id), None)
    if project:
        return jsonify(project)
    return jsonify({'error': 'Projet non trouvé'}), 404

@app.route('/api/investments/<int:investment_id>')
def get_investment(investment_id):
    investment = next((i for i in investments if i['id'] == investment_id), None)
    if investment:
        return jsonify(investment)
    return jsonify({'error': 'Investissement non trouvé'}), 404

if __name__ == '__main__':
    print("🚀 Démarrage de Solutions Afrique - Version Complète UIVERSE.IO")
    print("🌍 Accédez à http://localhost:5000")
    print("✨ Interface moderne avec toutes les fonctionnalités")
    print("📊 Tableau de bord et statistiques intégrés")
    app.run(host='0.0.0.0', port=5000, debug=True) 