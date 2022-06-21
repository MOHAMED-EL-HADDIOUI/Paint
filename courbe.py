# importation de la bibliotheque graphique Tkinter
from tkinter import*
# creation d'une fenetre
fenetre=Tk()
fenetre.title('courbe')
# creation d'un canevas
canevas=Canvas(fenetre)
canevas.configure(width=500,height=500,bg='white')
canevas.pack()
# initialisation des variables de position
x='vide'
y='vide'
# gestionnaire d'evenement associe au mouvement sur le canevas
def mouvement(event):
    global x,y
    if(x!='vide'):
        canevas.create_line(x,y,event.x,event.y)
    x=event.x
    y=event.y
canevas.bind('<Motion>',mouvement)
# attente des evenements
fenetre.mainloop()
