import random
from turtle import *
import turtle
import nltk


fichier = open(
    "bovary.txt",
    encoding="utf-8",
)
bovary_string = fichier.read()
bovary_liste = nltk.word_tokenize(bovary_string)
bovary_texte = nltk.Text(bovary_liste)
DICTIONNAIRE = sorted(set([mot for mot in bovary_liste if len(mot) == 5]))


# Setup turtle
tortue = Turtle()


def resetTortue():
    turtle.hideturtle()
    tortue.speed(3)
    tortue.pensize(3)
    tortue.penup()
    tortue.color("black")
    tortue.goto(-50, -50)  # Position initiale


class HangmanGame:
    xPosLettres = -100

    def __init__(self):
        self.nbEssais = 6
        self.GAME_OVER = False
        self.mot_mystere = random.choice(DICTIONNAIRE).lower()
        self.lettres_mot_mystere = list(self.mot_mystere)
        self.lettres_restantes = self.lettres_mot_mystere
        self.lettres_indices = ["", "", "", "", ""]

    def afficheLettres(self):
        for i in range(len(self.lettres_mot_mystere)):
            tortue.goto(self.xPosLettres + 50 * i, -200)
            tortue.pendown()
            tortue.forward(25)
            tortue.penup()

    def afficheLettre(self, lettre):
        tortue.goto(
            self.xPosLettres + 53 * self.lettres_mot_mystere.index(lettre), -199
        )
        tortue.pendown()
        tortue.write(lettre, font=("Arial", 25, "normal"))
        tortue.penup()

    def jouer(self):
        niveau = input("Quel niveau de jeu ? (1 ou 2) ")
        while not self.GAME_OVER:
            if self.nbEssais == 0:
                print(
                    "Vous avez perdu! Le mot que vous cherchiez était:",
                    self.mot_mystere,
                    "\n",
                )
                self.GAME_OVER = True
                break

            # Une fois toutes les lettres trouvées
            if self.lettres_restantes == ["", "", "", "", ""]:
                print("Vous avez gagné!")
                self.GAME_OVER = True
                break

            print(self.lettres_indices)
            print("Nombre d'essais: " + str(self.nbEssais))
            print("Mot mystère:", self.mot_mystere)
            print(self.lettres_restantes)
            lettre_essai = input("Votre lettre: ").lower()

            if not lettre_essai.isalpha():
                print("Entrez uniquement des lettres!\n")
                continue

            if len(lettre_essai) != 1:
                print("Entrez une seule lettre!\n")
                continue

            # Pour chaque essai réussi
            if lettre_essai in self.lettres_restantes and niveau == "2":
                self.lettres_indices[
                    self.lettres_restantes.index(lettre_essai)
                ] = lettre_essai
                self.afficheLettre(lettre_essai)
                # self.lettres_restantes.remove(lettre_essai)
                self.lettres_restantes[self.lettres_restantes.index(lettre_essai)] = ""
                print("Lettres trouvées:", self.lettres_indices, "\n")

            elif lettre_essai in self.lettres_restantes and niveau == "1":
                for i in range(len(self.lettres_restantes)):
                    if self.lettres_restantes[i] == lettre_essai:
                        self.lettres_indices[i] = lettre_essai
                        self.afficheLettre(lettre_essai)
                        self.lettres_restantes[i] = ""
                        print("Lettres trouvées:", self.lettres_indices, "\n")

            # Pour chaque essai raté
            else:
                self.nbEssais -= 1
                self.dessinePendu()

    def dessineBase(self):
        tortue.pendown()
        tortue.begin_fill()
        for i in range(4):
            tortue.forward(80)
            tortue.right(90)
        tortue.end_fill()
        tortue.goto(-25, -50)
        tortue.goto(-25, 200)
        tortue.goto(100, 200)
        tortue.goto(100, 175)
        tortue.penup()
        self.afficheLettres()

    def dessineTete(self):
        tortue.goto(100, 175)
        tortue.pendown()
        tortue.right(180)
        tortue.circle(20)
        tortue.penup()

    def dessineCorps(self):
        tortue.goto(100, 135)
        tortue.pendown()
        tortue.right(270)
        tortue.forward(80)
        tortue.penup()

    def dessineBrasGauche(self):
        tortue.goto(100, 115)
        tortue.pendown()
        tortue.right(60)
        tortue.forward(40)
        tortue.penup()

    def dessineBrasDroit(self):
        tortue.goto(100, 115)
        tortue.pendown()
        tortue.right(240)
        tortue.forward(40)
        tortue.penup()

    def dessineJambeGauche(self):
        tortue.goto(100, 55)
        tortue.pendown()
        tortue.forward(75)
        tortue.penup()

    def dessineJambeDroite(self):
        tortue.goto(100, 55)
        tortue.pendown()
        tortue.right(120)
        tortue.forward(75)
        tortue.penup()

    def dessinePendu(self):
        if self.nbEssais == 5:
            self.dessineTete()
        elif self.nbEssais == 4:
            self.dessineCorps()
        elif self.nbEssais == 3:
            self.dessineBrasGauche()
        elif self.nbEssais == 2:
            self.dessineBrasDroit()
        elif self.nbEssais == 1:
            self.dessineJambeGauche()
        elif self.nbEssais == 0:
            self.dessineJambeDroite()


def main():
    replay = "o"
    while replay == "o":
        resetTortue()
        game = HangmanGame()
        game.dessineBase()
        turtle.listen()
        game.jouer()
        replay = input("Voulez-vous rejouer ? (o/n) ").lower()
        tortue.reset()

    turtle.exitonclick()


if __name__ == "__main__":
    main()
