import random as rdm

# Quelques couleurs...
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
RED = (255, 0, 0)
GREEN=(0, 255, 0)
BLUE=(0, 0, 255)
BROWN=(102,51,0)
SKYBLUE=(153,204,255)
DarkSlateGray=(47, 79, 79)


# Initialisation de la hauteur et la largeur de l´écran  
W = 1020
H = 480
size = [W, H]





def randcol():
    '''crée un tuple de trois valeurs comprises entre 0 et 255'''
    return (rdm.randint(0,255),rdm.randint(0,255),rdm.randint(0,255)) 




 
