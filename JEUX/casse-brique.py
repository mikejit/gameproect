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
rectanglebas= pygame.Rect(90,350,400,10)
rectangleterre1= pygame.Rect(90,360,400,50)


#la plateforme en haut:
rectanglehaut= pygame.Rect(650,150,400,10)
rectangleterre2= pygame.Rect(650,160,400,50)




    


run = True

#Personnages 
#soldat
x_soldat=175
y_soldat=265
soldatreference=pygame.Rect(x_soldat,y_soldat,1,1)
soldat=pygame.image.load('soldat.png')
v=5
#fonction jump pour faire sauter le soldat

def sauter():
    g=9.8
    vi=0
    while y_soldat>=265:
        vi += g
        y_soldat +=vi
    if y_soldat<=265:
        vi=0
        y_soldat=265


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
    if keys[pygame.K_DOWN]:
        y_soldat+=v
    if keys[pygame.K_SPACE]:
        sauter()
    if keys[pygame.K_RIGHT]:
        soldatreference.x_soldat+=v
    if keys[pygame.K_LEFT]:
        soldatreference.x_soldat-=v
    if keys[pygame.K_ESCAPE]:
        run=False
    


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
