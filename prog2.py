# importation de la bibliotheque graphique Tkinter
from tkinter import*
# creation d'une fenetre
fenetre=Tk()
fenetre.title('prog2')
# creation des touches du pave numerique
bouton1=Button(fenetre)
bouton1.configure(text='1',width='3',height='2')
bouton1.grid(row=3,column=1)
bouton2=Button(fenetre)
bouton2.configure(text='2',width='3',height='2')
bouton2.grid(row=3,column=2)
bouton3=Button(fenetre)
bouton3.configure(text='3',width='3',height='2')
bouton3.grid(row=3,column=3)
bouton4=Button(fenetre)
bouton4.configure(text='4',width='3',height='2')
bouton4.grid(row=2,column=1)
bouton5=Button(fenetre)
bouton5.configure(text='5',width='3',height='2')
bouton5.grid(row=2,column=2)
bouton6=Button(fenetre)
bouton6.configure(text='6',width='3',height='2')
bouton6.grid(row=2,column=3)
bouton7=Button(fenetre)
bouton7.configure(text='7',width='3',height='2')
bouton7.grid(row=1,column=1)
bouton8=Button(fenetre)
bouton8.configure(text='8',width='3',height='2')
bouton8.grid(row=1,column=2)
bouton9=Button(fenetre)
bouton9.configure(text='9',width='3',height='2')
bouton9.grid(row=1,column=3)
# attente des evenements
fenetre.mainloop()


