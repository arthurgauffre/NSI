import pygame, sys
import time
from pygame.locals import *
from random import randint

pygame.font.init()
largeur = 1300
hauteur = 800
timer = 0
paramètre = True
règle = True
fenetre = pygame.display.set_mode((largeur, hauteur))
# création du texte
def texte(text, couleur, coordonnée, taille) :  
    mytext = pygame.font.SysFont('Times New Roman', taille)
    mytext = mytext.render(text, False, couleur)
    fenetre.blit(mytext, coordonnée)

class Balle :
    
    def __init__(self) :
        self.x = randint(0,largeur)
        self.y = randint(0,hauteur)
        self.couleur = (randint(0,255), randint(0,255), randint(0,255))
        self.dx = randint(-5,5)
        self.dy = randint(-5,5)
        self.taille = 8
    
    def collision(self) :        
        if ((ma_balle.x-self.x)**2 + (ma_balle.y-self.y)**2)**0.5 <= (ma_balle.taille + self.taille) :
           all_balls.remove(self)
           ma_balle.taille += 0.6

    def bot_collision(self) :              
        if ((ma_balle.x-self.x)**2 + (ma_balle.y-self.y)**2)**0.5 <= (ma_balle.taille + self.taille) :
            if ma_balle.taille >= self.taille :
                bot.remove(self)
            else : 
                while True : 
                    fenetre.fill([0, 0, 0])
                    texte('Game Over!', (255,255,255), (largeur//2 - 200, hauteur//2 - 150), 100)
                    texte('Appuyez sur échap pour fermer le jeu', (255,255,255), (largeur//2 - 200, hauteur//2 ), 25)
                    pygame.display.flip()
                    for event in pygame.event.get():
                        if event.type == KEYDOWN :
                            if event.key == K_ESCAPE :
                                sys.exit()         
        for k in all_balls : 
            if ((k.x-self.x)**2 + (k.y-self.y)**2)**0.5 <= (k.taille + self.taille) :
                
                    all_balls.remove(k)
                    self.taille += 0.3
        for balle in bot:
            if ((self.x-balle.x)**2 + (self.y-balle.y)**2)**0.5 < self.taille + balle.taille:
                self.dx, balle.dx = balle.dx, self.dx
                self.dy, balle.dy = balle.dy, self.dy

    def ressources(self) :
        self.taille= 5
        self.x = randint(0,largeur)
        self.y = randint(0,hauteur)
    
    def bouge(self) : 
        self.dessine()
        if timer > 3 :      
            self.x += self.dx
            self.y += self.dy
        if self.x > largeur - self.taille or self.x < self.taille :
            self.dx = -self.dx
        if self.y > hauteur - self.taille or self.y < self.taille :
            self.dy = -self.dy
    
    def respawn(self) : 
        if len(all_balls) < lim_de_balles : 
            new_ball = Balle()
            all_balls.append(new_ball)

    def dessine(self) :
        pygame.draw.circle(fenetre,self.couleur,(self.x,self.y),self.taille)

#les balles servent de boutons pour les paramètres
balle_moins = Balle()
balle_moins.x, balle_moins.y = largeur//2 + -100, hauteur//2 + 20
balle_plus = Balle()
balle_plus.x, balle_plus.y = largeur//2 + 100, hauteur//2 + 20  
balle_plus.taille, balle_moins.taille = 40, 40
balle_moins.couleur, balle_plus.couleur = (255,0,0), (0,255,0)
balle_start = Balle()
balle_start.x, balle_start.y = largeur//2 , hauteur//2 + 175
balle_start.taille = 50
balle_start.couleur = (100,100,100)
balle_ressource_100 = Balle ()
balle_ressource_200 = Balle ()
balle_ressource_300 = Balle ()
balle_ressource_400 = Balle ()
balle_ressource_100.x, balle_ressource_200.x, balle_ressource_300.x, balle_ressource_400.x = largeur//2, largeur//2 + 100, largeur//2 + 200, largeur//2 + 300
balle_ressource_100.y, balle_ressource_200.y, balle_ressource_300.y, balle_ressource_400.y = hauteur - 80, hauteur - 80, hauteur - 80, hauteur - 80
balle_ressource_100.couleur, balle_ressource_200.couleur, balle_ressource_300.couleur, balle_ressource_400.couleur = (255,0,0), (255,0,0), (255,0,0), (255,0,0)
balle_ressource_100.taille, balle_ressource_200.taille, balle_ressource_300.taille, balle_ressource_400.taille = 30, 30, 30, 30
balle_curseur = Balle()
balle_curseur.taille = 5
nbr_bot_str = 48   #je récupère l'ascii de 0 pour l'afficher le chiffre en str ensuite
nbr_bot = 0
nbr_ressource = 0
# affichage des règles et des commandes
while règle == True :
    fenetre.fill([255, 255, 255])
    texte('Règles du jeu:', (0,0,0), (20, 10), 40)
    texte('- Manger les balles pour grossir', (0,0,0), (20, 60), 25)
    texte('- Devenir assez gros pour manger les bots', (0,0,0), (20, 100), 25)
    texte('- Vous gagnez si vous avez mangé tous les bots sinon vous perdez si un bot vous mange', (0,0,0), (20, 140), 25)
    texte('- Vous avez 3 secondes avant que les bots bouges', (0,0,0), (20, 180), 25)
    texte('Commandes:', (0,0,0), (20, 240), 40)
    texte('- ZQSD ou les flèches pour se déplacer', (0,0,0), (20, 290), 25)
    texte('- Z = Haut, Q = Gauche, S = Bas et D = Droite', (0,0,0), (20, 330), 25)
    texte('- Flèche haut = Haut, Flèche bas = bas, Flèche droite = Droite et Flèche gauche = Gauche', (0,0,0), (20, 370), 25)
    texte('- Vous pouvez rester appuyé', (0,0,0), (20, 410), 25)
    texte('Appuyez sur Entrée pour accéder aux paramètres de jeu !', (0,0,0), (largeur - 500, hauteur - 50), 20)   
    for event in pygame.event.get():
                if event.type == KEYDOWN :
                    if event.key == K_RETURN :
                        règle = False
    pygame.display.flip()
# affichage des paramètres    
while paramètre == True :
    fenetre.fill([255, 255, 255])
    mx, my = pygame.mouse.get_pos()
    balle_curseur.x, balle_curseur.y = mx, my
    balle_plus.dessine()
    balle_moins.dessine()
    balle_start.dessine()
    balle_ressource_100.dessine()
    balle_ressource_200.dessine()
    balle_ressource_300.dessine()
    balle_ressource_400.dessine()
    texte('bot :', (0,0,0), (largeur//2 - 60, hauteur//2 + 65), 50)                
    texte(chr(nbr_bot_str), (0,0,0), (largeur//2 + 30, hauteur//2 + 70), 50)
    texte('Nombre de bot (max: 9)', (0,0,0), (largeur//2 -200, hauteur//2 - 125), 50)
    texte('+1', (0,0,0), (largeur//2 + 80, hauteur//2 - 10), 50)
    texte('-1', (0,0,0), (largeur//2 - 120, hauteur//2 - 10), 50)
    texte('PLAY', (255,255,255), (largeur//2 - 40, hauteur//2 + 150), 35)
    texte('Nombre de ressources:', (0,0,0), (largeur//2 - 305, hauteur - 100), 30)
    texte('100', (0,0,0), (largeur//2 - 20, hauteur - 100), 30)
    texte('200', (0,0,0), (largeur//2 + 80 , hauteur - 100), 30)
    texte('300', (0,0,0), (largeur//2 + 180, hauteur - 100), 30)
    texte('400', (0,0,0), (largeur//2 + 280, hauteur - 100), 30)
    
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN :
            if ((balle_plus.x-balle_curseur.x)**2 + (balle_plus.y-balle_curseur.y)**2)**0.5 <= (balle_plus.taille + balle_curseur.taille) :
                if nbr_bot_str < 57:
                    nbr_bot_str += 1
                    nbr_bot += 1
            if ((balle_moins.x-balle_curseur.x)**2 + (balle_moins.y-balle_curseur.y)**2)**0.5 <= (balle_moins.taille + balle_curseur.taille) :
                if nbr_bot_str > 48 :
                    nbr_bot_str -= 1
                    nbr_bot -= 1
            if ((balle_start.x-balle_curseur.x)**2 + (balle_start.y-balle_curseur.y)**2)**0.5 <= (balle_start.taille + balle_curseur.taille) :
                paramètre = False
            if ((balle_ressource_100.x-balle_curseur.x)**2 + (balle_ressource_100.y-balle_curseur.y)**2)**0.5 <= (balle_ressource_100.taille + balle_curseur.taille) :
                nbr_ressource = 100
                balle_ressource_100.couleur = (0,255,0)
                balle_ressource_200.couleur, balle_ressource_300.couleur, balle_ressource_400.couleur = (255,0,0), (255,0,0), (255,0,0)
            if ((balle_ressource_200.x-balle_curseur.x)**2 + (balle_ressource_200.y-balle_curseur.y)**2)**0.5 <= (balle_ressource_200.taille + balle_curseur.taille) :
                nbr_ressource = 200
                balle_ressource_200.couleur = (0,255,0)
                balle_ressource_100.couleur, balle_ressource_300.couleur, balle_ressource_400.couleur = (255,0,0), (255,0,0), (255,0,0)
            if ((balle_ressource_300.x-balle_curseur.x)**2 + (balle_ressource_300.y-balle_curseur.y)**2)**0.5 <= (balle_ressource_300.taille + balle_curseur.taille) :
                nbr_ressource = 300
                balle_ressource_300.couleur = (0,255,0)
                balle_ressource_100.couleur, balle_ressource_200.couleur, balle_ressource_400.couleur = (255,0,0), (255,0,0), (255,0,0)
            if ((balle_ressource_400.x-balle_curseur.x)**2 + (balle_ressource_400.y-balle_curseur.y)**2)**0.5 <= (balle_ressource_400.taille + balle_curseur.taille) :
                nbr_ressource = 400
                balle_ressource_400.couleur = (0,255,0)
                balle_ressource_100.couleur, balle_ressource_200.couleur, balle_ressource_300.couleur = (255,0,0), (255,0,0), (255,0,0)
    pygame.display.flip()
    
#création des bots   
bot = []
for a in range(nbr_bot) :
    new_bot = Balle() 
    new_bot.x = randint(50,largeur-50)       #le 50 permet d'éviter un bug de balles bloquées sur les paroies 
    new_bot.y = randint(50,hauteur-50)
    new_bot.couleur = (200, 24, 24)
    new_bot.dx = randint(-8,8)
    new_bot.dy = randint(-8,8)
    new_bot.taille = randint(5,50)
    bot.append(new_bot)
    
#création des ressources
all_balls = [Balle() for k in range(nbr_ressource)]
lim_de_balles = len(all_balls)

#création de la balle que l'on contrôle
ma_balle = Balle()
ma_balle.taille = 10
ma_balle.x = largeur/2
ma_balle.y = hauteur/2
ma_balle.dx = 6
ma_balle.dy = 6
ma_balle.couleur =  (53, 229, 42)

fenetre = pygame.display.set_mode((largeur, hauteur))
fenetre.fill([255,255,255])

while True :
    fenetre.fill([255,255,255])

    for balle in all_balls:
        balle.dessine()
        balle.respawn()
        balle.collision()
    
    for a in bot : 
        a.bot_collision()
        a.bouge() 
        a.dessine    

    pygame.draw.circle(fenetre,ma_balle.couleur,(ma_balle.x,ma_balle.y),ma_balle.taille)

    pygame.display.update()
    
    if len(bot) == 0:
        while True : 
            fenetre.fill([0, 0, 0])
            texte('You Win!', (255,255,255), (largeur//2 - 200, hauteur//2 - 150), 100)
            texte('Appuyez sur échap pour fermer le jeu', (255,255,255), (largeur//2 - 200, hauteur//2 ), 25)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == KEYDOWN :
                    if event.key == K_ESCAPE :
                        sys.exit()
    #commande de déplacement    
    for event in pygame.event.get():   
        if event.type == KEYDOWN:
            if event.key == K_RIGHT or event.key == K_d:
                pygame.key.set_repeat(40)
                if ma_balle.x < largeur - ma_balle.taille :
                    ma_balle.x += ma_balle.dx
            if event.key == K_LEFT or event.key == K_q:
                pygame.key.set_repeat(40)
                if ma_balle.x > 0 + ma_balle.taille :    
                    ma_balle.x -= ma_balle.dx
            if event.key == K_DOWN or event.key == K_s:
                pygame.key.set_repeat(40)
                if ma_balle.y < hauteur - ma_balle.taille :
                    ma_balle.y += ma_balle.dy
            if event.key == K_UP or event.key == K_z:
                pygame.key.set_repeat(40)
                if ma_balle.y > 0 + ma_balle.taille :     
                    ma_balle.y -= ma_balle.dy
            if event.key == K_ESCAPE :
                sys.exit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
    #création d'un timer
    timer += 0.03
    time.sleep(0.03)