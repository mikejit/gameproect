import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 1200, 580
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Popup Demo")
clock = pygame.time.Clock()

# ── COLORS ────────────────────────────────────────────────────────────────────
WHITE     = (255, 255, 255)
BLACK     = (0, 0, 0)
RED       = (200, 40, 40)
RED_HOVER = (220, 60, 60)
GREEN       = (50, 180, 50)
GREEN_HOVER = (80, 210, 80)
DARK_GRAY = (40, 40, 40)
BG_COLOR  = (70, 90, 110)

# ── FONTS ─────────────────────────────────────────────────────────────────────
font_big   = pygame.font.SysFont("arial", 64, bold=True)
font_small = pygame.font.SysFont("arial", 26)

# ── POPUP FUNCTION ────────────────────────────────────────────────────────────
def draw_popup(state, death_cause=""):
    """
    state       = "game_over" or "win"
    death_cause = "zombie" or "fall"  (only used when state is game_over)
    Returns the retry and quit button rects for click detection.
    """

    # Dark transparent overlay
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 160))
    screen.blit(overlay, (0, 0))

    # Panel
    panel = pygame.Rect(400, 120, 400, 260)
    border_color = GREEN if state == "win" else RED
    pygame.draw.rect(screen, DARK_GRAY, panel, border_radius=14)
    pygame.draw.rect(screen, border_color, panel, 4, border_radius=14)

    # Title
    if state == "win":
        title = font_big.render("YOU WIN!", True, GREEN)
    else:
        title = font_big.render("GAME OVER", True, RED)
    screen.blit(title, title.get_rect(center=(WIDTH // 2, 200)))

    # Subtitle
    if state == "game_over":
        if death_cause == "zombie":
            sub = font_small.render("You were caught by a zombie!", True, WHITE)
        else:
            sub = font_small.render("You fell off the platform!", True, WHITE)
        screen.blit(sub, sub.get_rect(center=(WIDTH // 2, 258)))

    # Buttons
    mouse = pygame.mouse.get_pos()

    retry_rect = pygame.Rect(430, 300, 155, 48)
    quit_rect  = pygame.Rect(620, 300, 155, 48)

    retry_col = GREEN_HOVER if retry_rect.collidepoint(mouse) else GREEN
    quit_col  = RED_HOVER   if quit_rect.collidepoint(mouse)  else RED

    pygame.draw.rect(screen, retry_col, retry_rect, border_radius=8)
    pygame.draw.rect(screen, quit_col,  quit_rect,  border_radius=8)

    retry_label = font_small.render("RETRY", True, WHITE)
    quit_label  = font_small.render("QUIT",  True, WHITE)
    screen.blit(retry_label, retry_label.get_rect(center=retry_rect.center))
    screen.blit(quit_label,  quit_label.get_rect(center=quit_rect.center))

    return retry_rect, quit_rect


# ── TEST SCREEN (simulates your game background) ──────────────────────────────
# This just shows the popup over a placeholder background.
# Replace this section with your actual game loop.

# Press Z to trigger "zombie death", F for "fall death", W for "win"
popup_state  = None   # None = no popup
death_cause  = ""

while True:
    clock.tick(60)
    screen.fill(BG_COLOR)

    # placeholder background text
    hint = font_small.render("Press Z = zombie death   |   F = fall death   |   W = win", True, WHITE)
    screen.blit(hint, hint.get_rect(center=(WIDTH // 2, HEIGHT // 2)))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                popup_state = "game_over"
                death_cause = "zombie"
            if event.key == pygame.K_f:
                popup_state = "game_over"
                death_cause = "fall"
            if event.key == pygame.K_w:
                popup_state = "win"

        if event.type == pygame.MOUSEBUTTONDOWN and popup_state:
            if retry_rect.collidepoint(event.pos):
                popup_state = None   # close popup (plug in your reset() here)
                death_cause = ""
            if quit_rect.collidepoint(event.pos):
                pygame.quit()
                sys.exit()

    # draw popup if active
    if popup_state:
        retry_rect, quit_rect = draw_popup(popup_state, death_cause)

    pygame.display.update()
