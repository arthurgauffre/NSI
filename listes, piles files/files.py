"""
class File:
    def __init__(self):
        self.data = []
    def est_vide(self) :
        if len(self.data) == 0 : 
            return True 
        else :
            return False
    def enfile(self, new_data) :
        self.data.append(new_data)
    def defile(self) :
        return self.data.pop(0)
    
    def __str__(self) -> str :
        s = '|'
        for k in self.data :
            s += str(k) + '|'
        return s
"""
# création d'une file avec deux piles 

class Pile:
    def __init__(self):
        self.data = []

    def est_vide(self):
        return len(self.data) == 0 


    def empile(self,x):
        self.data.append(x)

    def depile(self):
        if self.est_vide() == True :
            raise IndexError('Vous avez essayé de dépiler une pile vide !')
        else :
            return self.data.pop() 

class File:
    def __init__(self):
        self.entree = Pile()
        self.sortie = Pile()
    
    def enfile(self, new_file):
        self.entree.empile(new_file)
    
    def defile(self):
        if self.est_vide():
            raise IndexError("UwU File vide OwO")
        else:
            if not self.sortie.est_vide():
                x = self.sortie.depile()
                return x
            else:
                while not self.entree.est_vide:
                    self.entree.empile(self.entree.depile())
                x = self.sortie.depile()
                return x