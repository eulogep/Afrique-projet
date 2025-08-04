// Global variables
let currentSection = 'hero';
let problems = [];
let projects = [];
let investments = [];
let charts = {};

// API Base URL
const API_BASE = '/api';

// Initialize the application
document.addEventListener('DOMContentLoaded', function() {
    initializeApp();
});

async function initializeApp() {
    try {
        showLoading(true);
        await loadAllData();
        updateStats();
        initializeCharts();
        showSection('hero');
        showLoading(false);
        showNotification('Plateforme chargée avec succès!', 'success');
    } catch (error) {
        console.error('Erreur lors de l\'initialisation:', error);
        showNotification('Erreur lors du chargement des données', 'error');
        showLoading(false);
    }
}

// Data loading functions
async function loadAllData() {
    try {
        const [problemsResponse, projectsResponse, investmentsResponse] = await Promise.all([
            fetch(`${API_BASE}/problems`),
            fetch(`${API_BASE}/projects`),
            fetch(`${API_BASE}/investments`)
        ]);

        problems = await problemsResponse.json();
        projects = await projectsResponse.json();
        investments = await investmentsResponse.json();

        console.log('Données chargées:', { problems, projects, investments });
    } catch (error) {
        console.error('Erreur lors du chargement des données:', error);
        throw error;
    }
}

// Navigation functions
function showSection(sectionName) {
    // Hide all sections
    document.querySelectorAll('.section').forEach(section => {
        section.classList.add('hidden');
    });
    
    // Hide hero section
    const heroSection = document.getElementById('hero');
    if (heroSection) {
        heroSection.style.display = sectionName === 'hero' ? 'block' : 'none';
    }
    
    // Show target section
    const targetSection = document.getElementById(`${sectionName}-section`);
    if (targetSection) {
        targetSection.classList.remove('hidden');
    }
    
    // Update navigation
    updateNavigation(sectionName);
    
    // Load section-specific content
    switch(sectionName) {
        case 'problems':
            renderProblems();
            break;
        case 'projects':
            renderProjects();
            break;
        case 'investments':
            renderInvestments();
            break;
        case 'dashboard':
            renderDashboard();
            break;
    }
    
    currentSection = sectionName;
}

function updateNavigation(activeSection) {
    document.querySelectorAll('.nav-btn').forEach(btn => {
        btn.classList.remove('text-blue-600', 'font-semibold');
        btn.classList.add('text-gray-700');
    });
}

// Stats functions
function updateStats() {
    animateCounter('problems-count', problems.length);
    animateCounter('projects-count', projects.length);
    animateCounter('investments-count', investments.length);
    
    // Calculer le total des bénéficiaires des projets ET des personnes affectées par les problèmes
    const totalBeneficiaries = projects.reduce((sum, project) => sum + (project.beneficiaries_targeted || 0), 0);
    const totalAffected = problems.reduce((sum, problem) => sum + (problem.population_affected || 0), 0);
    const totalImpact = totalBeneficiaries + totalAffected;
    
    animateCounter('beneficiaries-count', totalImpact);
}

function animateCounter(elementId, targetValue) {
    const element = document.getElementById(elementId);
    if (!element) return;
    
    let currentValue = 0;
    const increment = targetValue / 50;
    const timer = setInterval(() => {
        currentValue += increment;
        if (currentValue >= targetValue) {
            currentValue = targetValue;
            clearInterval(timer);
        }
        element.textContent = Math.floor(currentValue).toLocaleString();
    }, 30);
}

