# importation de la bibliotheque graphique Tkinter
from tkinter import*
# creation d'une fenetre
fenetre=Tk()
fenetre.title('grid')
# creation des widgets
etiquette1=Label(fenetre)
etiquette1.configure(text='Prenom :')
etiquette1.grid(row=1,column=1)
etiquette2=Label(fenetre)
etiquette2.configure(text='Nom :')
etiquette2.grid(row=2,column=1)
saisie1=Entry(fenetre)
saisie1.grid(row=1,column=2)
saisie2=Entry(fenetre)
saisie2.grid(row=2,column=2)
# attente des evenements
fenetre.mainloop()


