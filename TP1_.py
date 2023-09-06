import random


class MotMystere:
    NOMBRE_ESSAIS = 6
    DICTIONNAIRE = [
        "kiefs",
        "adire",
        "niche",
        "allee",
        "balle",
        "brise",
        "chien",
        "chiot",
        "aller",
        "finir",
    ]

    def __init__():
        GAME_OVER = False
        mot = random.choice(MotMystere.DICTIONNAIRE)
        lettres_manquantes = [mot[i] for i in range(len(mot))]

        essais = 1
        while GAME_OVER == False:
            if essais > MotMystere.NOMBRE_ESSAIS:
                print("Vous avez perdu! Le mot que vous cherchiez était:", mot, "\n")
                GAME_OVER = True
                break
            print("Mot mystère:", mot)
            print("Essai", essais, "/", MotMystere.NOMBRE_ESSAIS)
            mot_essai = input("Entrez motEssai: ")
            lettres_essai = [mot_essai[i] for i in range(len(mot_essai))]
            lettres_trouvees = []
            lettres_indices = []

            if mot_essai == mot:
                print("Vous avez gagné!")
                GAME_OVER = True

            for i in range(len(lettres_manquantes)):
                if lettres_essai[i] == lettres_manquantes[i]:
                    lettres_indices.append("✔")
                elif lettres_essai[i] in lettres_manquantes:
                    lettres_indices.append("\u002B")
                else:
                    lettres_indices.append("✘")
            print(lettres_indices)
            essais += 1


MotMystere.__init__()
