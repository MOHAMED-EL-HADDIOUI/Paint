# importation de la bibliotheque graphique Tkinter
from tkinter import*
# creation d'une fenetre
fenetre=Tk()
fenetre.title('choix')
# creation d'une variable Tkinter
choix=IntVar()
choix.set(1) # initialisation de la variable choix
# creation de cases a cocher
case1=Radiobutton(fenetre)
case1.configure(text='choix 1',variable=choix,value=1)
case1.pack()
case2=Radiobutton(fenetre)
case2.configure(text='choix 2',variable=choix,value=2)
case2.pack()
case3=Radiobutton(fenetre)
case3.configure(text='choix 3',variable=choix,value=3)
case3.pack()
# attente des evenements
fenetre.mainloop()


