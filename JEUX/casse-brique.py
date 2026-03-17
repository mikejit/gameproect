
import pygame, sys, random as rdm, time, math
from utils import *
import subprocess

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

player_health = 100
zombie_health = 50
zombie_last_bite = 0  
bite_cooldown = 1000  
can_damage_zombie = True 
vy_zombie = 0

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

        if event.type == pygame.KEYDOWN:
            if event.key== pygame.K_ESCAPE:
                show_pause_menu(screen)
            
    if keys[pygame.K_UP] and not saut:
        vy = -20
        saut = True

    vy += g
    soldatreference.y += vy
    

    
    if zombie_health > 0:
        # Gravity for zombie
        vy_zombie += g
        zombiereference.y += vy_zombie

        # Follow player (Horizontal only)
        if soldatreference.x > zombiereference.x:
            zombiereference.x += v_zombie
        else:
            zombiereference.x -= v_zombie

    # --- 3. PLATFORM COLLISIONS (For both Player and Zombie) ---
    # Put both in a list to check them easily
    for rect in [rectanglebas, rectanglehaut]:
        # Player collision
        if soldatreference.colliderect(rect) and vy >= 0:
            soldatreference.bottom = rect.top
            vy = 0
            saut = False
        
        # Zombie collision
        if zombiereference.colliderect(rect) and vy_zombie >= 0:
            zombiereference.bottom = rect.top
            vy_zombie = 0

    # --- 4. COMBAT LOGIC ---
    current_time = pygame.time.get_ticks()
    if zombie_health > 0:
        if zombiereference.colliderect(soldatreference):
            # Zombie bites player
            if current_time - zombie_last_bite > bite_cooldown:
                player_health -= 20
                zombie_last_bite = current_time
            
            # Player hits zombie (Check if F is held via keys)
            if keys[pygame.K_f] and can_damage_zombie:
                zombie_health -= 15
                can_damage_zombie = False # Set to False so it only hits once

    # Reset attack flag when F is released
    if not keys[pygame.K_f]:
        can_damage_zombie = True
    # Dessins
    pygame.draw.rect(screen,GREEN,rectanglebas)
    pygame.draw.rect(screen,GREEN,rectanglehaut)
    pygame.draw.rect(screen,BROWN,rectangleterre1)
    pygame.draw.rect(screen,BROWN,rectangleterre2)
    screen.blit(soldat,soldatreference)
    if zombie_health > 0:
        screen.blit(zombie,zombiereference)
    pygame.draw.rect(screen, (0,255,0,), (10, 10, player_health,20))
    pygame.draw.rect(screen, (255,0,0,), (1050, 10, zombie_health,20))

    clock.tick(100)
    pygame.display.update()

pygame.quit()
