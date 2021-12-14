from pygame.locals import *
from random import randint

largeur = 1500
hauteur = 1000
color = (255,0,0)

class Balle :
    
    def __init__(self) :
        self.x = randint(0,largeur)
        self.y = randint(0,hauteur)
        self.couleur = (randint(0,255), randint(0,255), randint(0,255))
        self.dx = randint(-5,5)
        self.dy = randint(-5,5)
        self.taille = 5
    
    def split(self) :
        ma_balle.taille = ma_balle.taille/2
    
    def collision(self) :
        
        if ((ma_balle.x-self.x)**2 + (ma_balle.y-self.y)**2)**0.5 <= (ma_balle.taille + self.taille) :
           all_balls.remove(self)
           ma_balle.taille += 0.7
           
    def ressources(self) :
        self.taille= 5
        self.x = randint(0,largeur)
        self.y = randint(0,hauteur)
    
    def bouge(self) :
        self.dessine()
        
        self.x += self.dx
        self.y += self.dy
        if self.x > largeur - self.taille or self.x < self.taille :
            self.dx = -self.dx
        if self.y > hauteur - self.taille or self.y < self.taille :
            self.dy = -self.dy
        
    def dessine(self) :
        pygame.draw.circle(fenetre,self.couleur,(self.x,self.y),self.taille)
    
    
class Refuge : 
    
    def __init__(self) :
        self.abcisse = randint(50,largeur-50)
        self.ordonne = randint(50,hauteur-50)
        self.color = (0,255,0)
        self.grosseur = 50
    
    def apparition(self):
        pygame.draw.circle(fenetre,self.color,(self.abcisse,self.ordonne),self.grosseur)
"""split est la division en 2 de la balle"""


class Split :
    
    def __init__(self):
        self.x = ma_balle.x + ma_balle.taille 
        self.y = ma_balle.y
        self.couleur = ma_balle.couleur
        self.dx = ma_balle.dx
        self.dy = ma_balle.dy
        self.taille = ma_balle.taille/2 
    
    def dessin(self) :
        pygame.draw.circle(fenetre,self.couleur,(self.x,self.y),self.taille)
    
    def setter(self):
        for j in mon_split : 
            self. x += i.taille


refuge = [Refuge() for i in range(int(input("nombre de refuges : ")))]

all_balls = [Balle() for k in range(int(input("nombre de balles : ")))]

mon_split = []

def division() :
    for k in range(1) :
        new_balle = Split()
        mon_split.append(new_balle)
    if len(mon_split) >= 2 :
        new_balle.setter() 

ma_balle = Balle()
ma_balle.taille = 10
ma_balle.x = largeur/2
ma_balle.y = hauteur/2
ma_balle.dx = 6
ma_balle.dy = 6


pygame.display.init()
icon_32x32 = pygame.image.load("/home/eleve/Images/ec16f7526d03d523429bc7abcebdb49a.png")



pygame.display.set_icon(icon_32x32)
fenetre = pygame.display.set_mode((largeur, hauteur))
fenetre.fill([255,255,255])


while True :
    fenetre.fill([255,255,255])
    
    for balle in all_balls:
        balle.dessine()
        balle.collision()

    pygame.draw.circle(fenetre,color,(ma_balle.x,ma_balle.y),ma_balle.taille)

    for cachette in refuge :
        cachette.apparition()
        
    for i in mon_split:   
        i.dessin()

    pygame.display.update()
    
    for event in pygame.event.get():   
      if event.type == KEYDOWN:
        if event.key == K_RIGHT:
            pygame.key.set_repeat(40)
            if ma_balle.x < largeur - ma_balle.taille :
                ma_balle.x += ma_balle.dx
                if len(mon_split) >= 1 :                    
                    for k in mon_split :
                        k.x += k.dx
        if event.key == K_LEFT:
            pygame.key.set_repeat(40)
            if ma_balle.x > 0 + ma_balle.taille :    
                ma_balle.x -= ma_balle.dx
                if len(mon_split) >= 1 :                   
                    for k in mon_split :
                        k.x -= k.dx
        if event.key == K_DOWN:
            pygame.key.set_repeat(40)
            if ma_balle.y < hauteur - ma_balle.taille :
                ma_balle.y += ma_balle.dy
                if len(mon_split) >= 1 :
                    for k in mon_split :
                        k.y += k.dy
        if event.key == K_UP:
            pygame.key.set_repeat(40)
            if ma_balle.y > 0 + ma_balle.taille :     
                ma_balle.y -= ma_balle.dy
                if len(mon_split) >= 1 :                    
                    for k in mon_split :
                        k.y -= k.dy
        if event.key== K_SPACE :
            if ma_balle.taille >= 50 :
                division()
                ma_balle.split()              
            else:
                print("split impossible")
           
        
        
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()

    time.sleep(0.03)