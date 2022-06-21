# importation de la bibliotheque graphique Tkinter
from tkinter import*
# creation d'une fenetre
fenetre=Tk()
fenetre.title('prog5')
# creation d'un canevas
canevas=Canvas(fenetre)
canevas.configure(width=500,height=500,bg='white')
canevas.pack()
# creation d'une etiquette
etiquette=Label(fenetre)
etiquette.pack()
# gestionnaire d'evenement associe au mouvement sur le canevas
def mouvement(event):
    etiquette.configure(text='x='+str(event.x)+' et y='+str(event.y))
canevas.bind('<Motion>',mouvement)
# attente des evenements
fenetre.mainloop()


