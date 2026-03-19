import pygame, sys, random as rdm, time, math
import subprocess

# --- INITIALIZATION ---
pygame.init()
WIDTH, HEIGHT = 1200, 580
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PLAY")
clock = pygame.time.Clock()

# --- COLORS & FONTS ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 40, 40)
GREEN_UI = (50, 180, 50)
DARK_GRAY = (40, 40, 40)
BROWN = (139, 69, 19)
DarkSlateGray = (47, 79, 79)

font_big = pygame.font.SysFont("arial", 64, bold=True)
font_small = pygame.font.SysFont("arial", 26)
font_btn = pygame.font.SysFont("arial", 32)

# --- GAME OBJECTS ---
plateforme_bas = pygame.Rect(90, 450, 450, 20)
plateforme_terre_bas = pygame.Rect(90, 460, 450, 50)
plateforme_haut = pygame.Rect(650, 250, 400, 20)
plateforme_terre_haut = pygame.Rect(650, 260, 400, 50)

soldat = pygame.image.load("soldat.png").convert_alpha()
soldat_rect = soldat.get_rect(topleft=(175, 365))
vitesse_soldat = 5
vitesse_y_soldat = 0
gravite = 0.8
peut_sauter = False

zombie = pygame.image.load("zombie.png").convert_alpha()
zombie_rect = zombie.get_rect(topleft=(810, 105))
vitesse_zombie = 2
vitesse_y_zombie = 0

# Stats & Logic
vie_joueur = 100
vie_zombie = 50
dernier_morsure = 0
delai_morsure = 1000
peut_frapper_zombie = True
popup_state = None  
death_cause = ""    

decalage_pieds_soldat = 17
decalage_pieds_zombie = 80

# --- FUNCTIONS ---

def reset_game():
    """Resets all variables to start over"""
    global vie_joueur, vie_zombie, soldat_rect, zombie_rect, vitesse_y_soldat, vitesse_y_zombie, popup_state
    vie_joueur, vie_zombie = 100, 50
    soldat_rect.topleft = (175, 365)
    zombie_rect.topleft = (810, 105)
    vitesse_y_soldat, vitesse_y_zombie = 0, 0
    popup_state = None

