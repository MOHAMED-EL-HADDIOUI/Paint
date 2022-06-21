# importation de la bibliotheque graphique Tkinter
from tkinter import*
# creation d'une fenetre
fenetre=Tk()
fenetre.title('prog1')
# creation d'une etiquette
etiquette=Label(fenetre)
etiquette.configure(text='Mon premier programme graphique en Python')
etiquette.pack()
# creation d'une zone de saisie
saisie=Entry(fenetre)
saisie.pack()
# creation d'un bouton
bouton=Button(fenetre)
bouton.configure(text='Cliquer')
bouton.pack()
# attente des evenements
fenetre.mainloop()


