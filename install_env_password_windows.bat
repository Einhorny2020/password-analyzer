@echo off
echo Création de l'environnement pour analyseur de mots de passe
mkdir mon-projet-password
cd mon-projet-password
python -m venv venv
call venv\Scripts\activate
pip install --upgrade pip flask
echo Environnement prêt.
pause