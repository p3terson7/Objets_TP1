from turtle import *
import nltk

# Bovary
fichier = open("bovary.txt", encoding="utf-8")
bovary_string = fichier.read()
bovary_liste = nltk.word_tokenize(bovary_string)
bovary_texte = nltk.Text(bovary_liste)

# Setup turtle
tortue = Turtle()
tortue.speed(3)
tortue.pensize(3)
tortue.penup()
tortue.color("black")
tortue.goto(-50, -50)  # Position initiale


# Variables de jeu
nbEssais = 6
jeuEnCours = False






def dessineBase():
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


def dessineTete():
    tortue.goto(100, 175)
    tortue.pendown()
    tortue.right(180)
    tortue.circle(20)
    tortue.penup()

def dessineCorps():
    tortue.goto(100, 135)
    tortue.pendown()
    tortue.right(270)
    tortue.forward(80)
    tortue.penup()

def dessineBrasGauche():
    tortue.goto(100, 115)
    tortue.pendown()
    tortue.right(60)
    tortue.forward(40)
    tortue.penup()

def dessineBrasDroit():
    tortue.goto(100, 115)
    tortue.pendown()
    tortue.right(240)
    tortue.forward(40)
    tortue.penup()

def dessineJambeGauche():
    tortue.goto(100, 55)
    tortue.pendown()
    tortue.forward(75)
    tortue.penup()

def dessineJambeDroite():
    tortue.goto(100, 55)
    tortue.pendown()
    tortue.right(120)
    tortue.forward(75)
    tortue.penup()


dessineBase()
dessineTete()
dessineCorps()
dessineBrasGauche()
dessineBrasDroit()
dessineJambeGauche()
dessineJambeDroite()
