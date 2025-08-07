# 🚀 Guide de Déploiement Vercel - Plateforme Solutions Afrique

## 📋 **Prérequis**

- Compte Vercel (gratuit) : [vercel.com](https://vercel.com)
- Projet Git (GitHub, GitLab, Bitbucket)
- Code source de la plateforme

## 🔧 **Fichiers de Configuration Créés**

### ✅ **Fichiers ajoutés pour Vercel :**
- `vercel.json` - Configuration principale de Vercel
- `api/index.py` - Point d'entrée pour Vercel
- `runtime.txt` - Version Python spécifiée
- `vercel-build.sh` - Script de build personnalisé
- `.gitignore` - Exclusion des fichiers non nécessaires
- `DEPLOYMENT_GUIDE.md` - Ce guide

### ✅ **Fichiers modifiés :**
- `main.py` - Compatibilité Vercel
- `requirements.txt` - Versions mises à jour

## 🚀 **Étapes de Déploiement**

### **1. Préparation du Repository**

```bash
# Vérifier que tous les fichiers sont commités
git add .
git commit -m "🚀 Préparation pour déploiement Vercel"
git push origin main
```

### **2. Connexion à Vercel**

1. **Aller sur [vercel.com](https://vercel.com)**
2. **Se connecter** avec votre compte GitHub/GitLab
3. **Cliquer sur "New Project"**

### **3. Import du Projet**

1. **Sélectionner** votre repository
2. **Vérifier** la configuration :
   - **Framework Preset** : Other
   - **Root Directory** : `./` (racine)
   - **Build Command** : `chmod +x vercel-build.sh && ./vercel-build.sh`
   - **Output Directory** : (laisser vide)
   - **Install Command** : `pip install -r requirements.txt`

### **4. Variables d'Environnement**

Dans les paramètres du projet Vercel, ajouter :

```env
FLASK_ENV=production
SECRET_KEY=votre_clé_secrète_ici
DATABASE_URL=sqlite:///database/app.db
```

### **5. Déploiement**

1. **Cliquer sur "Deploy"**
2. **Attendre** la fin du build (2-3 minutes)
3. **Vérifier** les logs de build

## 🔍 **Vérification du Déploiement**

### **Tests à effectuer :**

1. **Page d'accueil** : `https://votre-projet.vercel.app/`
2. **API Health** : `https://votre-projet.vercel.app/api/health`
3. **Initialisation DB** : `POST https://votre-projet.vercel.app/api/init-db`

### **Endpoints à tester :**

```bash
# Test de santé
curl https://votre-projet.vercel.app/api/health

# Test des problèmes
curl https://votre-projet.vercel.app/api/problems

# Test des projets
curl https://votre-projet.vercel.app/api/projects

# Test des investissements
curl https://votre-projet.vercel.app/api/investments
```

## 🛠️ **Configuration Avancée**

### **Base de Données PostgreSQL (Recommandé)**

Pour une base de données persistante :

1. **Créer** une base PostgreSQL (Vercel Postgres, Supabase, etc.)
2. **Ajouter** la variable d'environnement :
   ```env
   DATABASE_URL=postgresql://user:password@host:port/database
   ```

### **Domaines Personnalisés**

1. **Aller** dans les paramètres du projet
2. **Ajouter** votre domaine personnalisé
3. **Configurer** les DNS selon les instructions

### **Variables d'Environnement Avancées**

```env
# Production
FLASK_ENV=production
SECRET_KEY=votre_clé_très_sécurisée
DATABASE_URL=postgresql://...

# Développement
FLASK_ENV=development
DEBUG=true
```

## 🔧 **Dépannage**

### **Erreurs Courantes :**

#### **1. Build Failed**
```bash
# Vérifier les logs Vercel
# Problème souvent lié aux dépendances
```

**Solution :** Mettre à jour `requirements.txt`

#### **2. Database Connection Error**
```bash
# Erreur de connexion à la base de données
```

**Solution :** Vérifier `DATABASE_URL` dans les variables d'environnement

#### **3. Static Files Not Found**
```bash
# Fichiers statiques non trouvés
```

**Solution :** Vérifier le chemin `src/static/` dans `main.py`

#### **4. CORS Errors**
```bash
# Erreurs CORS en développement
```

**Solution :** Vérifier la configuration CORS dans `main.py`

### **Logs de Debug**

```bash
# Voir les logs en temps réel
vercel logs --follow

# Voir les logs d'une fonction spécifique
vercel logs --function=main
```

## 📊 **Monitoring et Analytics**

### **Vercel Analytics**
1. **Activer** Vercel Analytics
2. **Configurer** les événements personnalisés
3. **Surveiller** les performances

### **Health Checks**
```bash
# Endpoint de santé automatique
curl https://votre-projet.vercel.app/api/health
```

## 🔄 **Mises à Jour**

### **Déploiement Automatique**
- **Chaque push** sur la branche main déclenche un déploiement
- **Pull Requests** créent des previews automatiques

### **Rollback**
1. **Aller** dans les déploiements Vercel
2. **Sélectionner** une version précédente
3. **Cliquer** sur "Promote to Production"

## 📱 **Performance**

### **Optimisations Appliquées :**
- ✅ **Compression** automatique des assets
- ✅ **CDN** global de Vercel
- ✅ **Cache** intelligent
- ✅ **Edge Functions** pour les API

### **Métriques à Surveiller :**
- **Temps de réponse** API
- **Temps de chargement** pages
- **Taux d'erreur** 4xx/5xx
- **Utilisation** des ressources

## 🎉 **Félicitations !**

Votre **Plateforme Solutions Afrique** est maintenant déployée sur Vercel !

### **URL de Production :**
`https://votre-projet.vercel.app`

### **Prochaines Étapes :**
1. **Tester** toutes les fonctionnalités
2. **Configurer** un domaine personnalisé
3. **Mettre en place** le monitoring
4. **Partager** l'URL avec votre équipe

---

**🌍 Votre plateforme est maintenant accessible partout dans le monde !**
