#!/bin/bash
echo "Création de l'environnement pour analyseur de mots de passe"
mkdir -p mon-projet-password
cd mon-projet-password
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip flask
echo "Prêt à l'emploi !"