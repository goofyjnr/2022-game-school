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
ui_group = pygame.sprite.Group()
platforms = pygame.sprite.Group()


#platform object
def platform_spawn():
    for n in range(7):
        platform = Platform((randint(40,WINDOW_WITDTH-40),randint(10,WINDOW_HEIGHT-30)),70,20)
        platform.add(all_sprites,platforms)

    
platform_spawn()

#base platform
platform = Platform((WINDOW_WITDTH/2,WINDOW_HEIGHT),WINDOW_WITDTH,40)
platform.add(all_sprites,platforms)

#player object
player = Player((30,WINDOW_HEIGHT/2),40,40)
player.add(all_sprites, players)
player.vel = Vector2(0,0)

#player health 
player_health_text = Text("Health: " + str(player.health),40,(WINDOW_WITDTH-100,WINDOW_HEIGHT-460),all_sprites, ui_group)

#monster object create 5 monsters 
#in random positions on the right edge of the screen
def monster_spawn():
    for n in range(1):
        new_monster = Monster((WINDOW_WITDTH,randint(0,WINDOW_HEIGHT-35)),30,30)
        new_monster.add(all_sprites, monsters)
        new_monster.vel = Vector2(-randint(3,10),0)

#creats coins placed randomly on the screen
def coins_spawn():
    for n in range(1):
        new_coin = Coin((randint(0,WINDOW_WITDTH-10),randint(0,WINDOW_HEIGHT-20)),30,30)
        new_coin.add(all_sprites,coins)


#score text
score_text = Text("Score: " + str(player.score),40,(WINDOW_WITDTH/2,WINDOW_HEIGHT-460),all_sprites, ui_group)

#pauses the game
def pause():
    paused = True
    pause_text = Text("paused",40,(WINDOW_WITDTH/2,WINDOW_HEIGHT/2),all_sprites, ui_group)
    ui_group.draw(window)
    pygame.display.update()
    
    while paused:
        event = pygame.event.wait()
        if event.type == KEYDOWN:
            if event.key == K_p:
                
                paused = False
                pause_text.kill()

def hits_platform(player,platforms):
    hits_platforms = pygame.sprite.spritecollide(player,platforms,False)
    if len(hits_platforms) != 0 :
        if player.vel.y > 0:
            player.vel.y = 0 
            player.position.y = hits_platforms[0].rect.top+1

def player_offscreen():
    if player.position.x < 0:
        player.vel = Vector2(0,0)
        player.position.x = player.position.x+3       
    if player.position.x > WINDOW_WITDTH:
        player.vel = Vector2(0,0)
        player.position.x = player.position.x-3
    if player.position.y < 0 :
        player.vel = Vector2(0,0)
        player.position.x = player.position.y+3
    if player.position.y > WINDOW_HEIGHT:
        player.vel = Vector2(0,0)
        player.position.x = player.position.y-3



#spawns all initial coins and monsters
for n in range(5):
    monster_spawn()
for n in range(15):
    coins_spawn()




#main game loop
running = True
while running:

    game_clock.tick(FPS)

    #get the events
    events = pygame.event.get()
    
    #loop through all the events
    for event in events:
        #print(event)
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            #if ESC key gets pressed
            if event.key == K_ESCAPE:
                running = False #if the escape key is pressed quit the game.
            elif event.key == K_p:
                pause()
            elif event.key == K_SPACE:
                player.jump()
            elif event.key == K_RIGHT:
                player.move("right")
            elif event.key == K_LEFT:
                player.move("left")
            elif event.key == K_UP:
                player.move("up")
            elif event.key == K_DOWN:
                player.move("down")

    for monster in monsters:
        if not window.get_rect().inflate(100,100).contains(monster.rect):
            monster.kill()
            monster_spawn()
    hit_monster = pygame.sprite.spritecollide(player,monsters,True)
    if len(hit_monster) != 0:
        player.health -= 1
        player_health_text.text = "Health : " + str(player.health)


        monster_spawn()
    hit_coins = pygame.sprite.spritecollide(player,coins,True)
    if len(hit_coins) != 0:
        player.score += 1
        score_text.text ="Score : " + str(player.score)
        
        coins_spawn()
    if player.health == 0:
        gameover_text = Text("Game Over",40,(WINDOW_WITDTH/2,WINDOW_HEIGHT/2),all_sprites, ui_group)
        ui_group.draw(window)
        player.kill()
        pygame.display.update()
        pygame.time.delay(1000)
        running = False

    hits_platform(player,platforms)
    player_offscreen()



    all_sprites.update()
    window.fill(BACKGROUNDCOLOUR)
    for sprite in all_sprites:
        window.blit(sprite.image,sprite.rect)
    
    pygame.display.update()
    

pygame.quit()