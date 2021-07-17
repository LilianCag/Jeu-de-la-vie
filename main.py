# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = #
# Author       : Lilian Cagnon (@Doxed#5900 / Discord)
# Project name : Life Game
# File name    : main.py
# Last update  : 17-July-2021
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = #

# Imports
from tkinter import *
import random

# Variables
c = 20
largeur = 50
hauteur = 30 
generation = 0

cell = [[0 for row in range(hauteur)] for col in range(largeur)]
etat = [[0 for row in range(hauteur)] for col in range(largeur)]
temp = [[0 for row in range(hauteur)] for col in range(largeur)]

# Boucle
def task():
    calcul()
    affichage()
    app.after(50, task)

# Initialisation randomisée
def init():
    generation = 1
    for x in range(largeur):
        for y in range(hauteur):
            r = random.uniform(0, 1)
            if r > 0.5:
                etat[x][y] = 1
            else:
                etat[x][y] = 0
            temp[x][y] = 0

# Initialisation vaisseaux
def gnrt_vaisseaux():
    for x in range(largeur):
        for y in range(hauteur):
            etat[x][y] = 0
            temp[x][y] = 0
    etat[7][24] = 1
    etat[7][25] = 1
    etat[8][24] = 1
    etat[8][25] = 1
    etat[17][23] = 1
    etat[17][24] = 1
    etat[17][25] = 1
    etat[18][26] = 1
    etat[19][27] = 1
    etat[20][27] = 1
    etat[18][22] = 1
    etat[19][21] = 1
    etat[20][21] = 1
    etat[21][24] = 1
    etat[22][26] = 1
    etat[22][22] = 1
    etat[23][23] = 1
    etat[23][24] = 1
    etat[23][25] = 1
    etat[24][24] = 1
    etat[29][24] = 1
    etat[27][25] = 1
    etat[28][25] = 1
    etat[27][26] = 1
    etat[28][26] = 1
    etat[27][27] = 1
    etat[28][27] = 1
    etat[29][28] = 1
    etat[31][28] = 1
    etat[31][29] = 1
    etat[31][23] = 1
    etat[31][24] = 1
    etat[41][27] = 1
    etat[41][26] = 1
    etat[42][27] = 1
    etat[42][26] = 1

# Calcul du nombre de voisins 
def nbvoisins_bords(a,b):
    nbvoisins = 0
    if etat[(a-1)][(b+1)%hauteur] == 1:
        nbvoisins += 1
    if etat[a][(b+1)%hauteur] == 1:
        nbvoisins += 1
    if etat[(a+1)%largeur][(b+1)%hauteur] == 1:
        nbvoisins += 1
    if etat[(a-1)%largeur][b] == 1:
        nbvoisins += 1
    if etat[(a+1)%largeur][b] == 1:
        nbvoisins += 1
    if etat[(a-1)%largeur][(b-1)%hauteur] == 1:
        nbvoisins += 1
    if etat[a][(b-1)%hauteur] == 1:
        nbvoisins += 1
    if etat[(a+1)%largeur][(b-1)%hauteur] == 1:
        nbvoisins += 1
    return nbvoisins

# Calcul du nombre de voisins 
def nbvoisins(a,b):
    nbvoisins = 0
    for x in range (a-1, a+2):
        for y in range(b-1, b+2):
            if (x >= 0 and x < largeur) and (y >= 0 and y < hauteur):
                if(etat[x][y] == 1):
                    nbvoisins += 1
    return nbvoisins-etat[a][b]

# Calcul pour déterminer si la cellule doit rester morte/en vie
def calcul():
    for x in range (largeur):
        for y in range(hauteur):
            nb =  nbvoisins(x,y)
            # mort de solitude (voisins < 2)
            if etat[x][y] == 1 and nb < 2:
                temp[x][y] = 0
            # reste en vie (voisins = 2/3)
            if etat[x][y] == 1 and (nb == 2 or nb == 3):
                temp[x][y] = 1
            # mort par surpopulation (voisins > 3)
            if etat[x][y] == 1 and nb > 3:
                temp[x][y] = 0
            # naissance (voisins = 3)
            if etat[x][y] == 0 and nb == 3:
                temp[x][y] = 1
    for x in range(largeur):
        for y in range(hauteur):
            etat[x][y] = temp[x][y]

# Affichage du tableau
def affichage():
    for x in range(largeur):
        for y in range(hauteur):
            if etat[x][y] == 0:
                couleur = "white"
            else:   
                couleur = "black"
            if etat[x][y] == 2:
                couleur = "red"
            canvas.itemconfig(cell[x][y], fill = couleur)


# Programme principal
app = Tk()
app.title('Jeu de la vie')
canvas = Canvas(app, width = c*largeur, height = c*hauteur, bg = 'white')
for x in range(largeur):
    for y in range(hauteur):
            cell[x][y] = canvas.create_rectangle((x*c, y*c, (x+1)*c, (y+1)*c), outline = 'gray', fill='white')
menu = Menu(app)
menufichier = Menu(menu,tearoff=0)
menu.add_cascade(label="Options", menu=menufichier)
menufichier.add_command(label="Redémarrer", command=init)
menufichier.add_command(label="Vaisseaux", command=gnrt_vaisseaux)
menufichier.add_command(label="Quitter", command=app.destroy)
app.config(menu=menu)
init()
task()
canvas.pack()
app.mainloop()