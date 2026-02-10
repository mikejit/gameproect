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
#portal
rectangleportal=pygame.Rect(920,35,10,30) 
portal=pygame.image.load('portal.png')



    


run = True

#Personnages 
#soldat
x_soldat=175
y_soldat=265
soldatreference=pygame.Rect(x_soldat,y_soldat,1,1)
soldat=pygame.image.load('soldat.png')
v=5





#zombies 
x_zombie=810
y_zombie=5
zombiereference=pygame.Rect(x_zombie,y_zombie,1,1)
zombie=pygame.image.load('zombie.png')

    # rect_vaisseau=vaisseau.get_rect()
# -------- Boucle principale du jeu -----------
while run:
    # fond d´écran
    screen.fill(SKYBLUE)
    # --- Gestion des évènements
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("clic souris")      
    keys = pygame.key.get_pressed()
         
    if keys[pygame.K_SPACE]:
        print('barre espace')
    if keys[pygame.K_RIGHT]:
        print("touche right")
        x_soldat+=v
    if keys[pygame.K_LEFT]:
        print("touche gauche")
        x_soldat-=v
    if keys[pygame.K_ESCAPE]:
        run=False
    


    # Dessins
    pygame.draw.rect(screen,GREEN,rectanglebas)
    pygame.draw.rect(screen,GREEN,rectanglehaut)
    pygame.draw.rect(screen,BROWN,rectangleterre1)
    pygame.draw.rect(screen,BROWN,rectangleterre2)
    screen.blit(portal,rectangleportal) 
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
 
