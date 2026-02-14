import pygame, sys
import random as rdm
from utils import *
import time

pygame.init()

# initialisation de l´écran avec sa taille et le titre
screen = pygame.display.set_mode(size)
pygame.display.set_caption("PLAY")

# gestion de la vitesse de rafraichissement de l´écran
clock = pygame.time.Clock()




# la plateforme en bas :
rectanglebas= pygame.Rect(90,350,450,10)
rectangleterre1= pygame.Rect(90,360,450,50)


#la plateforme en haut:
rectanglehaut= pygame.Rect(650,150,400,10)
rectangleterre2= pygame.Rect(650,160,400,50)


#variables de jump
saut=False
jh=20
g=1
vy=jh
    


run = True

#Personnages 
#soldat
x_soldat=175
y_soldat=265
soldat=pygame.image.load('soldat.png').convert_alpha()
soldatreference = soldat.get_rect()
soldatreference.topleft = (x_soldat, y_soldat)
v=5

#zombies 
x_zombie=810
y_zombie=5
zombiereference=pygame.Rect(x_zombie,y_zombie,1,1)
zombie=pygame.image.load('zombie.png')
# Creation zombies 
def create_zombie():
    zombies=[]
    for i in range (3):
        rectangle = rdm.choice([rectanglebas, rectanglehaut])
        if rectangle == rectanglebas:
            x_bas = rdm.randint(90,490)
            y_bas = 350
            zombies.append([x_bas, y_bas], zombie)
        else:
            x_haut = rdm.randint(650,1050)
            y_haut = 150
            zombies.append([x_haut, y_haut], zombie)
    
        return zombies     
#Level 1 


    # rect_vaisseau=vaisseau.get_rect()
# -------- Boucle principale du jeu -----------
while run:
    # fond d´écran
    screen.fill(DarkSlateGray)
    # --- Gestion des évènements
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("clic souris")      
    keys = pygame.key.get_pressed()

    #para fazer o agaixamento do soldado temos que fazer uma foto differente do gajo 
    #kiko tenta fazer um png mais pequeno ou nsei pto 
    
    if keys[pygame.K_SPACE]:
        saut=True
    if saut: 
        soldatreference.y-=vy
        #effet de graviter sur le saut
        vy-=g
        if vy<-jh:
            saut=False
            vy=jh
    if keys[pygame.K_RIGHT]:
        soldatreference.x+=v
    if keys[pygame.K_LEFT]:
        soldatreference.-=v
    if keys[pygame.K_ESCAPE]:
        run=False
    
    #si le joueur tombe
    if soldatreference.x>=505 or soldatreference.x<=15:
        v=0
        soldatreference.y+=g
        if soldatreference.y>=480:
            soldatreference.x=175
            soldatreference.y=265
            v=5

    #kiko faz um ecra game over 
    
    # Dessins
    pygame.draw.rect(screen,GREEN,rectanglebas)
    pygame.draw.rect(screen,GREEN,rectanglehaut)
    pygame.draw.rect(screen,BROWN,rectangleterre1)
    pygame.draw.rect(screen,BROWN,rectangleterre2) 
    screen.blit(soldat,soldatreference)
    screen.blit(zombie,zombiereference)
    # Mouvements de la balle

    

    


    # 60 mises à jour par seconde
    clock.tick(100)
    # mise à jour de l´écran
    pygame.display.update()

time.sleep(0.2)
# On sort de la boucle et on quitte
pygame.quit()
