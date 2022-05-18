import pygame
from pygame.locals import *
from config import *
from objects import *
from random import randint

pygame.init()


window = pygame.display.set_mode((WINDOW_WITDTH,WINDOW_HEIGHT))

game_clock = pygame.time.Clock()

#create an image object
#picture = Drawable((WINDOW_WITDTH/2,WINDOW_HEIGHT/2),100,100)

#sprite groups
all_sprites = pygame.sprite.Group()
players = pygame.sprite.Group()
monsters = pygame.sprite.Group()
coins = pygame.sprite.Group()

#player object
player = Player((0,WINDOW_HEIGHT/2),40,40)
player.add(all_sprites, players)
player.vel = Vector2(0,0)

#monster object create 5 monsters 
#in random positions on the right edge of the screen
for n in range(5):
    new_monster = Monster((WINDOW_WITDTH,randint(0,WINDOW_HEIGHT)),30,30)
    new_monster.add(all_sprites, monsters)
    new_monster.vel = Vector2(-randint(1,10),0)

#creats coins placed randomly on the screen
for n in range(10):
    new_coin = Coin((randint(0,WINDOW_WITDTH),randint(0,WINDOW_HEIGHT)),30,30)
    new_coin.add(all_sprites,coins)



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
            elif event.key == K_SPACE:
                player.jump()
            elif event.key == K_RIGHT:
                player.move("right")
            elif event.key == K_LEFT:
                player.move("left")
    
    all_sprites.update()
    window.fill((70,60,78))
    for sprite in all_sprites:
        window.blit(sprite.image,sprite.rect)
    
    pygame.display.update()
    

pygame.quit()