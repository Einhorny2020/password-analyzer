# Analyseur de mots de passe (Cybersécurité)

Ce projet permet d'analyser la robustesse d'une liste de mots de passe et propose une interface web simple pour tester des entrées manuelles.

## Fichiers inclus

- `password_analyzer.py` : script principal
- `passwords.txt` : fichier d'exemple
- `webapp/` : interface web Flask
- Scripts d'installation : `.sh` et `.bat`
- `README.md` : ce guide

## Lancer le script en local

### Sous macOS/Linux
```bash
chmod +x install_env_password_mac.sh
./install_env_password_mac.sh
python3 -m venv venv
source venv/bin/activate
python password_analyzer.py
```
### Pour linux si pas déja fait
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

### Sous Windows
```bat
install_env_password_windows.bat
venv\Scripts\activate
python password_analyzer.py
```

## Lancer l'interface web

```bash
pip install flask
cd webapp
flask run
```

Accès via : http://localhost:5000

