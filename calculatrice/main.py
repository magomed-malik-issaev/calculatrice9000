def calculatrice():
    while True:
        try:
            # Demande à l'utilisateur d'entrer une expression mathématique
            expression = input("Entrez une expression mathématique (q pour quitter) : ")

            # Vérifie si l'utilisateur souhaite quitter le programme
            if expression.lower() == 'q':
                print("Au revoir !")
                break

            # Évalue l'expression mathématique
            resultat = evaluer_expression(expression)
            print("Résultat :", resultat)

        except ValueError:
            print("Erreur : Entrée invalide. Veuillez entrer une expression mathématique valide.")
        except ZeroDivisionError:
            print("Erreur : Division par zéro.")

def evaluer_expression(expression):
    # Supprime les espaces inutiles de l'expression
    expression = expression.replace(" ", "")

    # Liste des opérateurs pris en charge
    operateurs = ['+', '-', '*', '/']

    # Recherche de l'opérateur dans l'expression
    for operateur in operateurs:
        if operateur in expression:
            # Divise l'expression en deux parties à l'emplacement de l'opérateur
            partie_gauche, partie_droite = expression.split(operateur)

            # Convertit les parties en nombres
            nombre_gauche = convertir_en_nombre(partie_gauche)
            nombre_droite = convertir_en_nombre(partie_droite)

            # Effectue l'opération correspondante à l'opérateur
            if operateur == '+':
                return nombre_gauche + nombre_droite
            elif operateur == '-':
                return nombre_gauche - nombre_droite
            elif operateur == '*':
                return nombre_gauche * nombre_droite
            elif operateur == '/':
                return nombre_gauche / nombre_droite

    # Si aucun opérateur n'est trouvé, l'expression est invalide
    raise ValueError

def convertir_en_nombre(chaine):
    # Tente de convertir la chaîne en nombre entier ou décimal
    try:
        return int(chaine)
    except ValueError:
        return float(chaine)

# Appel de la fonction principale
calculatrice()