import pygame
import sys
import subprocess

pygame.init()
pygame.mixer.init()
songameover=pygame.mixer.Sound("JEUX/lose.mp3")
songameover.play()

WIDTH, HEIGHT = 1200, 580
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Death Screen Preview")
clock = pygame.time.Clock()


page = "game-over"
death_cause = "zombie" 


BG        = (34, 34, 85) 
WHITE     = (255, 255, 255)
RED       = (200, 40, 40)
GREEN     = (50, 180, 50)
DARK_GRAY = (40, 40, 40)
YELLOW    = (255, 220, 50)

font       = pygame.font.SysFont("arial", 50, bold=True)
font_big   = pygame.font.SysFont("arial", 64, bold=True)
font_small = pygame.font.SysFont("arial", 26)

def draw_title(text):
    t = font.render(text, True, YELLOW)
    screen.blit(t, t.get_rect(center=(WIDTH // 2, 80)))

def draw_game_over(cause):
    
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180)) 
    screen.blit(overlay, (0, 0))

    
    panel = pygame.Rect(400, 150, 400, 250)
    pygame.draw.rect(screen, DARK_GRAY, panel, border_radius=15)
    pygame.draw.rect(screen, RED, panel, 5, border_radius=15)

    
    title = font_big.render("YOU DIED", True, RED)
    screen.blit(title, title.get_rect(center=(WIDTH // 2, 220)))

   
    msg = "Caught by a zombie!" if cause == "zombie" else "You fell off the world!"
    sub = font_small.render(msg, True, WHITE)
    screen.blit(sub, sub.get_rect(center=(WIDTH // 2, 280)))

    
    retry_rect = pygame.Rect(430, 320, 140, 45)
    quit_rect  = pygame.Rect(630, 320, 140, 45)
    
    pygame.draw.rect(screen, GREEN, retry_rect, border_radius=8)
    pygame.draw.rect(screen, RED, quit_rect, border_radius=8)

    retry_txt = font_small.render("RETRY", True, WHITE)
    quit_txt  = font_small.render("QUIT", True, WHITE)
    screen.blit(retry_txt, retry_txt.get_rect(center=retry_rect.center))
    screen.blit(quit_txt, quit_txt.get_rect(center=quit_rect.center))
    
    return retry_rect, quit_rect


while True:
    screen.fill(BG)
    mouse = pygame.mouse.get_pos()
    click = False

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                click = True
        
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z: death_cause = "zombie"
            if event.key == pygame.K_f: death_cause = "fall"

    
    if page == "game-over":
        draw_title("GAME OVER")
        b_retry, b_quit = draw_game_over(death_cause) 

        if click:
            if b_retry.collidepoint(mouse):
                pygame.quit()
                subprocess.run([sys.executable, "JEUX/level1.py"])
                sys.exit()

            if b_quit.collidepoint(mouse):
                pygame.quit()
                sys.exit()

    pygame.display.update()
    clock.tick(60)
