# importation de la bibliotheque graphique Tkinter
from tkinter import*
# creation d'une fenetre
fenetre=Tk()
fenetre.title('jour-nuit')
# creation des boutons
boutonjour=Button(fenetre)
boutonjour.configure(text='Jour')
boutonjour.pack()
boutonnuit=Button(fenetre)
boutonnuit.configure(text='Nuit')
boutonnuit.pack()
# gestionnaire d'evenement associe au clic sur boutonjour
def clicjour(event):
    fenetre.configure(bg='yellow')
boutonjour.bind('<ButtonPress-1>',clicjour)
# gestionnaire d'evenement associe au clic sur boutonnuit
def clicnuit(event):
    fenetre.configure(bg='black')
boutonnuit.bind('<ButtonPress-1>',clicnuit)
# attente des evenements
fenetre.mainloop()


