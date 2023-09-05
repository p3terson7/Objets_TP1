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

        lettres_trouvees = []
        essais = 1
        while GAME_OVER == False:
            print("Essai", essais, "/", MotMystere.NOMBRE_ESSAIS)
            mot_essai = input("Entrez motEssai: ")

            if mot_essai == mot:
                print("Vous avez gagné!")
                GAME_OVER = True


# MotMystere.__init__()