// Rendering functions
function renderProblems(filteredProblems = null) {
    const problemsGrid = document.getElementById('problems-grid');
    if (!problemsGrid) return;
    
    const problemsToRender = filteredProblems || problems;
    
    problemsGrid.innerHTML = problemsToRender.map(problem => `
        <div class="bg-white rounded-lg shadow-md p-6 card-hover problem-card cursor-pointer" onclick="showProblemDetail(${problem.id})">
            <div class="flex justify-between items-start mb-4">
                <div class="flex items-center">
                    <i class="fas fa-exclamation-triangle text-orange-500 text-xl mr-3"></i>
                    <span class="text-xs font-semibold px-2 py-1 rounded-full ${getCategoryColor(problem.category)} text-white">
                        ${getCategoryLabel(problem.category)}
                    </span>
                </div>
                <div class="flex items-center">
                    ${getSeverityStars(problem.severity_level)}
                    <span class="ml-2 text-sm font-medium text-gray-600">Niveau ${problem.severity_level}</span>
                </div>
            </div>
            
            <h3 class="text-lg font-semibold text-gray-800 mb-3">${problem.title}</h3>
            <p class="text-gray-600 text-sm mb-4 line-clamp-3">${problem.description}</p>
            
            <div class="space-y-2 text-sm text-gray-500">
                <div class="flex items-center">
                    <i class="fas fa-map-marker-alt mr-2 text-red-500"></i>
                    <span>${problem.country}${problem.region ? `, ${problem.region}` : ''}</span>
                </div>
                <div class="flex items-center">
                    <i class="fas fa-users mr-2 text-blue-500"></i>
                    <span>${(problem.population_affected || 0).toLocaleString()} personnes affectées</span>
                </div>
                <div class="flex items-center justify-between mt-4">
                    <span class="text-xs text-gray-400">
                        <i class="fas fa-lightbulb mr-1"></i>
                        ${getRelatedProjectsCount(problem.id)} solution(s) proposée(s)
                    </span>
                    <button class="text-blue-600 hover:text-blue-800 text-sm font-medium">
                        Voir détails <i class="fas fa-arrow-right ml-1"></i>
                    </button>
                </div>
            </div>
        </div>
    `).join('');
}

function renderProjects(filteredProjects = null) {
    const projectsGrid = document.getElementById('projects-grid');
    if (!projectsGrid) return;
    
    const projectsToRender = filteredProjects || projects;
    
    projectsGrid.innerHTML = projectsToRender.map(project => `
        <div class="bg-white rounded-lg shadow-md p-6 card-hover project-card cursor-pointer" onclick="showProjectDetail(${project.id})">
            <div class="flex justify-between items-start mb-4">
                <span class="text-xs font-semibold px-3 py-1 rounded-full ${getStatusColor(project.status)} text-white">
                    ${getStatusLabel(project.status)}
                </span>
                <span class="text-sm text-gray-500">${project.timeline || 'Timeline non définie'}</span>
            </div>
            
            <h3 class="text-lg font-semibold text-gray-800 mb-3">${project.title}</h3>
            <p class="text-gray-600 text-sm mb-4 line-clamp-3">${project.description}</p>
            
            <div class="grid grid-cols-2 gap-4 mb-4">
                <div class="text-center p-3 bg-blue-50 rounded-lg">
                    <div class="text-xl font-bold text-blue-600">$${(project.budget_required || 0).toLocaleString()}</div>
                    <div class="text-xs text-gray-500">Budget requis</div>
                </div>
                <div class="text-center p-3 bg-green-50 rounded-lg">
                    <div class="text-xl font-bold text-green-600">${project.expected_roi || 0}%</div>
                    <div class="text-xs text-gray-500">ROI attendu</div>
                </div>
            </div>
            
            <div class="space-y-2 text-sm text-gray-500">
                <div class="flex items-center">
                    <i class="fas fa-map-marker-alt mr-2 text-red-500"></i>
                    <span>${project.country || 'Pays non spécifié'}</span>
                    <span class="ml-auto">
                        <i class="fas fa-users mr-1 text-blue-500"></i>
                        ${(project.beneficiaries_targeted || 0).toLocaleString()} bénéficiaires
                    </span>
                </div>
                
                <div class="flex items-center justify-between mt-4">
                    <span class="text-xs text-gray-400">
                        <i class="fas fa-chart-line mr-1"></i>
                        ${getProjectInvestmentsCount(project.id)} investissement(s)
                    </span>
                    <span class="text-xs font-medium ${getProjectFundingColor(project)}">
                        $${getProjectFunding(project.id).toLocaleString()} levés
                    </span>
                </div>
            </div>
            
            <!-- Progress Bar -->
            <div class="mt-4">
                <div class="flex justify-between text-xs text-gray-500 mb-1">
                    <span>Financement</span>
                    <span>${getProjectFundingPercentage(project)}%</span>
                </div>
                <div class="w-full bg-gray-200 rounded-full h-2">
                    <div class="progress-bar" style="width: ${getProjectFundingPercentage(project)}%"></div>
                </div>
            </div>
        </div>
    `).join('');
}

