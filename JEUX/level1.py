import pygame, sys, random as rdm, time, math
from utils import *
import subprocess


# MINI
pygame.init()
screen = pygame.display.set_mode((1200, 580))
pygame.display.set_caption("PLAY")
clock = pygame.time.Clock()


#sons
pygame.init()
pygame.mixer.init()




# platformes
plateforme_bas = pygame.Rect(90, 450, 450, 20)
plateforme_terre_bas = pygame.Rect(90, 460, 450, 50)
plateforme_haut = pygame.Rect(650, 250, 400, 20)
plateforme_terre_haut = pygame.Rect(650, 260, 400, 50)


zombie = pygame.image.load("JEUX/zombie.png").convert_alpha()
# soldat
soldat = pygame.image.load("JEUX/soldat.png").convert_alpha()
soldat_rect = soldat.get_rect(topleft=(175, 365))
vitesse_soldat = 5
# /MINI

# var saut
vitesse_y_soldat = 0
gravite = 0.8
peut_sauter = False

# zombie

diff_zmb=[
    (2,50),
    (2,100),
    (2,150),
    (2,200),
    (2,250)
]
zombies=[]
niv=1  # start at 1 so at least 1 zombie

def ajout_zomb(niv):
    nouv_zomb=[]
    for i in range(niv):
        vitesse, vie = rdm.choice(diff_zmb)
        rect = zombie.get_rect(topleft=(rdm.randint(700,1100),100))
        nouv_zomb.append({
            "rect":rect,
            "speed":vitesse,
            "health":vie,
            "vy":0
        })

    return nouv_zomb

zombies=ajout_zomb(niv)

# vie combat
vie_joueur = 100
dernier_morsure = 0
delai_morsure = 1000
peut_frapper_zombie = True

# Offset pour que les pieds touchent bien la plateforme
decalage_pieds_soldat = 17
decalage_pieds_zombie = 80
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
    for btn, label in [(btn_menu, "Main Menu"), (btn_settings, "Settings"), (btn_quit, "Quit")]:
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

    # si il tombe
    if soldat_rect.y > 700 or vie_joueur == 0:
        pygame.quit()
        subprocess.run([sys.executable, "JEUX/game-over.py"])
        sys.exit()

    
        

    # zombie update
    for z in zombies:
        if z["health"] > 0:
            # Gravité du zombie
            z["vy"] += gravite
            z["rect"].y += z["vy"]

            # Le zombie suit le joueur
            if soldat_rect.x > z["rect"].x:
                z["rect"].x += z["speed"]
            else:
                z["rect"].x -= z["speed"]

    # mudanças

    if all(z["health"] <= 0 for z in zombies):
        niv += 1

        
        zombies = ajout_zomb(niv)
        vie_joueur = 100

    # mudanças acaba
    # contact avec les platformes
    for rect in [plateforme_bas, plateforme_haut]:
        # Collision soldat
        if soldat_rect.colliderect(rect) and vitesse_y_soldat >= 0:
            soldat_rect.bottom = rect.top + decalage_pieds_soldat
            vitesse_y_soldat = 0
            peut_sauter = False

        # Collision zombie
        for z in zombies:
            if z["rect"].colliderect(rect) and z["vy"] >= 0:
                z["rect"].bottom = rect.top + decalage_pieds_zombie
                z["vy"] = 0

    # combat
    current_time = pygame.time.get_ticks()
    for z in zombies:
        if z["health"] > 0 and z["rect"].colliderect(soldat_rect):
            # Zombie mord le joueur
            if current_time - dernier_morsure > delai_morsure:
    
                vie_joueur -= 20
                dernier_morsure = current_time

            # Joueur frappe le zombie avec F
            if keys[pygame.K_f] and peut_frapper_zombie:
                
                z["health"] -= 15
                peut_frapper_zombie = False

    if not keys[pygame.K_f]:
        peut_frapper_zombie = True
        

    # dessin
    pygame.draw.rect(screen, GREEN, plateforme_bas)
    pygame.draw.rect(screen, GREEN, plateforme_haut)
    pygame.draw.rect(screen, BROWN, plateforme_terre_bas)
    pygame.draw.rect(screen, BROWN, plateforme_terre_haut)

    screen.blit(soldat, soldat_rect)

    # barre de vie du joueur (au-dessus du soldat)
    player_bar_width = 50
    player_bar_height = 7
    bar_x = soldat_rect.x
    bar_y = soldat_rect.y - 10
    current_width = int((vie_joueur / 100) * player_bar_width)
    # fond rouge
    pygame.draw.rect(screen, (255, 0, 0), (bar_x, bar_y, player_bar_width, player_bar_height))
    # vie verte
    pygame.draw.rect(screen, (0, 255, 0), (bar_x, bar_y, current_width, player_bar_height))

    for z in zombies:
        if z["health"] > 0:
            screen.blit(zombie, z["rect"])
            # barre de vie du zombie (au-dessus de la tête)
            bar_width = 40
            bar_height = 5
            # position
            bar_x = z["rect"].x
            bar_y = z["rect"].y - 10
            # max health (important!)
            max_health = 250  # biggest value from diff_zmb
            # calcul de la vie actuelle
            current_width = int((z["health"] / max_health) * bar_width)
            # fond rouge
            pygame.draw.rect(screen, (255, 0, 0), (bar_x, bar_y, bar_width, bar_height))
            # vie verte
            pygame.draw.rect(screen, (0, 255, 0), (bar_x, bar_y, current_width, bar_height))

    # vie
    pygame.draw.rect(screen, (0, 255, 0), (10, 10, vie_joueur, 20))

    clock.tick(100)
    pygame.display.update()

