# importation de la bibliotheque graphique Tkinter
from tkinter import*
# creation d'une fenetre
fenetre=Tk()
fenetre.title('prog8')
# creation d'une variable Tkinter
couleur=IntVar()
couleur.set(0) # initialisation de la variable couleur
# creation de la palette de couleurs
palette=['#000000','#800000','#008000','#808000','#000080','#800080','#008080','#808080',
         '#c0c0c0','#ff0000','#00ff00','#ffff00','#0000ff','#ff00ff','#00ffff','#ffffff']
# creation des boutons radio
r={}
for i in range(0,16):
    r[i]=Radiobutton(fenetre)
    r[i].configure(variable=couleur,value=i,bg=palette[i])
    r[i].pack()
# attente des evenements
fenetre.mainloop()