function renderInvestments(filteredInvestments = null) {
    const investmentsGrid = document.getElementById('investments-grid');
    if (!investmentsGrid) return;
    
    const investmentsToRender = filteredInvestments || investments;
    
    // Update investment summary
    updateInvestmentSummary();
    
    investmentsGrid.innerHTML = investmentsToRender.map(investment => `
        <div class="bg-white rounded-lg shadow-md p-6 card-hover investment-card cursor-pointer" onclick="showInvestmentDetail(${investment.id})">
            <div class="flex justify-between items-start mb-4">
                <div class="flex items-center">
                    <i class="fas ${getInvestmentTypeIcon(investment.investment_type)} text-2xl mr-3 ${getInvestmentTypeColor(investment.investment_type)}"></i>
                    <span class="text-xs font-semibold px-2 py-1 rounded-full ${getInvestmentStatusColor(investment.status)} text-white">
                        ${getInvestmentStatusLabel(investment.status)}
                    </span>
                </div>
            </div>
            
            <div class="text-center mb-4">
                <div class="text-2xl font-bold text-gray-800">
                    ${investment.amount.toLocaleString()} ${investment.currency}
                </div>
                <div class="text-sm text-gray-500">Montant investi</div>
            </div>
            
            <div class="space-y-3">
                <div class="flex justify-between items-center">
                    <span class="text-sm text-gray-600">Type:</span>
                    <span class="text-sm font-medium">${getInvestmentTypeLabel(investment.investment_type)}</span>
                </div>
                
                <div class="flex justify-between items-center">
                    <span class="text-sm text-gray-600">Retour attendu:</span>
                    <span class="text-sm font-medium text-green-600">${investment.expected_return || 0}%</span>
                </div>
                
                <div class="flex justify-between items-center">
                    <span class="text-sm text-gray-600">Date:</span>
                    <span class="text-sm text-gray-500">${formatDate(investment.investment_date)}</span>
                </div>
            </div>
            
            ${investment.terms ? `
                <div class="mt-4 p-3 bg-gray-50 rounded-lg">
                    <div class="text-xs text-gray-500 mb-1">Conditions:</div>
                    <div class="text-sm text-gray-700 line-clamp-2">${investment.terms}</div>
                </div>
            ` : ''}
        </div>
    `).join('');
}

function renderDashboard() {
    renderRecentActivity();
    updateCharts();
}

function renderRecentActivity() {
    const activityContainer = document.getElementById('recent-activity');
    if (!activityContainer) return;
    
    const activities = [
        ...problems.slice(-3).map(p => ({
            type: 'problem',
            title: p.title,
            date: p.created_at || new Date().toISOString(),
            icon: 'fas fa-exclamation-triangle',
            color: 'text-orange-500'
        })),
        ...projects.slice(-3).map(p => ({
            type: 'project',
            title: p.title,
            date: p.created_at || new Date().toISOString(),
            icon: 'fas fa-lightbulb',
            color: 'text-green-500'
        })),
        ...investments.slice(-3).map(i => ({
            type: 'investment',
            title: `Investissement de ${i.amount} ${i.currency}`,
            date: i.investment_date || new Date().toISOString(),
            icon: 'fas fa-chart-line',
            color: 'text-blue-500'
        }))
    ].sort((a, b) => new Date(b.date) - new Date(a.date)).slice(0, 10);
    
    activityContainer.innerHTML = activities.map(activity => `
        <div class="flex items-center p-4 bg-gray-50 rounded-lg">
            <div class="flex-shrink-0">
                <i class="${activity.icon} ${activity.color} text-lg"></i>
            </div>
            <div class="ml-4 flex-1">
                <div class="text-sm font-medium text-gray-800">${activity.title}</div>
                <div class="text-xs text-gray-500">${formatDate(activity.date)}</div>
            </div>
            <div class="text-xs text-gray-400 capitalize">${activity.type}</div>
        </div>
    `).join('');
}

// Chart functions
function initializeCharts() {
    initializeProblemsChart();
    initializeROIChart();
}

function initializeProblemsChart() {
    const ctx = document.getElementById('problemsChart');
    if (!ctx) return;
    
    const categoryData = problems.reduce((acc, problem) => {
        const category = getCategoryLabel(problem.category);
        acc[category] = (acc[category] || 0) + 1;
        return acc;
    }, {});
    
    charts.problemsChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: Object.keys(categoryData),
            datasets: [{
                data: Object.values(categoryData),
                backgroundColor: [
                    '#f59e0b',
                    '#ef4444',
                    '#3b82f6',
                    '#10b981'
                ],
                borderWidth: 2,
                borderColor: '#ffffff'
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'bottom'
                }
            }
        }
    });
}

