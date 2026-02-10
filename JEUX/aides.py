''' 
dessiner un rectangle:
        # Créer un rectangle: rectangle= pygame.Rect(x,y,largeur,hauteur)
        # Le dessiner:        pygame.draw.rect(screen,couleur,rectangle)
        
dessiner un cercle: pygame.draw.circle(screen,couleur, [x, y], rayon)

ajouter du texte:
    #font1 = pygame.font.SysFont(None, 72)
    #txt1 = font1.render('NSI FOR EVER', True, GREY)

ajouter une image:
    # vaisseau=pygame.image.load('vaisseau.png')
    # rect_vaisseau=vaisseau.get_rect()

    Dessiner texte ou image dans la boucle du jeu:
        # texte: screen.blit(txt1,(x,y))
        # image: screen.blit(vaisseau,rect_vaisseau)

Détecter une collision entre deux rectangles (1 et 2), retourne True ou False:
        #  collide = pygame.Rect.colliderect(rectangle1, rectangle2)
    
    '''