##Untitled Game made by Alex and Rowitt @ 2022 V. 0.0.1
## Origin: 10/30/2022

import pygame

## My beloved game loop that **MUST** always remain true.
demonology = True

pygame.init()
pygame.display.set_caption('thecouncil-game')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((800,400))

while demonology:
    for event in pygame.event.get():    ## Here I'm using a for loop to check for any player events
        if event.type == pygame.QUIT:   ## That warrants the game quitting, allows player to exit game
            pygame.quit()
    # all engine and core code
    # updates everything
    pygame.display.update()