function initializeROIChart() {
    const ctx = document.getElementById('roiChart');
    if (!ctx) return;
    
    const projectData = projects.map(project => ({
        title: project.title.substring(0, 20) + '...',
        roi: project.expected_roi || 0
    })).slice(0, 6);
    
    charts.roiChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: projectData.map(p => p.title),
            datasets: [{
                label: 'ROI (%)',
                data: projectData.map(p => p.roi),
                backgroundColor: 'rgba(102, 126, 234, 0.8)',
                borderColor: 'rgba(102, 126, 234, 1)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        callback: function(value) {
                            return value + '%';
                        }
                    }
                }
            },
            plugins: {
                legend: {
                    display: false
                }
            }
        }
    });
}

function updateCharts() {
    if (charts.problemsChart) {
        const categoryData = problems.reduce((acc, problem) => {
            const category = getCategoryLabel(problem.category);
            acc[category] = (acc[category] || 0) + 1;
            return acc;
        }, {});
        
        charts.problemsChart.data.labels = Object.keys(categoryData);
        charts.problemsChart.data.datasets[0].data = Object.values(categoryData);
        charts.problemsChart.update();
    }
    
    if (charts.roiChart) {
        const projectData = projects.map(project => ({
            title: project.title.substring(0, 20) + '...',
            roi: project.expected_roi || 0
        })).slice(0, 6);
        
        charts.roiChart.data.labels = projectData.map(p => p.title);
        charts.roiChart.data.datasets[0].data = projectData.map(p => p.roi);
        charts.roiChart.update();
    }
}

// Filter functions
function filterProblems() {
    const category = document.getElementById('category-filter')?.value;
    const country = document.getElementById('country-filter')?.value;
    const severity = document.getElementById('severity-filter')?.value;
    
    let filtered = problems;
    
    if (category) {
        filtered = filtered.filter(p => p.category === category);
    }
    
    if (country) {
        filtered = filtered.filter(p => p.country === country);
    }
    
    if (severity) {
        filtered = filtered.filter(p => p.severity_level == severity);
    }
    
    renderProblems(filtered);
    showNotification(`${filtered.length} problème(s) trouvé(s)`, 'info');
}

function filterProjects() {
    const status = document.getElementById('status-filter')?.value;
    const budgetMin = document.getElementById('budget-min')?.value;
    const budgetMax = document.getElementById('budget-max')?.value;
    const roiFilter = document.getElementById('roi-filter')?.value;
    
    let filtered = projects;
    
    if (status) {
        filtered = filtered.filter(p => p.status === status);
    }
    
    if (budgetMin) {
        filtered = filtered.filter(p => (p.budget_required || 0) >= parseInt(budgetMin));
    }
    
    if (budgetMax) {
        filtered = filtered.filter(p => (p.budget_required || 0) <= parseInt(budgetMax));
    }
    
    if (roiFilter) {
        filtered = filtered.filter(p => (p.expected_roi || 0) >= parseInt(roiFilter));
    }
    
    renderProjects(filtered);
    showNotification(`${filtered.length} projet(s) trouvé(s)`, 'info');
}

// Modal functions
function showAddModal() {
    document.getElementById('add-modal').classList.add('show');
    switchTab('problem');
}

function closeModal(modalId) {
    document.getElementById(modalId).classList.remove('show');
}

function switchTab(tabName) {
    // Update tab buttons
    document.querySelectorAll('[id^="tab-"]').forEach(tab => {
        tab.className = 'tab-inactive px-4 py-2 rounded-lg font-medium';
    });
    document.getElementById(`tab-${tabName}`).className = 'tab-active px-4 py-2 rounded-lg font-medium';
    
    // Update tab content
    document.querySelectorAll('.tab-content').forEach(content => {
        content.classList.add('hidden');
    });
    document.getElementById(`form-${tabName}`).classList.remove('hidden');
}

