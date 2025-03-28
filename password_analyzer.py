import re

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔸 Augmenter la longueur (≥ 8 caractères)")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("🔸 Ajouter une majuscule")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("🔸 Ajouter un chiffre")

    if re.search(r"[^a-zA-Z0-9]", password):
        score += 1
    else:
        feedback.append("🔸 Ajouter un symbole")

    return score, feedback

def main():
    with open("passwords.txt", "r") as file:
        passwords = [line.strip() for line in file.readlines()]

    for pwd in passwords:
        score, fb = check_password_strength(pwd)
        print(f"[{pwd}] Score: {score}/4")
        if score < 4:
            for f in fb:
                print("→", f)
        print()
        
if __name__ == "__main__":
    main()