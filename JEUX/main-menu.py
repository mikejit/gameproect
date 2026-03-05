import pygame, sys
from button import Button

pygame.init()

screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("MENU")

BG = pygame.image.load("assets/Background.png")

def get_font(size):
    any


def play():
    pygame.display.set_caption("Play")

    while True:

        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("black")

        PLAY_TEXT = get_font(45).render("This is the play screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect
        screen.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font =get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(screen)

        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def options():
    pygame.display.set_caption("Options")

    while True: 
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the play screen.", True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640,260))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK= Button(image=None, pos=(640,460),
                            text_input="BACK", font =get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.qui()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def settings():
    pygame.display.set_caption("Settings")

    while True: 
        SETTINGS_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("Red")

        SETTINGS_TEXT = get_font(45).render("This is the SETTINGS screeen.", True, "Black")
        SETTINGS_RECT = SETTINGS_TEXT.get_rect(center=(640,260))
        screen.blit(SETTINGS_TEXT , SETTINGS_RECT)

        SETTINGS_BACK = Button(image=None, pos=(640,460), 
                            text_input="BACK", font = get_font(75), base_color="Black", hovering_color="Green")

        SETTINGS_BACK.changeColor(SETTINGS_MOUSE_POS)
        SETTINGS_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SETTINGS_BACK.checkForInput(SETTINGS_MOUSE_POS):
                    main_menu()
        pygame.display.update()





def main_menu():
    pygame.display.set_caption


    while True:
        screen.blit(BG,(0,0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#FFFFFF")
        MENU_RECT = MENU_TEXT.get_rect(center= (640, 100))

        PLAY_BUTTON = Button(image = pygame.image.load("assets/Play Rect.png"), pos=(640,250),
                             text_input="PLAY", font= get_font(75), base_color= "##d7fcd4", hovering_color="White" )
        
        OPTION_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640,400),
                               text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hoverinf_color="White")
        SETTINGS_BUTTON = Button(image=pygame.image.load("assets/Settings Rect.png"), pos=(640,400),
                               text_input="SETTINGS", font=get_font(75), base_color="#d7fcd4", hoverinf_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640,400),
                               text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hoverinf_color="White")
        screen.blit(MENU_TEXT, MENU_RECT)
                            
        for button in [PLAY_BUTTON, OPTION_BUTTON, SETTINGS_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
      
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTION_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if SETTINGS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    settings()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                sys.exit()
        pygame.display.update()

main_menu()