// Detail modal functions
function showProblemDetail(problemId) {
    const problem = problems.find(p => p.id === problemId);
    if (!problem) return;
    
    const relatedProjects = projects.filter(p => p.problem_id === problemId);
    
    document.getElementById('detail-title').textContent = problem.title;
    document.getElementById('detail-content').innerHTML = `
        <div class="space-y-6">
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                <div class="bg-orange-50 p-4 rounded-lg">
                    <div class="text-sm text-gray-600">Catégorie</div>
                    <div class="font-semibold">${getCategoryLabel(problem.category)}</div>
                </div>
                <div class="bg-red-50 p-4 rounded-lg">
                    <div class="text-sm text-gray-600">Niveau de sévérité</div>
                    <div class="font-semibold">${problem.severity_level}/5</div>
                </div>
                <div class="bg-blue-50 p-4 rounded-lg">
                    <div class="text-sm text-gray-600">Population affectée</div>
                    <div class="font-semibold">${(problem.population_affected || 0).toLocaleString()}</div>
                </div>
            </div>
            
            <div>
                <h3 class="text-lg font-semibold mb-2">Description</h3>
                <p class="text-gray-700">${problem.description}</p>
            </div>
            
            <div>
                <h3 class="text-lg font-semibold mb-2">Localisation</h3>
                <p class="text-gray-700">
                    <i class="fas fa-map-marker-alt mr-2"></i>
                    ${problem.country}${problem.region ? `, ${problem.region}` : ''}
                </p>
            </div>
            
            ${relatedProjects.length > 0 ? `
                <div>
                    <h3 class="text-lg font-semibold mb-4">Solutions Proposées (${relatedProjects.length})</h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        ${relatedProjects.map(project => `
                            <div class="border border-gray-200 p-4 rounded-lg">
                                <h4 class="font-medium text-gray-800 mb-2">${project.title}</h4>
                                <p class="text-sm text-gray-600 mb-2">${project.description.substring(0, 100)}...</p>
                                <div class="flex justify-between text-xs text-gray-500">
                                    <span>Budget: $${(project.budget_required || 0).toLocaleString()}</span>
                                    <span>ROI: ${project.expected_roi || 0}%</span>
                                </div>
                            </div>
                        `).join('')}
                    </div>
                </div>
            ` : ''}
        </div>
    `;
    
    document.getElementById('detail-modal').classList.add('show');
}

function showProjectDetail(projectId) {
    const project = projects.find(p => p.id === projectId);
    if (!project) return;
    
    const relatedInvestments = investments.filter(i => i.project_id === projectId);
    const totalFunding = relatedInvestments.reduce((sum, inv) => sum + inv.amount, 0);
    const fundingPercentage = project.budget_required ? (totalFunding / project.budget_required * 100) : 0;
    
    document.getElementById('detail-title').textContent = project.title;
    document.getElementById('detail-content').innerHTML = `
        <div class="space-y-6">
            <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
                <div class="bg-blue-50 p-4 rounded-lg">
                    <div class="text-sm text-gray-600">Budget requis</div>
                    <div class="font-semibold">$${(project.budget_required || 0).toLocaleString()}</div>
                </div>
                <div class="bg-green-50 p-4 rounded-lg">
                    <div class="text-sm text-gray-600">ROI attendu</div>
                    <div class="font-semibold">${project.expected_roi || 0}%</div>
                </div>
                <div class="bg-purple-50 p-4 rounded-lg">
                    <div class="text-sm text-gray-600">Bénéficiaires</div>
                    <div class="font-semibold">${(project.beneficiaries_targeted || 0).toLocaleString()}</div>
                </div>
                <div class="bg-yellow-50 p-4 rounded-lg">
                    <div class="text-sm text-gray-600">Timeline</div>
                    <div class="font-semibold">${project.timeline || 'Non définie'}</div>
                </div>
            </div>
            
            <div>
                <h3 class="text-lg font-semibold mb-2">Description du Projet</h3>
                <p class="text-gray-700">${project.description}</p>
            </div>
            
            <div>
                <h3 class="text-lg font-semibold mb-4">Financement</h3>
                <div class="bg-gray-50 p-4 rounded-lg">
                    <div class="flex justify-between text-sm text-gray-600 mb-2">
                        <span>Progression du financement</span>
                        <span>${fundingPercentage.toFixed(1)}%</span>
                    </div>
                    <div class="w-full bg-gray-200 rounded-full h-3">
                        <div class="progress-bar" style="width: ${Math.min(fundingPercentage, 100)}%"></div>
                    </div>
                    <div class="flex justify-between text-sm text-gray-600 mt-2">
                        <span>Levé: $${totalFunding.toLocaleString()}</span>
                        <span>Objectif: $${(project.budget_required || 0).toLocaleString()}</span>
                    </div>
                </div>
            </div>
            
            ${relatedInvestments.length > 0 ? `
                <div>
                    <h3 class="text-lg font-semibold mb-4">Investissements (${relatedInvestments.length})</h3>
                    <div class="space-y-3">
                        ${relatedInvestments.map(investment => `
                            <div class="border border-gray-200 p-4 rounded-lg">
                                <div class="flex justify-between items-center">
                                    <div>
                                        <span class="font-medium">${investment.amount.toLocaleString()} ${investment.currency}</span>
                                        <span class="text-sm text-gray-500 ml-2">(${getInvestmentTypeLabel(investment.investment_type)})</span>
                                    </div>
                                    <span class="text-xs px-2 py-1 rounded-full ${getInvestmentStatusColor(investment.status)} text-white">
                                        ${getInvestmentStatusLabel(investment.status)}
                                    </span>
                                </div>
                                <div class="text-sm text-gray-600 mt-1">
                                    Retour attendu: ${investment.expected_return || 0}% • ${formatDate(investment.investment_date)}
                                </div>
                            </div>
                        `).join('')}
                    </div>
                </div>
            ` : ''}
        </div>
    `;
    
    document.getElementById('detail-modal').classList.add('show');
}

