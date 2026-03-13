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

def show_pause_menu(screen):
    # Semi-transparent overlay
    overlay = pygame.Surface((1200, 580), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 150))
    screen.blit(overlay, (0, 0))

    # Popup box
    popup = pygame.Rect(400, 150, 400, 280)
    pygame.draw.rect(screen, (50, 50, 50), popup)
    pygame.draw.rect(screen, (255, 255, 255), popup, 3)

    font_title = pygame.font.SysFont(None, 50)
    font_btn = pygame.font.SysFont(None, 40)

    # Title
    title = font_title.render("PAUSED", True, (255, 255, 255))
    screen.blit(title, (550, 170))

    # Buttons
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

    # Wait for click or ESC to close
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return  # Resume game
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
