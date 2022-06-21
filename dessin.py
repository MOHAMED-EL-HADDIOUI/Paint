# importation de la bibliotheque graphique Tkinter
from tkinter import*
# creation d'une fenetre
fenetre=Tk()
fenetre.title('dessin')
# creation d'un canevas
canevas=Canvas(fenetre)
canevas.configure(width=500,height=500,bg='white')
canevas.pack()
# dessin dans le canevas
canevas.create_line(100,0,400,500,fill='red',width=3)
canevas.create_rectangle(400,100,300,200,outline='blue',width=2)
canevas.create_oval(100,300,200,400,outline='green',width=2)
# attente des evenements
fenetre.mainloop()