function showInvestmentDetail(investmentId) {
    const investment = investments.find(i => i.id === investmentId);
    if (!investment) return;
    
    const relatedProject = projects.find(p => p.id === investment.project_id);
    
    document.getElementById('detail-title').textContent = `Investissement de ${investment.amount.toLocaleString()} ${investment.currency}`;
    document.getElementById('detail-content').innerHTML = `
        <div class="space-y-6">
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                <div class="bg-blue-50 p-4 rounded-lg">
                    <div class="text-sm text-gray-600">Montant</div>
                    <div class="font-semibold">${investment.amount.toLocaleString()} ${investment.currency}</div>
                </div>
                <div class="bg-green-50 p-4 rounded-lg">
                    <div class="text-sm text-gray-600">Type</div>
                    <div class="font-semibold">${getInvestmentTypeLabel(investment.investment_type)}</div>
                </div>
                <div class="bg-purple-50 p-4 rounded-lg">
                    <div class="text-sm text-gray-600">Retour attendu</div>
                    <div class="font-semibold">${investment.expected_return || 0}%</div>
                </div>
            </div>
            
            <div>
                <h3 class="text-lg font-semibold mb-2">Statut</h3>
                <span class="px-3 py-1 rounded-full ${getInvestmentStatusColor(investment.status)} text-white font-medium">
                    ${getInvestmentStatusLabel(investment.status)}
                </span>
            </div>
            
            <div>
                <h3 class="text-lg font-semibold mb-2">Date d'investissement</h3>
                <p class="text-gray-700">${formatDate(investment.investment_date)}</p>
            </div>
            
            ${investment.terms ? `
                <div>
                    <h3 class="text-lg font-semibold mb-2">Conditions</h3>
                    <p class="text-gray-700">${investment.terms}</p>
                </div>
            ` : ''}
            
            ${relatedProject ? `
                <div>
                    <h3 class="text-lg font-semibold mb-4">Projet Associé</h3>
                    <div class="border border-gray-200 p-4 rounded-lg">
                        <h4 class="font-medium text-gray-800 mb-2">${relatedProject.title}</h4>
                        <p class="text-sm text-gray-600 mb-2">${relatedProject.description.substring(0, 200)}...</p>
                        <div class="grid grid-cols-2 gap-4 text-xs text-gray-500">
                            <span>Budget total: $${(relatedProject.budget_required || 0).toLocaleString()}</span>
                            <span>ROI projet: ${relatedProject.expected_roi || 0}%</span>
                        </div>
                    </div>
                </div>
            ` : ''}
        </div>
    `;
    
    document.getElementById('detail-modal').classList.add('show');
}

