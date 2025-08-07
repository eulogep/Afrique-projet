# 🚀 Guide de Déploiement Vercel - Étapes Détaillées

## 📋 **Situation Actuelle**
✅ **Repository local créé** : `africa-solutions-platform-vercel`  
✅ **Fichiers de configuration Vercel** : Tous présents  
✅ **Token Vercel** : `lhfoFyVgU0D4CTp46VD7mnGm`  
🔄 **Prochaine étape** : Créer le repository GitHub et déployer

---

## 🎯 **Étapes de Déploiement**

### **1. Créer le Repository GitHub**

1. **Aller sur [github.com](https://github.com)**
2. **Cliquer sur "New repository"**
3. **Nom** : `africa-solutions-platform`
4. **Description** : `Plateforme Solutions Afrique - Projet complet avec API Flask et interface moderne`
5. **Visibilité** : Public (recommandé pour Vercel)
6. **NE PAS** cocher "Initialize this repository with a README"
7. **Cliquer sur "Create repository"**

### **2. Connecter le Repository Local à GitHub**

```bash
# Remplacez YOUR_USERNAME par votre nom d'utilisateur GitHub
git remote add origin https://github.com/YOUR_USERNAME/africa-solutions-platform.git
git branch -M main
git push -u origin main
```

### **3. Déployer sur Vercel**

#### **Option A : Via l'Interface Web (Recommandé)**

1. **Aller sur [vercel.com](https://vercel.com)**
2. **Se connecter** avec votre compte GitHub
3. **Cliquer sur "New Project"**
4. **Sélectionner** votre repository `africa-solutions-platform`
5. **Configuration automatique** :
   - **Framework Preset** : Other
   - **Root Directory** : `./` (racine)
   - **Build Command** : `chmod +x vercel-build.sh && ./vercel-build.sh`
   - **Output Directory** : (laisser vide)
   - **Install Command** : `pip install -r requirements.txt`

#### **Option B : Via CLI Vercel**

```bash
# Installer Vercel CLI
npm install -g vercel

# Se connecter avec votre token
vercel login

# Déployer
vercel --token lhfoFyVgU0D4CTp46VD7mnGm
```

### **4. Configurer les Variables d'Environnement**

Dans les paramètres du projet Vercel :

```env
FLASK_ENV=production
SECRET_KEY=africa_solutions_2025_secure_key_vercel
DATABASE_URL=sqlite:///database/app.db
```

### **5. Déclencher le Déploiement**

1. **Cliquer sur "Deploy"**
2. **Attendre** la fin du build (2-3 minutes)
3. **Vérifier** les logs de build

---

## 🔍 **Vérification du Déploiement**

### **Tests Automatiques**

Une fois déployé, testez ces URLs :

```bash
# Page d'accueil
https://votre-projet.vercel.app/

# API Health Check
https://votre-projet.vercel.app/api/health

# Test des problèmes
https://votre-projet.vercel.app/api/problems

# Test des projets
https://votre-projet.vercel.app/api/projects

# Test des investissements
https://votre-projet.vercel.app/api/investments
```

### **Réponses Attendues**

```json
// GET /api/health
{
  "status": "healthy",
  "message": "Africa Solutions Platform API is running"
}

// GET /api/problems
[
  {
    "id": 1,
    "title": "Insécurité alimentaire",
    "country": "RDC",
    "severity": 5
  }
]
```

---

## 🛠️ **Dépannage**

### **Erreurs Courantes**

#### **1. Build Failed**
```bash
# Vérifier les logs Vercel
# Problème souvent lié aux dépendances Python
```

**Solution** : Vérifier `requirements.txt` et `runtime.txt`

#### **2. Database Connection Error**
```bash
# Erreur de connexion à la base de données
```

**Solution** : Vérifier `DATABASE_URL` dans les variables d'environnement

#### **3. Static Files Not Found**
```bash
# Fichiers statiques non trouvés
```

**Solution** : Vérifier le chemin `src/static/` dans `main.py`

### **Logs de Debug**

```bash
# Via l'interface Vercel
# Aller dans Functions > main.py > View Function Logs

# Via CLI
vercel logs --follow
```

---

## 📊 **Configuration Avancée**

### **Base de Données PostgreSQL (Optionnel)**

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

---

## 🎉 **Succès !**

Une fois déployé avec succès :

### **URL de Production**
`https://votre-projet.vercel.app`

### **Fonctionnalités Disponibles**
- ✅ **Page d'accueil** avec design moderne
- ✅ **API complète** pour problèmes, projets, investissements
- ✅ **Base de données** avec données d'exemple
- ✅ **Interface responsive** mobile et desktop
- ✅ **Animations** et effets visuels

### **Prochaines Étapes**
1. **Tester** toutes les fonctionnalités
2. **Configurer** un domaine personnalisé
3. **Partager** l'URL avec votre équipe
4. **Monitorer** les performances via Vercel Analytics

---

## 📞 **Support**

Si vous rencontrez des problèmes :

1. **Vérifier** les logs Vercel
2. **Consulter** le guide de dépannage
3. **Tester** localement avec `python main.py`
4. **Vérifier** la configuration dans `vercel.json`

---

**🌍 Votre plateforme sera bientôt accessible partout dans le monde !**
