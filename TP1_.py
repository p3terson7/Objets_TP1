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
        lettres_mot = [mot[i] for i in range(len(mot))]

        essais = 1
        while GAME_OVER == False:
            if essais > MotMystere.NOMBRE_ESSAIS:
                print("Vous avez perdu! Le mot que vous cherchiez était:", mot, "\n")
                GAME_OVER = True
                break

            print("Mot mystère:", mot)
            print("Essai", essais, "/", MotMystere.NOMBRE_ESSAIS)
            mot_essai = input("Entrez motEssai: ")

            if len(mot_essai) != len(mot):
                print("Le mot doit avoir", len(mot), "lettres!\n")
                continue
            lettres_essai = [mot_essai[i] for i in range(len(mot_essai))]

            lettres_trouvees = []
            lettres_indices = []

            if mot_essai == mot:
                print("Vous avez gagné!")
                GAME_OVER = True

            for i in range(len(lettres_mot)):
                if lettres_essai[i] == lettres_mot[i]:
                    lettres_indices.append("✔")
                elif lettres_essai[i] in lettres_mot:
                    lettres_indices.append("+")
                else:
                    lettres_indices.append("✘")
            for i in range(len(lettres_indices)):
                if lettres_indices[i] == "+":
                    compteur_memes_lettres = lettres_essai.count(lettres_essai[i])
                    while compteur_memes_lettres > lettres_mot.count(lettres_essai[i]):
                        lettres_indices[i] = "✘"
                        lettres_essai[i] = " "
                        compteur_memes_lettres -= 1
            print(lettres_indices)
            essais += 1


MotMystere.__init__()
