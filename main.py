import pygame
from pygame.locals import *
from config import *
from objects import *

pygame.init()


window = pygame.display.set_mode((WINDOW_WITDTH,WINDOW_HEIGHT))

game_clock = pygame.time.Clock()

#create an image object
#picture = Drawable((WINDOW_WITDTH/2,WINDOW_HEIGHT/2),100,100)

#moveing object
moving_object = Physics((0,WINDOW_HEIGHT/2),100,100)
moving_object.vel = Vector2(20,2)


#main game loop
running = True
while running:

    game_clock.tick(FPS)


    #get the events
    events = pygame.event.get()

    #loop through all the events
    for event in events:
        print(event)
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            #if ESC key gets pressed
            if event.key == K_ESCAPE:
                running = False #if the escape key is pressed quit the game.
    
    moving_object.update()
    window.fill((70,60,78))
    window.blit(moving_object.image,moving_object.rect)
    pygame.display.update()
    

pygame.quit()