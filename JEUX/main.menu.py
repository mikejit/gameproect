def main_menu():
  pygame.display.set_caption:("Menu")

  while True:
    SCREEN.blit(BG,(0,0))

    MENU_MOUSE_POS = pygame.mouse.get_pos()

    MENU_TEXT = get_font(100).render("MAIN MENU", True, #FFFFFF)
    MENU_RECT = MENU_TEXT.get_rect(center= (640, 100))

    PLAY_BUTTON = Button(image=pygame.image.load(assests/Play Rect.png), pos=(640, 250),
                        text_input="PLAY", font=get_font(75), base_color = #d7fcd4, hovering_color="White")
    OPTION_BUTTON = Button(image=pygame.image.load(assests/Options Rect.png), pos=(640, 400),
                        text_input="OPTIONS", font = get_font(75), base_color = #d7fcd4, hovering_color="White")
    SETTINGS_BUTTON = Button(image=pygame.image.load(assests/Settings Rect.png), pos(640, 550),
                            text_input="SETTINGS", font = get_font(75), base_color = #d7fcd4, hovering_color="White")
    QUIT_BUTTON = Button(image=pygame.image.load(assests/Quit Rect.png), pos(640,700), 
                        text_input="QUIT", font = get_font(75), base_color = #d7fcd4, hovering_color="White)

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