// Form submission functions
async function submitProblem(event) {
    event.preventDefault();
    
    const formData = {
        title: document.getElementById('problem-title').value,
        description: document.getElementById('problem-description').value,
        category: document.getElementById('problem-category').value,
        country: document.getElementById('problem-country').value,
        region: document.getElementById('problem-region').value,
        severity_level: parseInt(document.getElementById('problem-severity').value),
        population_affected: parseInt(document.getElementById('problem-population').value) || 0
    };
    
    try {
        const response = await fetch(`${API_BASE}/problems`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });
        
        if (response.ok) {
            const newProblem = await response.json();
            problems.push(newProblem);
            closeModal('add-modal');
            renderProblems();
            updateStats();
            updateCharts(); // Ajouter la mise à jour des graphiques
            showNotification('Problème ajouté avec succès!', 'success');
            event.target.reset();
        } else {
            throw new Error('Erreur lors de l\'ajout du problème');
        }
    } catch (error) {
        console.error('Erreur:', error);
        showNotification('Erreur lors de l\'ajout du problème', 'error');
    }
}

async function submitProject(event) {
    event.preventDefault();
    
    const formData = {
        title: document.getElementById('project-title').value,
        description: document.getElementById('project-description').value,
        status: document.getElementById('project-status').value,
        budget_required: parseInt(document.getElementById('project-budget').value) || 0,
        expected_roi: parseInt(document.getElementById('project-roi').value) || 0,
        timeline: document.getElementById('project-timeline').value,
        country: document.getElementById('project-country').value,
        beneficiaries_targeted: parseInt(document.getElementById('project-beneficiaries').value) || 0
    };
    
    try {
        const response = await fetch(`${API_BASE}/projects`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });
        
        if (response.ok) {
            const newProject = await response.json();
            projects.push(newProject);
            closeModal('add-modal');
            renderProjects();
            updateStats();
            updateCharts(); // Ajouter la mise à jour des graphiques
            showNotification('Projet ajouté avec succès!', 'success');
            event.target.reset();
        } else {
            throw new Error('Erreur lors de l\'ajout du projet');
        }
    } catch (error) {
        console.error('Erreur:', error);
        showNotification('Erreur lors de l\'ajout du projet', 'error');
    }
}

async function submitInvestment(event) {
    event.preventDefault();
    
    const formData = {
        amount: parseFloat(document.getElementById('investment-amount').value),
        currency: document.getElementById('investment-currency').value,
        investment_type: document.getElementById('investment-type').value,
        status: document.getElementById('investment-status').value,
        expected_return: parseFloat(document.getElementById('investment-return').value) || 0,
        terms: document.getElementById('investment-terms').value,
        investment_date: new Date().toISOString().split('T')[0]
    };
    
    try {
        const response = await fetch(`${API_BASE}/investments`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });
        
        if (response.ok) {
            const newInvestment = await response.json();
            investments.push(newInvestment);
            closeModal('add-modal');
            renderInvestments();
            updateStats();
            updateCharts(); // Ajouter la mise à jour des graphiques
            showNotification('Investissement ajouté avec succès!', 'success');
            event.target.reset();
        } else {
            throw new Error('Erreur lors de l\'ajout de l\'investissement');
        }
    } catch (error) {
        console.error('Erreur:', error);
        showNotification('Erreur lors de l\'ajout de l\'investissement', 'error');
    }
}

// Utility functions
function showLoading(show) {
    const loading = document.getElementById('loading');
    if (loading) {
        loading.classList.toggle('show', show);
    }
}

function showNotification(message, type = 'info') {
    const notification = document.getElementById('notification');
    const notificationText = document.getElementById('notification-text');
    
    if (notification && notificationText) {
        notificationText.textContent = message;
        notification.className = `notification ${type}`;
        notification.classList.add('show');
        
        setTimeout(() => {
            notification.classList.remove('show');
        }, 3000);
    }
}

function updateInvestmentSummary() {
    const totalInvested = investments.reduce((sum, inv) => sum + inv.amount, 0);
    const fundedProjects = new Set(investments.map(inv => inv.project_id)).size;
    const avgROI = investments.length > 0 ? 
        investments.reduce((sum, inv) => sum + (inv.expected_return || 0), 0) / investments.length : 0;
    
    const totalInvestedEl = document.getElementById('total-invested');
    const fundedProjectsEl = document.getElementById('funded-projects');
    const avgROIEl = document.getElementById('average-roi');
    
    if (totalInvestedEl) totalInvestedEl.textContent = `$${totalInvested.toLocaleString()}`;
    if (fundedProjectsEl) fundedProjectsEl.textContent = fundedProjects;
    if (avgROIEl) avgROIEl.textContent = `${avgROI.toFixed(1)}%`;
}

