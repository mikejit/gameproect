import pygame, sys, random as rdm, time, math
from utils import *

pygame.init()

screen = pygame.display.set_mode((1200,580))
pygame.display.set_caption("PLAY")
clock = pygame.time.Clock()

#plateforme 
rectanglebas = pygame.Rect(90, 450, 450, 10)
rectangleterre1 = pygame.Rect(90, 460, 450, 50)
rectanglehaut = pygame.Rect(650, 250, 400, 10)
rectangleterre2 = pygame.Rect(650, 260, 400, 50)

#soldat
soldat=pygame.image.load("soldat.png").convert_alpha()
x_soldat=175
y_soldat=365
soldatreference = soldat.get_rect(topleft=(x_soldat,y_soldat))
v_soldat=5

# variables saut
vy = 0
g = 1
saut = False

# zombie
zombie=pygame.image.load("zombie.png").convert_alpha()
x_zombie = 810
y_zombie = 105
zombiereference = zombie.get_rect(topleft=(x_zombie,y_zombie))
v_zombie = 2

run = True

while run:
    screen.fill(DarkSlateGray)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if keys[pygame.K_RIGHT]:
        soldatreference.x += v_soldat
    if keys[pygame.K_LEFT]:
        soldatreference.x -= v_soldat

    #saut
    if keys[pygame.K_SPACE] and not saut:
        vy = -20
        saut = True

    # G
    vy += g
    soldatreference.y += vy

    # plateforme de bas
    if 90 <= soldatreference.x <= 540:
        if soldatreference.y >= 365:
            soldatreference.y = 365
            vy = 0
            saut = False
    #platefforme du haut
    if 650 <= soldatreference.x <= 1050:
        if 165 <= soldatreference.y <= 250 and vy >= 0:
            soldatreference.y = 165
            vy = 0
            saut = False

    # zombies automatiques
    direction_x = soldatreference.x - x_zombie
    distance = abs(direction_x)
    if distance != 0:
        direction_x /= distance
    x_zombie += direction_x * v_zombie
    zombiereference.x = x_zombie

    # Dessins
    pygame.draw.rect(screen,GREEN,rectanglebas)
    pygame.draw.rect(screen,GREEN,rectanglehaut)
    pygame.draw.rect(screen,BROWN,rectangleterre1)
    pygame.draw.rect(screen,BROWN,rectangleterre2)
    screen.blit(soldat,soldatreference)
    screen.blit(zombie,zombiereference)

    clock.tick(100)
    pygame.display.update()

pygame.quit()
