import pygame, sys
import subprocess 

pygame.init()
screen = pygame.display.set_mode((1200, 580))
pygame.display.set_caption("Level 2")
font = pygame.font.SysFont("arial", 50, bold=True)
small_font = pygame.font.SysFont("arial", 35)

BG      = (34, 34, 85)  
WHITE   = (255, 255, 255)
YELLOW  = (255, 220, 50)

page = "level"  

def draw_button(text, y):
    """Draw a button and return its rect."""
    label = small_font.render(text, True, BG)
    rect  = pygame.Rect(300, y, 540, 50)
    pygame.draw.rect(screen, WHITE, rect, border_radius=8)
    screen.blit(label, label.get_rect(center=rect.center))
    return rect

def draw_title(text):
    t = font.render(text, True, YELLOW)
    screen.blit(t, t.get_rect(center=(570, 80)))

while True:
    screen.fill(BG)
    mouse = pygame.mouse.get_pos()
    click = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = True


    if page == "level":
        draw_title("LEVEL COMPLETE")
        b_play     = draw_button("Next Level",     200)
        b_settings = draw_button("SETTINGS", 360)
        b_quit     = draw_button("QUIT",     440)

        if click:
            if b_play.collidepoint(mouse):     
                pygame.quit()
                subprocess.run([sys.executable, "casse-brique.py"])
                sys.exit()
            if b_options.collidepoint(mouse):  page = "options"
            if b_settings.collidepoint(mouse): page = "settings"
            if b_quit.collidepoint(mouse):
                pygame.quit(); sys.exit()

    elif page == "play":
        draw_title("PLAY")
        msg = small_font.render("Game goes here!", True, WHITE)
        screen.blit(msg, msg.get_rect(center=(400, 300)))
        b_back = draw_button("BACK", 450)
        if click and b_back.collidepoint(mouse): page = "menu"


    
    elif page == "settings":
        draw_title("SETTINGS")
        msg = small_font.render("Settings go here!", True, WHITE)
        screen.blit(msg, msg.get_rect(center=(400, 300)))
        b_back = draw_button("BACK", 450)
        if click and b_back.collidepoint(mouse): page = "menu"

    pygame.display.update()