// Helper functions for data formatting
function getCategoryLabel(category) {
    const labels = {
        'socio-economic': 'Socio-économique',
        'security-stability': 'Sécurité et Stabilité'
    };
    return labels[category] || category;
}

function getCategoryColor(category) {
    const colors = {
        'socio-economic': 'bg-blue-500',
        'security-stability': 'bg-red-500'
    };
    return colors[category] || 'bg-gray-500';
}

function getStatusLabel(status) {
    const labels = {
        'proposed': 'Proposé',
        'funded': 'Financé',
        'in_progress': 'En cours',
        'completed': 'Terminé'
    };
    return labels[status] || status;
}

function getStatusColor(status) {
    const colors = {
        'proposed': 'bg-yellow-500',
        'funded': 'bg-green-500',
        'in_progress': 'bg-blue-500',
        'completed': 'bg-purple-500'
    };
    return colors[status] || 'bg-gray-500';
}

function getInvestmentTypeLabel(type) {
    const labels = {
        'loan': 'Prêt',
        'grant': 'Subvention',
        'equity': 'Equity',
        'donation': 'Don'
    };
    return labels[type] || type;
}

function getInvestmentTypeIcon(type) {
    const icons = {
        'loan': 'fa-handshake',
        'grant': 'fa-gift',
        'equity': 'fa-chart-pie',
        'donation': 'fa-heart'
    };
    return icons[type] || 'fa-dollar-sign';
}

function getInvestmentTypeColor(type) {
    const colors = {
        'loan': 'text-blue-600',
        'grant': 'text-green-600',
        'equity': 'text-purple-600',
        'donation': 'text-red-600'
    };
    return colors[type] || 'text-gray-600';
}

function getInvestmentStatusLabel(status) {
    const labels = {
        'pending': 'En attente',
        'approved': 'Approuvé',
        'disbursed': 'Décaissé',
        'completed': 'Terminé'
    };
    return labels[status] || status;
}

function getInvestmentStatusColor(status) {
    const colors = {
        'pending': 'bg-yellow-500',
        'approved': 'bg-green-500',
        'disbursed': 'bg-blue-500',
        'completed': 'bg-purple-500'
    };
    return colors[status] || 'bg-gray-500';
}

function getSeverityStars(level) {
    let stars = '';
    for (let i = 1; i <= 5; i++) {
        if (i <= level) {
            stars += '<i class="fas fa-star text-yellow-400"></i>';
        } else {
            stars += '<i class="far fa-star text-gray-300"></i>';
        }
    }
    return stars;
}

function getRelatedProjectsCount(problemId) {
    return projects.filter(p => p.problem_id === problemId).length;
}

function getProjectInvestmentsCount(projectId) {
    return investments.filter(i => i.project_id === projectId).length;
}

function getProjectFunding(projectId) {
    return investments
        .filter(i => i.project_id === projectId)
        .reduce((sum, inv) => sum + inv.amount, 0);
}

function getProjectFundingPercentage(project) {
    const funding = getProjectFunding(project.id);
    const budget = project.budget_required || 0;
    return budget > 0 ? Math.min((funding / budget) * 100, 100) : 0;
}

function getProjectFundingColor(project) {
    const percentage = getProjectFundingPercentage(project);
    if (percentage >= 100) return 'text-green-600';
    if (percentage >= 50) return 'text-blue-600';
    if (percentage >= 25) return 'text-yellow-600';
    return 'text-red-600';
}

function formatDate(dateString) {
    if (!dateString) return 'Date non spécifiée';
    const date = new Date(dateString);
    return date.toLocaleDateString('fr-FR', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    });
}

// Event listeners for modal closing
document.addEventListener('click', function(event) {
    if (event.target.classList.contains('modal')) {
        event.target.classList.remove('show');
    }
});

// Keyboard shortcuts
document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
        document.querySelectorAll('.modal.show').forEach(modal => {
            modal.classList.remove('show');
        });
    }
});

// Initialize on page load
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initializeApp);
} else {
    initializeApp();
}

