#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# essai_couleur_hasard.py
#
# inspiré du script animation.py de Fabrice Sincère



from tkinter import *
import random

def couleur_alea() :
	""" crée des couleur en hexadecimal au hasard"""
	# à commenter
	liste_hexa = [ '0' , '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , 'A' , 'B' , 'C' , 'D' , 'E' , 'F' ]
	couleur ='#'

	# à commenter 
	for i in range(6) :
		couleur = couleur + liste_hexa[random.randint(0, 15)] 


	# à commenter
	return couleur


def Cercle():
	""" Dessine un cercle de centre (x,y) et de rayon r
		Fonction récursive (qui s'appelle elle même tant que le booleen Arret est vrai)
	"""
	global time

	# à commenter
	x = random.randint(0,Largeur)
	y = random.randint(0,Hauteur)
	r = random.randint(10,Rayon)


	# à commenter
	Canevas.create_oval(x-r, y-r, x+r, y+r, outline='black' ,  fill=  couleur_alea() )

	#Tant que ce test est vrai la fonction start() est appelée
		# appel de la fonction start() après une pause de 100 millisecondes

	Mafenetre.after(time,start)


def Carre():
	""" Dessine un cercle de centre (x,y) et de rayon r
		Fonction récursive (qui s'appelle elle même tant que le booleen Arret est vrai)
	"""

	global Arret
	global time

	# à commenter
	x = random.randint(0,Largeur)
	y = random.randint(0,Hauteur)
	r = random.randint(10,Rayon)

	# à commenter
	Canevas.create_rectangle(x-r, y-r, x+r, y+r, outline='black' ,  fill=  couleur_alea() )
	# appel de la fonction start() après une pause de 100 millisecondes
	Mafenetre.after(time,start)


def Arreter():
	""" Arrêt de l'animation """
	global Arret
	Arret = True



def Effacer_canevas():
	Canevas.delete(ALL)


def start():
	global Arret
	if Arret == False:
		forme = random.randint(0,1)
		if forme == 1:
			Carre()
		else:
			Cercle()
	else:
		Arret = False

def color_background():
	Mafenetre.configure(bg=entree_color.get())
	pass


def time_set():
	global time
	time = int(entree_time.get())

#***********************************
#       Programme principal        *
#***********************************


#Initialisation des variables
Arret = False
Largeur = 500
Hauteur = 350
Rayon = 50
time = 100


# Création de la fenêtre principale (main window)
Mafenetre = Tk()
Mafenetre.title('couleurs au hasard')


# Création d'un widget Canvas
Canevas = Canvas(Mafenetre, width = Largeur, height =Hauteur, bg ='white')
Canevas.pack(padx =5, pady =5)


# Création d'un widget Button (bouton qui permet de créer les cercles)
BoutonStart = Button(Mafenetre, text ='Start', command = start)
BoutonStart.pack(side = LEFT, padx = 10, pady = 10)




# Création d'un widget Button (bouton qui arrete les création de cercles ou de carrés)
BoutonArreter = Button(Mafenetre, text ='Arrêter', command = Arreter)
BoutonArreter.pack(side = LEFT, padx = 5, pady = 5)


# Création d'un widget Button (bouton qui permet d'effacer le canevas)
BoutonEffacer = Button(Mafenetre, text ='Effacer', command = Effacer_canevas)
BoutonEffacer.pack(side = LEFT, padx = 5, pady = 5)

entree_color=Entry(Mafenetre)
entree_color.pack(side = LEFT, padx =5, pady =5)

Boutoncolor = Button(Mafenetre, text ='Confirmer couleur (Format Hexadecimal)', command = color_background)
Boutoncolor.pack(side = LEFT, padx = 5, pady = 5)

entree_time=Entry(Mafenetre)
entree_time.pack(side = LEFT, padx =5, pady =5)

Boutontime = Button(Mafenetre, text ="Confirmer le temps d'actualisation (s)", command = time_set)
Boutontime.pack(side = LEFT, padx = 5, pady = 5)



# Création d'un widget Button (bouton Quitter)
BoutonQuitter = Button(Mafenetre, text ='Quitter', command = Mafenetre.destroy)
BoutonQuitter.pack(side = LEFT, padx = 5, pady = 5)

input()

Mafenetre.mainloop()
