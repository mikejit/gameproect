import pygame, sys, random as rdm, time, math
from utils import *
import subprocess
#MINI
pygame.init()
screen = pygame.display.set_mode((1200, 580))
pygame.display.set_caption("PLAY")
clock = pygame.time.Clock()

# platformes
plateforme_bas = pygame.Rect(90, 450, 450, 20)
plateforme_terre_bas = pygame.Rect(90, 460, 450, 50)
plateforme_haut = pygame.Rect(650, 250, 400, 20)
plateforme_terre_haut = pygame.Rect(650, 260, 400, 50)

#soldat
soldat = pygame.image.load("soldat.png").convert_alpha()
soldat_rect = soldat.get_rect(topleft=(175, 365))
vitesse_soldat = 5
#/MINI

#var saut
vitesse_y_soldat = 0
gravite = 0.8
peut_sauter = False

# zombie
zombies = []
if vie_zombie==0:
    for i in range(3): 
        zombie = pygame.image.load("zombie.png").convert_alpha()
        zombie_rect = zombie.get_rect(topleft=(810, 105))
        vitesse_zombie = 2
        

# vie combat
vie_joueur = 100
vie_zombie = 50
dernier_morsure = 0
delai_morsure = 1000
peut_frapper_zombie = True
vitesse_y_zombie = 0

# Offset pour que les pieds touchent bien la plateforme
decalage_pieds_soldat = 17
decalage_pieds_zombie =80
run = True


def show_pause_menu(screen):
    # Overlay semi-transparent
    overlay = pygame.Surface((1200, 580), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 150))
    screen.blit(overlay, (0, 0))

    # Boîte de pause
    popup = pygame.Rect(400, 160, 400, 280)
    pygame.draw.rect(screen, (50, 50, 50), popup)
    pygame.draw.rect(screen, (255, 255, 255), popup, 3)

    font_title = pygame.font.SysFont(None, 50)
    font_btn = pygame.font.SysFont(None, 40)

    title = font_title.render("PAUSED", True, (255, 255, 255))
    screen.blit(title, (550, 170))

    btn_menu = pygame.Rect(450, 240, 300, 50)
    btn_settings = pygame.Rect(450, 310, 300, 50)
    btn_quit = pygame.Rect(450, 380, 300, 50)

    mouse = pygame.mouse.get_pos()
    for btn, label in [(btn_menu, "Main Menu"), (btn_settings, "Settings"),(btn_quit, "Quit")]:
        color = (100, 100, 100) if btn.collidepoint(mouse) else (70, 70, 70)
        pygame.draw.rect(screen, color, btn)
        pygame.draw.rect(screen, (255, 255, 255), btn, 2)
        text = font_btn.render(label, True, (255, 255, 255))
        text_rect = text.get_rect(center=btn.center)
        screen.blit(text, text_rect)

    pygame.display.update()

    # Attente du clic ou ESC
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return  # Reprendre le jeu
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_menu.collidepoint(event.pos):
                    pygame.quit()
                    subprocess.run([sys.executable, "main-menu.py"])
                    sys.exit()
                if btn_settings.collidepoint(event.pos):
                    pygame.quit()
                    subprocess.run([sys.executable, "main-menu.py", "--settings"])
                    sys.exit()
                if btn_quit.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()


while run:
    screen.fill(DarkSlateGray)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                show_pause_menu(screen)

    # Mouvement horizontal du soldat
    if keys[pygame.K_LEFT]:
        soldat_rect.x -= vitesse_soldat
    if keys[pygame.K_RIGHT]:
        soldat_rect.x += vitesse_soldat

    # Saut
    if (keys[pygame.K_UP] or keys[pygame.K_SPACE]) and not peut_sauter:
        vitesse_y_soldat = -18
        peut_sauter = True

    vitesse_y_soldat += gravite
    soldat_rect.y += vitesse_y_soldat


    #si il tombe
    if soldat_rect.y>700 or vie_joueur==0:
        run=False

    if vie_zombie > 0:
        # Gravité du zombie
        vitesse_y_zombie += gravite
        zombie_rect.y += vitesse_y_zombie
        #creation de tuples avec vie,vitesse,image
        # Le zombie suit le joueur
        if soldat_rect.x > zombie_rect.x:
            zombie_rect.x += vitesse_zombie
        else:
            zombie_rect.x -= vitesse_zombie

    # contact avec les platformes
    for rect in [plateforme_bas, plateforme_haut]:
        # Collision soldat
        if soldat_rect.colliderect(rect) and vitesse_y_soldat >= 0:
            soldat_rect.bottom = rect.top + decalage_pieds_soldat
            vitesse_y_soldat = 0
            peut_sauter = False

        # Collision zombie
        if zombie_rect.colliderect(rect) and vitesse_y_zombie >= 0:
            zombie_rect.bottom = rect.top + decalage_pieds_zombie
            vitesse_y_zombie = 0

    # combat
    current_time = pygame.time.get_ticks()
    if vie_zombie > 0 and zombie_rect.colliderect(soldat_rect):
        # Zombie mord le joueur
        if current_time - dernier_morsure > delai_morsure:
            vie_joueur -= 20
            dernier_morsure = current_time

        # Joueur frappe le zombie avec F
        if keys[pygame.K_f] and peut_frapper_zombie:
            vie_zombie -= 15
            peut_frapper_zombie = False

    if not keys[pygame.K_f]:
        peut_frapper_zombie = True

    # dessin
    pygame.draw.rect(screen, GREEN, plateforme_bas)
    pygame.draw.rect(screen, GREEN, plateforme_haut)
    pygame.draw.rect(screen, BROWN, plateforme_terre_bas)
    pygame.draw.rect(screen, BROWN, plateforme_terre_haut)

    screen.blit(soldat, soldat_rect)
    if vie_zombie > 0:
        screen.blit(zombie, zombie_rect)

    # vie
    pygame.draw.rect(screen, (0, 255, 0), (10, 10, vie_joueur, 20))
    pygame.draw.rect(screen, (255, 0, 0), (1050, 10, vie_zombie, 20))

    clock.tick(100)
    pygame.display.update()

pygame.quit()
