import pygame
from config import *
from objects import *

pygame.init()



window = pygame.display.set_mode((WINDOW_WITDTH,WINDOW_HEIGHT))

#create an image object
#picture = Drawable((WINDOW_WITDTH/2,WINDOW_HEIGHT/2),100,100)

#moveing object
moving_object = Physics((0,WINDOW_HEIGHT/2),100,100)
moving_object.vel = Vector2(4,0)


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
    
    moving_object.update()
    window.fill((70,60,78))
    window.blit(moving_object.image,moving_object.rect)
    pygame.display.update()
    

pygame.quit()