def draw_popup(state, cause=""):
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 160))
    screen.blit(overlay, (0, 0))
    
    panel = pygame.Rect(400, 120, 400, 260)
    border_color = RED if state == "game_over" else GREEN_UI
    pygame.draw.rect(screen, DARK_GRAY, panel, border_radius=14)
    pygame.draw.rect(screen, border_color, panel, 4, border_radius=14)
    
    title_text = "GAME OVER" if state == "game_over" else "YOU WIN!"
    title = font_big.render(title_text, True, border_color)
    screen.blit(title, title.get_rect(center=(WIDTH // 2, 200)))

    if state == "game_over":
        sub_text = "Caught by a zombie!" if cause == "zombie" else "You fell off the platform!"
        sub = font_small.render(sub_text, True, WHITE)
        screen.blit(sub, sub.get_rect(center=(WIDTH // 2, 258)))

    retry_rect = pygame.Rect(430, 300, 155, 48)
    quit_rect = pygame.Rect(620, 300, 155, 48)
    
    pygame.draw.rect(screen, GREEN_UI, retry_rect, border_radius=8)
    pygame.draw.rect(screen, RED, quit_rect, border_radius=8)
    
    screen.blit(font_small.render("RETRY", True, WHITE), font_small.render("RETRY", True, WHITE).get_rect(center=retry_rect.center))
    screen.blit(font_small.render("QUIT", True, WHITE), font_small.render("QUIT", True, WHITE).get_rect(center=quit_rect.center))
    
    return retry_rect, quit_rect

def show_pause_menu(screen):
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 150))
    screen.blit(overlay, (0, 0))

    popup = pygame.Rect(400, 100, 400, 380)
    pygame.draw.rect(screen, (50, 50, 50), popup, border_radius=10)
    pygame.draw.rect(screen, WHITE, popup, 3, border_radius=10)

    title = font_big.render("PAUSED", True, WHITE)
    screen.blit(title, title.get_rect(center=(600, 140)))

    # Define Buttons in your specific order
    btn_resume   = pygame.Rect(450, 190, 300, 45)
    btn_menu     = pygame.Rect(450, 250, 300, 45) # Main Menu is now 2nd
    btn_retry    = pygame.Rect(450, 310, 300, 45) # Retry is now 3rd
    btn_settings = pygame.Rect(450, 370, 300, 45)
    btn_quit     = pygame.Rect(450, 430, 300, 45)

    buttons = [
        (btn_resume, "Resume"),
        (btn_menu, "Main Menu"),
        (btn_retry, "Retry"),
        (btn_settings, "Settings"),
        (btn_quit, "Quit")
    ]

    while True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_resume.collidepoint(event.pos): return
                if btn_menu.collidepoint(event.pos):
                    pygame.quit(); subprocess.run([sys.executable, "main-menu.py"]); sys.exit()
                if btn_retry.collidepoint(event.pos): reset_game(); return
                if btn_settings.collidepoint(event.pos):
                    pygame.quit(); subprocess.run([sys.executable, "main-menu.py", "--settings"]); sys.exit()
                if btn_quit.collidepoint(event.pos):
                    pygame.quit(); sys.exit()

        # Draw Buttons with Hover Effect
        for btn, label in buttons:
            color = (100, 100, 100) if btn.collidepoint(mouse) else (70, 70, 70)
            pygame.draw.rect(screen, color, btn, border_radius=5)
            pygame.draw.rect(screen, WHITE, btn, 2, border_radius=5)
            text = font_btn.render(label, True, WHITE)
            screen.blit(text, text.get_rect(center=btn.center))
        
        pygame.display.update()

# --- MAIN LOOP ---
run = True
retry_rect, quit_rect = pygame.Rect(0,0,0,0), pygame.Rect(0,0,0,0)

while run:
    screen.fill(DarkSlateGray)
    current_time = pygame.time.get_ticks()
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                show_pause_menu(screen)
        
        if event.type == pygame.MOUSEBUTTONDOWN and popup_state:
            if retry_rect.collidepoint(event.pos):
                reset_game()
            if quit_rect.collidepoint(event.pos):
                run = False

    if not popup_state:
        # Player movement
        if keys[pygame.K_LEFT]: soldat_rect.x -= vitesse_soldat
        if keys[pygame.K_RIGHT]: soldat_rect.x += vitesse_soldat
        if (keys[pygame.K_UP] or keys[pygame.K_SPACE]) and not peut_sauter:
            vitesse_y_soldat = -18
            peut_sauter = True

        vitesse_y_soldat += gravite
        soldat_rect.y += vitesse_y_soldat

        if vie_zombie > 0:
            vitesse_y_zombie += gravite
            zombie_rect.y += vitesse_y_zombie
            if soldat_rect.x > zombie_rect.x: zombie_rect.x += vitesse_zombie
            else: zombie_rect.x -= vitesse_zombie

        # Collisions
        for rect in [plateforme_bas, plateforme_haut]:
            if soldat_rect.colliderect(rect) and vitesse_y_soldat >= 0:
                soldat_rect.bottom = rect.top + decalage_pieds_soldat
                vitesse_y_soldat = 0
                peut_sauter = False
            if zombie_rect.colliderect(rect) and vitesse_y_zombie >= 0:
                zombie_rect.bottom = rect.top + decalage_pieds_zombie
                vitesse_y_zombie = 0

        # Combat
        if vie_zombie > 0 and zombie_rect.colliderect(soldat_rect):
            if current_time - dernier_morsure > delai_morsure:
                vie_joueur -= 20
                dernier_morsure = current_time
            if keys[pygame.K_f] and peut_frapper_zombie:
                vie_zombie -= 15
                peut_frapper_zombie = False
        
        if not keys[pygame.K_f]: peut_frapper_zombie = True

        # Death conditions
        if soldat_rect.y > 700:
            popup_state = "game_over"; death_cause = "fall"
        elif vie_joueur <= 0:
            vie_joueur = 0; popup_state = "game_over"; death_cause = "zombie"
        elif vie_zombie <= 0:
            vie_zombie = 0; popup_state = "win"

    # --- DRAWING ---
    pygame.draw.rect(screen, GREEN_UI, plateforme_bas)
    pygame.draw.rect(screen, GREEN_UI, plateforme_haut)
    pygame.draw.rect(screen, BROWN, plateforme_terre_bas)
    pygame.draw.rect(screen, BROWN, plateforme_terre_haut)

    screen.blit(soldat, soldat_rect)
    if vie_zombie > 0:
        screen.blit(zombie, zombie_rect)

    # UI: Player Health Bar
    pygame.draw.rect(screen, WHITE, (9, 9, 102, 22), 2)
    pygame.draw.rect(screen, (0, 255, 0), (10, 10, max(0, vie_joueur), 20))
    hp_text = font_small.render(f"{vie_joueur}", True, WHITE)
    screen.blit(hp_text, (120, 8))

    # UI: Zombie Health Bar
    if vie_zombie > 0:
        pygame.draw.rect(screen, WHITE, (1049, 9, 52, 22), 2)
        pygame.draw.rect(screen, RED, (1050, 10, vie_zombie, 20))

    if popup_state:
        retry_rect, quit_rect = draw_popup(popup_state, death_cause)

    clock.tick(60)
    pygame.display.update()

pygame.quit()
