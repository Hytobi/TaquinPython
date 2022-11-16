import tkinter

import string
from random import randint

def initialisationImages():
    '''Fonction qui cree la liste des images
       Argument : None
       Retour : images --- list --- liste d'image'''
    images=[]
    images.append("./alphabet/rien.gif")
    for i in string.ascii_lowercase :
        img = "./alphabet/"+i+".gif"
        images.append(img)
    return images

class VueTaquin :

    '''Classe qui définit et met en place une interface graphique.
    On y affiche les image de 5x5 lettres, qui change à chaque clic.
    '''
    
    def __init__(self,dim=4):
        '''Méthode qui initialise la classe, elle construit l'interface graphique et la lance.
           Argument : self --- class --- VueAlphabet4
           Retour : None'''
        
        fenetre = tkinter.Tk()
        fenetre.title("Taquin")

        self.__images = initialisationImages()
        self.__dim = dim

        self.__lesIndices=[]
        self.__Images = []
        self.__tout = []
        a=0
        for j in range(dim):
            self.__btns = []
            for i in range(dim) :
                if j == dim-1 and i == dim-1:
                    self.__lesIndices.append(0)
        
                    img = tkinter.PhotoImage(file=str(self.__images[self.__lesIndices[i+a]]))

                    self.__Images.append(img)
                else:
                    self.__lesIndices.append(i+1+a)
        
                    img = tkinter.PhotoImage(file=str(self.__images[self.__lesIndices[i+a]]))
                
                    self.__Images.append(img)
    
                self.__btns.append(tkinter.Button(fenetre, image=self.__Images[i+a]))
                self.__btns[i]["command"] = self.ctrl_choisit_case()
                self.__btns[i].grid(row=j,column=i)

                
            self.__tout.append(self.__btns)
            a+=dim
        print(self.__lesIndices)
        print(self.__Images)
        print(self.__tout )
        print(self.__btns)

        
        
        btn_recommencer = tkinter.Button(fenetre,text="Recommencer",command =self.reboot)
        btn_recommencer.grid(row=5,column=1)

        btn_quitter = tkinter.Button(fenetre,text="Au revoir",command = fenetre.destroy)
        btn_quitter.grid(row=5,column=dim-2)
        
        
        fenetre.mainloop()

    def ctrl_choisit_case(self):
        '''Methode qui gère l’événement l’utilisateur a cliqué sur une image'''
        x = randint(0,15)
        self.__lesIndices[x] = self.__lesIndices[15]
        self.__btns[x]["image"] = self.__Images[self.__lesIndices[x]]
        


        
    def reboot(self):
        '''Méthode qui change les lettres aléatoirement.
           Argument : self --- class --- VueAlphabet3
           Retour : None'''
        a=0
        for j in range(self.__dim):
            i=0
            while i!=self.__dim:
                image = randint(0,len(string.ascii_lowercase)-1)

                if image not in self.__lesIndices :
                    self.__lesIndices[i+a]=image
                    self.__Images[i+a] = tkinter.PhotoImage(file=str(self.__images[self.__lesIndices[i+a]]))
                    self.__tout[j][i].config(image=self.__Images[i+a])
                    i+=1

            a+=self.__dim


                

if __name__ == '__main__' :
    appli = VueTaquin()

