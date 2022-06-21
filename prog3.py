# importation de la bibliotheque graphique Tkinter
from tkinter import*
# creation d'une fenetre
fenetre=Tk()
fenetre.title('prog3')
# creation d'une etiquette
etiquette=Label(fenetre)
etiquette.configure(text='nombre de clics : 0')
etiquette.pack()
# creation d'un bouton
bouton=Button(fenetre)
bouton.configure(text='Cliquer')
bouton.pack()
# creation de la variable nombre de clics
nbclics=0
# gestionnaire d'evenement associe au clic sur le bouton
def clic(event):
    global nbclics
    nbclics=nbclics+1
    etiquette.configure(text='nombre de clics : '+str(nbclics))
bouton.bind('<ButtonPress-1>',clic)
# attente des evenements
fenetre.mainloop()


