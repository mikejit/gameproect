def play():
    pygame.display.set_caption("Play")

    while True:

        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("This is the play screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = button(image=None, pos=(640, 460), 
                            text_input="BACK", font =get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

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

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen." True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640,260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK= button(image=None, pos=(640,460),
                            text_input="BACK", font =get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

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
        SETTINS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("Red")

        SETTINGS_TEXT = get_font(45).render("This is the SETTINGS screeen.", True, "Black")
        SETTINGS_RECT = SETTINGS_TEXT.get_rect(center=(640,260))
        SCREEN.blit(SETTINGS_TEXT , SETTINGS_RECT)

        SETTINGS_BACK = button(image=None, pos=(640,460), 
                            text_input="BACK", font = get_font(75), base_color="Black", hovering_color="Green")

        SETTINGS_BACK.changeColor(SETTINGS_MOUSE_POS)
        SETTINGS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SETTINGS_BACK.checkForInput(SETTINGS_MOUSE_POS):
                    main_menu()
        pygame.display.update()






    
                             
        



def main_menu():
    pygame.display.set_caption:("Menu")


  while True:
    SCREEN.blit(BG,(0,0))

    MENU_MOUSE_POS = pygame.mouse.get_pos()

    MENU_TEXT = get_font(100).render("MAIN MENU", True, "#FFFFFF")
    MENU_RECT = MENU_TEXT.get_rect(center= (640, 100))

    PLAY_BUTTON = button (image=pygame.image.load=(assests/Play Rect.png), pos=(640, 250),
                        text_input="PLAY", font=get_font(75), base_color = "#d7fcd4", hovering_color="White")
    OPTION_BUTTON = button(image=pygame.image.load=(assests/Options Rect.png), pos=(640, 400),
                        text_input="OPTIONS", font = get_font(75), base_color = "#d7fcd4", hovering_color="White")
    SETTINGS_BUTTON = button(image=pygame.image.load=(assests/Settings Rect.png), pos(640, 550),
                            text_input="SETTINGS", font = get_font(75), base_color = "#d7fcd4", hovering_color="White")
    QUIT_BUTTON = button (image=pygame.image.load=(assests/Quit Rect.png), pos(640,700), 
                        text_input="QUIT", font = get_font(75), base_color = "#d7fcd4", hovering_color="White")

    SCREEN.blit(MENU_TEXT, MENU_RECT)
                            
    for button in [PLAY_BUTTON, OPTIONS_BUTTON, SEETINGS_BUTTON]:
        button.changeColor(MENU_MOUSE_POS)
        button.update(SCREEN)
      
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                play()
            if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                options()
            if SETTINGS_BUTTON.checkForInput(MENU_MOUSE_POS):
                settings()
            if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                pygame.quit()
                sys.exit()
    pygame.display.update()

main_menu()
