#!/usr/bin/env python3
"""
🌍 Solutions Afrique - Version UIVERSE.IO
Application moderne inspirée des meilleures pratiques de uiverse.io
"""

from flask import Flask, jsonify, send_from_directory, render_template_string
from flask_cors import CORS
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'solutions-afrique-uiverse-2025'

# Enable CORS
CORS(app)

# Données d'exemple modernisées
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
        'color': '#FF6B6B'
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
        'color': '#4ECDC4'
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
        'color': '#45B7D1'
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
        'country': 'République Démocratique du Congo',
        'icon': '🎓',
        'color': '#96CEB4'
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
        'country': 'Kenya',
        'icon': '🐟',
        'color': '#FFEAA7'
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
        'color': '#DDA0DD'
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
        'color': '#98D8C8'
    }
]

# Template HTML moderne inspiré de uiverse.io
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🌍 Solutions Afrique - Plateforme UIVERSE.IO</title>
    
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
                <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-16">
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
        // Gestionnaire d'animations UIVERSE.IO
        class UiverseManager {
            constructor() {
                this.init();
            }
            
            init() {
                this.createParticles();
                this.setupAnimations();
                this.loadData();
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
                // Animation des compteurs
                this.animateCounters();
                
                // Animation au scroll
                this.setupScrollAnimations();
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
                    
                    // Mettre à jour les compteurs
                    document.getElementById('problemsCount').textContent = problems.length;
                    document.getElementById('projectsCount').textContent = projects.length;
                    document.getElementById('investmentsCount').textContent = investments.length;
                    
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
                        <div class="flex justify-between items-center">
                            <span class="px-3 py-1 bg-red-100 text-red-800 rounded-full text-sm">
                                Niveau ${problem.severity_level}/5
                            </span>
                            <span class="text-gray-500 text-sm">
                                ${problem.affected_population.toLocaleString()} personnes
                            </span>
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
                        <div class="grid grid-cols-2 gap-4 text-sm">
                            <div>
                                <span class="text-gray-500">Budget:</span>
                                <span class="font-bold">$${project.required_budget.toLocaleString()}</span>
                            </div>
                            <div>
                                <span class="text-gray-500">ROI:</span>
                                <span class="font-bold text-green-600">${project.expected_roi}%</span>
                            </div>
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
                                <p class="text-gray-600">Projet #${investment.project_id}</p>
                            </div>
                        </div>
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
                        <div class="mt-4">
                            <span class="px-3 py-1 bg-green-100 text-green-800 rounded-full text-sm">
                                ${investment.status}
                            </span>
                        </div>
                    </div>
                `).join('');
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
        }
        
        function toggleMobileMenu() {
            const menu = document.getElementById('mobileMenu');
            menu.classList.toggle('hidden');
        }
        
        // Initialisation
        document.addEventListener('DOMContentLoaded', () => {
            new UiverseManager();
        });
    </script>
</body>
</html>
'''

# Routes simplifiées et optimisées
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

@app.route('/api/health')
def health_check():
    return {'status': 'healthy', 'message': 'Solutions Afrique UIVERSE.IO API'}

if __name__ == '__main__':
    print("🚀 Démarrage de Solutions Afrique - Version UIVERSE.IO")
    print("🌍 Accédez à http://localhost:5000")
    print("✨ Interface moderne inspirée de uiverse.io")
    app.run(host='0.0.0.0', port=5000, debug=True) 