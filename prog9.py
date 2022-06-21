# importation de la bibliotheque graphique Tkinter
from tkinter import*
# creation d'une fenetre
fenetre=Tk()
fenetre.title('Logiciel de dessin')
# creation des differents cadres
zonedessin=LabelFrame(fenetre)
zonedessin.configure(text='zone de dessin',bd=2,relief='groove')
zonedessin.grid(row=1,rowspan=3,column=1,padx=10,pady=10)
selectioncouleur=LabelFrame(fenetre)
selectioncouleur.configure(text='selection de la couleur du trait',bd=2,relief='groove')
selectioncouleur.grid(row=1,column=2,padx=10,pady=10)
selectionepaisseur=LabelFrame(fenetre)
selectionepaisseur.configure(text='selection de l\'epaisseur du trait',bd=2,relief='groove')
selectionepaisseur.grid(row=2,column=2,padx=10,pady=10)
selectionstyle=LabelFrame(fenetre)
selectionstyle.configure(text='selection du style de trait')
selectionstyle.grid(row=3,column=2,padx=10,pady=10)
# creation des widgets du cadre zonedessin
canevas=Canvas(zonedessin)
canevas.configure(width=500,height=500,bg='white')
canevas.pack()
# creation des widgets du cadre selectioncouleur
couleur=IntVar()
couleur.set(0) 
palette=['#000000','#800000','#008000','#808000','#000080','#800080','#008080','#808080',
         '#c0c0c0','#ff0000','#00ff00','#ffff00','#0000ff','#ff00ff','#00ffff','#ffffff']
rcouleur={}
for i in range(0,16):
    rcouleur[i]=Radiobutton(selectioncouleur)
    rcouleur[i].configure(variable=couleur,value=i,bg=palette[i])
    rcouleur[i].grid(row=1,column=i)
# creation des widgets du cadre selectionepaisseur
epaisseur=IntVar()
epaisseur.set(1)
repaisseur={}
for i in range(1,7):
    repaisseur[i]=Radiobutton(selectionepaisseur)
    repaisseur[i].configure(variable=epaisseur,value=i,text=str(i))
    repaisseur[i].grid(row=1,column=i)
# creation des widgets du cadre selectionstyle
style=StringVar()
style.set('droite')
rstyle1=Radiobutton(selectionstyle)
rstyle1.configure(variable=style,value='droite',text='droite')
rstyle1.grid(row=1,column=1)
rstyle2=Radiobutton(selectionstyle)
rstyle2.configure(variable=style,value='courbe',text='courbe')
rstyle2.grid(row=1,column=2)
# initialisation des variables de position
x='vide'
y='vide'
x1='vide'
y1='vide'
x2='vide'
y2='vide'
# initialisation de l'etat du bouton gauche de la souris
etatboutonsouris='haut'
# gestionnaire d'evenement associe au clic sur le canevas
def clic(event):
    global etatboutonsouris,x1,y1
    etatboutonsouris='bas'
    x1=event.x
    y1=event.y
canevas.bind('<ButtonPress-1>',clic)
# gestionnaire d'evenement associe au declic sur le canevas
def declic(event):
    global etatboutonsouris,x1,y1,x2,y2
    etatboutonsouris='haut'
    x2=event.x
    y2=event.y
    if (style.get()=='droite'):
        canevas.create_line(x1,y1,x2,y2,fill=palette[couleur.get()],width=epaisseur.get())
canevas.bind('<ButtonRelease-1>',declic)
# gestionnaire d'evenement associe au mouvement sur le canevas
def mouvement(event):
    global etatboutonsouris,x,y
    if (style.get()=='courbe' and etatboutonsouris=='bas'):
        canevas.create_line(x,y,event.x,event.y,fill=palette[couleur.get()],width=epaisseur.get())
    x=event.x
    y=event.y
canevas.bind('<Motion>',mouvement)
# attente des evenements
fenetre.mainloop()
