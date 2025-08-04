// Script pour corriger le problème d'API et de chargement des données

// Fonction pour vérifier et corriger les endpoints API
function fixAPIEndpoints() {
    // Vérifier si les données sont chargées
    console.log('Vérification des données...');
    console.log('Problems:', problems.length);
    console.log('Projects:', projects.length);
    console.log('Investments:', investments.length);
    
    // Si les données ne sont pas chargées, essayer de les recharger
    if (problems.length === 0 || projects.length === 0 || investments.length === 0) {
        console.log('Rechargement des données...');
        loadAllData().then(() => {
            updateStats();
            renderProblems();
            renderProjects();
            renderInvestments();
            updateCharts();
        }).catch(error => {
            console.error('Erreur lors du rechargement:', error);
        });
    }
}

// Fonction pour corriger les statistiques
function fixStats() {
    // Recalculer les statistiques avec les bonnes données
    const totalProblems = problems.length;
    const totalProjects = projects.length;
    const totalInvestments = investments.length;
    
    // Calculer le total des personnes affectées et bénéficiaires
    const totalAffected = problems.reduce((sum, problem) => sum + (problem.population_affected || 0), 0);
    const totalBeneficiaries = projects.reduce((sum, project) => sum + (project.beneficiaries_targeted || 0), 0);
    const totalImpact = totalAffected + totalBeneficiaries;
    
    console.log('Statistiques corrigées:');
    console.log('Problèmes:', totalProblems);
    console.log('Projets:', totalProjects);
    console.log('Investissements:', totalInvestments);
    console.log('Impact total:', totalImpact);
    
    // Mettre à jour l'affichage
    document.getElementById('problems-count').textContent = totalProblems;
    document.getElementById('projects-count').textContent = totalProjects;
    document.getElementById('investments-count').textContent = totalInvestments;
    document.getElementById('beneficiaries-count').textContent = totalImpact.toLocaleString();
}

// Exécuter les corrections au chargement
document.addEventListener('DOMContentLoaded', function() {
    setTimeout(() => {
        fixAPIEndpoints();
        fixStats();
    }, 2000);
});

// Ajouter un bouton de correction d'urgence
function addFixButton() {
    const fixButton = document.createElement('button');
    fixButton.textContent = 'Corriger les données';
    fixButton.className = 'fixed bottom-4 right-4 bg-red-500 text-white px-4 py-2 rounded-lg z-50';
    fixButton.onclick = () => {
        fixAPIEndpoints();
        fixStats();
    };
    document.body.appendChild(fixButton);
}

// Ajouter le bouton après le chargement
setTimeout(addFixButton, 1000);

