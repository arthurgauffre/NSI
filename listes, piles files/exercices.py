"""class Pile :
    def __init__(self):
        self.data = []
    def empile(self,n):
        self.data.append(n)
    
    def depile(self):
        self.data.pop()
    def est_vide(self):
        if len(self.data) == 0 : 
            return True
        else :
            return False
    def __str__(self):      
        s = '|'              
        for k in self.data :
            s = s + str(k) + '|'
        return s
    def __repr__(self):       
        s = '|'              
        for k in self.data :
            s = s + str(k) + '|'
        return s
        
        
pile = Pile()
pile.empile(4)
pile.empile(5)
pile.depile()
"""

class Cellule :
    def __init__(self, contenu, suivante):
        self.contenu = contenu
        self.suivante = suivante
    
class Pile : 
    def __init__(self) : 
        self.data = None

    def est_vide(self)  :
        return self.data == None  
              
    def empile(self, valeur) : 
        self.data = Cellule(valeur, self.data)

    def depile(self) : 
        valeur_retire = self.data.contenu
        self.data = self.data.suivante
        return valeur_retire