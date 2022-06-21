# importation de la bibliotheque graphique Tkinter
from tkinter import*
# creation d'une fenetre
fenetre=Tk()
fenetre.title('frame')
# creation d'un cadre
cadre=Frame(fenetre)
cadre.configure(bd=2,relief='groove')
cadre.grid(padx=15,pady=15)
# creation des widgets du cadre
saisie=Entry(cadre)
saisie.grid(row=1,column=1,padx=5,pady=5)
bouton=Button(cadre)
bouton.configure(text='bouton')
bouton.grid(row=2,column=1,padx=5,pady=5)
# attente des evenements
fenetre.mainloop()
