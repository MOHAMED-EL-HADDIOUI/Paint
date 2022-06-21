# importation de la bibliotheque graphique Tkinter
from tkinter import*
# creation d'une fenetre
fenetre=Tk()
fenetre.title('clicpos')
# creation d'un canevas
canevas=Canvas(fenetre)
canevas.configure(width=500,height=500,bg='white')
canevas.pack()
# creation d'une etiquette
etiquette=Label(fenetre)
etiquette.pack()
# gestionnaire d'evenement associe au clic sur le canevas
def clic(event):
    etiquette.configure(text='x='+str(event.x)+' et y='+str(event.y))
canevas.bind('<ButtonPress-1>',clic)
# attente des evenements
fenetre.mainloop()


