from tkinter import *
import tkinter as tk
import numpy as np
import math as m
import matplotlib.pyplot as plt

            ##### Creation de la page du programme #####

fenetre = tk.Tk() #creation de la fenêtre du logiciel
fenetre.geometry("480x360") #Dimension de la fenêtre
fenetre.title("Osmose inverse")

            ##### Creation de liste de temperatures et concentration #####

temperaturesdeg=np.linspace(0,100,100)
temperatureskel=np.linspace(273,373,100)
concentration=np.linspace(0.1,50,100)

            ##### Définition de constante utiles #####

R=8.314 #Constante universelle des gaz parfaits
pi=m.pi
n=(10**-3) #Viscosité dynamique de l'eau
L=0.01 #Longeur d'un pore
nbpores=0.471/(2*10**-9)**2 #Nombres de pores pour un cylindre de rayon 7.5 cm et de hauteur 10 cm

            ##### initialisation des variables pour utilisation GLOBAL #####
i=0
c=0
t=0
            ##### Fonctions utilisées dans le programme #####

def osmose(i,c,t):
    """revoie la pression osmotique p à partir du
nombre i d'ions dissociés et c la concentration du
soluté de la solution saline."""
    R=8.314
    T=t+273
    DeltaC=c/(100*10**-3)
    p=R*T*DeltaC*i
    return (p*10**-5,"bar")

def listetemp():
    valeurs_osmose=[]
    for k in range(len(temperaturesdeg)):
        temporaire=osmose(i,c,k)
        valeurs_osmose.append(temporaire)
    return(valeurs_osmose)

def graphtemp():
    """Renvoie le graphique de la pression osmotique en fonction de la concentration
a Temperature fixée"""
    liste=listetemp()
    Xe=[]
    for k in range(len(liste)):
        temp=liste[k]
        Xe.append(temp[0])
    Ye=temperatureskel
    plt.plot(Xe,Ye) #Création du graphique
    plt.savefig("graphique.png",dpi=50) #Sauvegarde du graphique
    plt.show()

def debit(p):
    """Renvoie le debit d'eau a travers une membrane de longeur L=1cm et de pore de
dimension 10E-5 m"""
    dp=abs(p-1)*10**5 #difference de pression par rapport a l'air (1 Bar)
    deb=(pi*(10**-9)**4)*dp/(8*n*L) #Debit pour un ecoulement de Poiseuille
    debtot=deb*nbpores #debit total
    print("Débit :",debtot*3600*1000,"L/h")
    return(debtot)

            ##### Fonctions calculs des boutons #####

def calcul():
    R=8.314
    T=t+273
    DeltaC=c/(100*10**-3)
    p=R*T*DeltaC*i
    print("Préssion :",p*10**-5,"bar")
    return (p*10**-5,"bar")

def calculdebit():
    p,txt=osmose(i,c,t)
    debit(p)
    return(p)

            ##### Recuperation des valeurs #####

def recupvaleurs():
    """Récupère les 3 valeurs saisie dans le logiciel"""
    global i
    global c
    global t
    i=float(reci.get())
    c=float(recc.get())
    t=float(rect.get())
    return(i,c,t)

reci = tk.Entry(fenetre, width=40)
recc = tk.Entry(fenetre, width=40)
rect = tk.Entry(fenetre, width=40)

photo = tk.PhotoImage(file="graphique préssion osmotique.png")

canvas = Canvas(fenetre,width=350, height=250)
canvas.create_image(0, 0, anchor=NW, image=photo)


            ##### Bouton #####

btnvalid = tk.Button(fenetre, height=1, width=11, text="Valider valeurs", command=recupvaleurs) 
btncalcul = tk.Button(fenetre, height=1, width=10, text="Pression", command=calcul)
btndebit = tk.Button(fenetre, height=1, width=10, text="Debit", command=calculdebit)
btngraph = tk.Button(fenetre,height=1, width=32, text="Afficher graphique à température variable", command=graphtemp)

            ##### Texte indicatif #####

labeli = Label(fenetre, text="Valeur de i", bg="green")
labelc = Label(fenetre, text="Valeur de c(mol.L-1)", bg="yellow")
labelt = Label(fenetre, text="Valeur de T(°c)", bg="red")

            ##### Mise en page (technique grid) #####

labeli.grid(column=0,row=0)
labelc.grid(column=0,row=1)
labelt.grid(column=0,row=2)
reci.grid(column=1,row=0)
recc.grid(column=1,row=1)
rect.grid(column=1,row=2)
btncalcul.grid(column=2,row=1)
btnvalid.grid(column=2,row=0)
btndebit.grid(column=2,row=2)
btngraph.grid(column=1,row=4)
canvas.grid(column=0,row=5,columnspan=3,rowspan=6)

fenetre.mainloop()
