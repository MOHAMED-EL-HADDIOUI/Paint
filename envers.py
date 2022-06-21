# importation de la bibliotheque graphique Tkinter
from tkinter import*
# creation d'une fenetre
fenetre=Tk()
fenetre.title('envers')
# creation d'une variable Tkinter
texte=StringVar()
# creation d'une zone de saisie
saisie=Entry(fenetre)
saisie.configure(textvariable=texte)
saisie.pack()
# creation d'un bouton
bouton=Button(fenetre)
bouton.configure(text='Inverser')
bouton.pack()
# gestionnaire d'evenement associe au clic sur le bouton
def clic(event):
    endroit=texte.get()
    envers=endroit[::-1]
    texte.set(envers)
bouton.bind('<ButtonPress-1>',clic)
# attente des evenements
fenetre.mainloop()


