import random
import nltk


class MotMystere:
    # nltk.download("punkt")
    fichier = open(
        "bovary.txt",
        encoding="utf-8",
    )
    bovary_string = fichier.read()
    bovary_liste = nltk.word_tokenize(bovary_string)

    DICTIONNAIRE = sorted(set([mot for mot in bovary_liste if len(mot) == 5]))

    NOMBRE_ESSAIS = 6

    # Initialisation des variables
    def __init__(self):
        self.GAME_OVER = False
        self.mot = random.choice(self.DICTIONNAIRE).lower()
        self.lettres_mot = list(self.mot)
        self.essais = 1

    def jouer(self):
        while not self.GAME_OVER:
            # Si le joueur a dépassé le nombre d'essais, il a perdu
            if self.essais > self.NOMBRE_ESSAIS:
                print(
                    "Vous avez perdu! Le mot que vous cherchiez était:", self.mot, "\n"
                )
                self.GAME_OVER = True
                break

            print("Mot mystère:", self.mot)
            print("Essai", self.essais, "/", self.NOMBRE_ESSAIS)
            mot_essai = input("Entrez le mot d'essai: ").lower()

            if not mot_essai.isalpha():
                print("Entrez uniquement des lettres!\n")
                continue

            if len(mot_essai) != len(self.mot):
                print("Le mot doit avoir", len(self.mot), "lettres!\n")
                continue

            lettres_essai = list(mot_essai)

            # Si le mot d'essai est le mot mystère, le joueur a gagné
            if mot_essai == self.mot:
                print("Vous avez gagné!")
                self.GAME_OVER = True
            else:
                lettres_indices = []

                # Vérifie si les lettres sont dans le mot mystère
                for i in range(len(self.lettres_mot)):
                    if lettres_essai[i] == self.lettres_mot[i]:
                        lettres_indices.append("✔")
                    elif lettres_essai[i] in self.lettres_mot:
                        lettres_indices.append("+")
                    else:
                        lettres_indices.append("✘")

                # On repasse sur + pour vérifier qu'il n'y a pas de doublons
                for i in range(len(lettres_indices)):
                    if lettres_indices[i] == "+":
                        compteur_memes_lettres = lettres_essai.count(lettres_essai[i])
                        while compteur_memes_lettres > self.lettres_mot.count(
                            lettres_essai[i]
                        ):
                            lettres_indices[i] = "✘"
                            lettres_essai[i] = " "
                            compteur_memes_lettres -= 1

                print(lettres_indices)
                self.essais += 1


def main():
    play_again = True
    while play_again:
        jeu = MotMystere()
        jeu.jouer()
        replay = input("Voulez-vous jouer à nouveau ? (oui/non): ").lower()
        play_again = replay == "oui"


if __name__ == "__main__":
    main()
