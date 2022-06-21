# importation de la bibliotheque graphique Tkinter
from tkinter import*
# creation d'une fenetre
fenetre=Tk()
fenetre.title('prog6')
# creation d'un canevas
canevas=Canvas(fenetre)
canevas.configure(width=500,height=500,bg='white')
canevas.pack()
# initialisation des variables de position
x1='vide'
y1='vide'
x2='vide'
y2='vide'
# gestionnaire d'evenement associe au clic sur le canevas
def clic(event):
    global x1,y1
    x1=event.x
    y1=event.y
canevas.bind('<ButtonPress-1>',clic)
# gestionnaire d'evenement associe au declic sur le canevas
def declic(event):
    global x1,y1,x2,y2
    x2=event.x
    y2=event.y
    canevas.create_line(x1,y1,x2,y2)
canevas.bind('<ButtonRelease-1>',declic)
# attente des evenements
fenetre.mainloop()
