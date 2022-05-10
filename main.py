import pygame
from config import *
from objects import *

pygame.init()



window = pygame.display.set_mode((WINDOW_WITDTH,WINDOW_HEIGHT))


#main game loop
running = True
while running:
    #get the events
    events = pygame.event.get()

    #loop through all the events
    for event in events:
        print(event)
        if event.type == pygame.QUIT:
            running = False
    
    window.fill((70,60,78))
    pygame.display.update()
    




pygame.quit()