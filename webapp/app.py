from flask import Flask, render_template, request
import re

app = Flask(__name__)

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append(" Augmenter la longueur (≥ 8 caractères)")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append(" Ajouter une majuscule")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append(" Ajouter un chiffre")

    if re.search(r"[^a-zA-Z0-9]", password):
        score += 1
    else:
        feedback.append(" Ajouter un symbole")

    return score, feedback

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    feedback = []
    password = ""
    if request.method == "POST":
        password = request.form["password"]
        result, feedback = check_password_strength(password)
    return render_template("index.html", result=result, feedback=feedback, password=password)

if __name__ == "__main__":
    app.run(debug=True)