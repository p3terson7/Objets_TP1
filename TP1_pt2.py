from turtle import *

tortue = Turtle()
tortue.speed(1)
tortue.pensize(3)
tortue.penup()
tortue.color("black")
tortue.goto(-50, -50) #Position initiale de la tortue

nbEssais = 6
estDebutant = None


def dessineBase():
    tortue.pendown()
    tortue.begin_fill()
    for i in range(4):
        tortue.forward(100)
        tortue.right(90)
    tortue.end_fill()
    tortue.goto(-25, -50)
    tortue.goto(-25, 200)
    tortue.goto(100, 200)
    tortue.goto(100, 175)



dessineBase()
def setDifficulte():
    choix = int(input("Entrez 1 pour le mode débutant ou 2 pour le mode avancé: "))
    if choix == 1:
        estDebutant = true
    elif choix == 2:
        estDebutant = false
