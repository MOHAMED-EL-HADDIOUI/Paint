# importation de la bibliotheque graphique Tkinter
from tkinter import*
# creation d'une fenetre
fenetre=Tk()
fenetre.title('prog7')
# creation d'un canevas
canevas=Canvas(fenetre)
canevas.configure(width=500,height=500,bg='white')
canevas.pack()
# initialisation des variables de position
x='vide'
y='vide'
# initialisation de l'etat du bouton gauche de la souris
etatboutonsouris='haut'
# gestionnaire d'evenement associe au clic sur le canevas
def clic(event):
    global etatboutonsouris,x,y
    etatboutonsouris='bas'
    x=event.x
    y=event.y
canevas.bind('<ButtonPress-1>',clic)
# gestionnaire d'evenement associe au declic sur le canevas
def declic(event):
    global etatboutonsouris
    etatboutonsouris='haut'
canevas.bind('<ButtonRelease-1>',declic)
# gestionnaire d'evenement associe au mouvement sur le canevas
def mouvement(event):
    global etatboutonsouris,x,y
    if (etatboutonsouris=='bas'):
        canevas.create_line(x,y,event.x,event.y)
    x=event.x
    y=event.y
canevas.bind('<Motion>',mouvement)
# attente des evenements
fenetre.mainloop()
