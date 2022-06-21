# importation de la bibliotheque graphique Tkinter
from tkinter import*
# creation d'une fenetre
fenetre=Tk()
fenetre.title('prog4')
# creation d'une variable Tkinter
calcul=StringVar()
# creation d'une zone de saisie
saisie=Entry(fenetre)
saisie.configure(textvariable=calcul)
saisie.pack()
# creation d'une etiquette
etiquette=Label(fenetre)
etiquette.pack()
# creation d'un bouton
bouton=Button(fenetre)
bouton.configure(text='Calculer')
bouton.pack()
# gestionnaire d'evenement associe au clic sur le bouton
def clic(event):
    etiquette.configure(text=str(eval(calcul.get())))
bouton.bind('<ButtonPress-1>',clic)
# attente des evenements
fenetre.mainloop()


