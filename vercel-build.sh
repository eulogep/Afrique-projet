#!/bin/bash

# Script de build pour Vercel
echo "🚀 Démarrage du build Vercel..."

# Créer le dossier database s'il n'existe pas
mkdir -p database

# Initialiser la base de données
echo "📊 Initialisation de la base de données..."
python init_db.py

# Peupler la base de données avec les données d'exemple
echo "🌱 Peuplement de la base de données..."
python seed_database.py

echo "✅ Build terminé avec succès!"
