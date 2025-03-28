#!/bin/bash

echo "Création de l'environnement virtuel pour Analyseur de mots de passe (Linux)"

# Création d'un dossier projet si besoin
mkdir -p mon-projet-password
cd mon-projet-password

# Création de l'environnement virtuel
python3 -m venv venv

# Activation de l'environnement
source venv/bin/activate

# Mise à jour de pip et installation de Flask
pip install --upgrade pip
pip install flask

echo ""
echo "Environnement prêt !"
echo "Pour lancer le script :"
echo "python ../password_analyzer.py"
echo ""
echo "Pour lancer l'interface web :"
echo "cd ../webapp && flask run"
