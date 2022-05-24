from config import *
from pygame.sprite import Sprite
from pygame.math import Vector2
from pygame.image import load
from pygame.transform import scale
from pygame.font import Font


class Drawable(Sprite):
    def __init__(self,position, width,height,image="assets/chara-1.png"):
        super().__init__()

        self.position = Vector2(position)
        self.image = scale(load(image),(width,height))
        self.image.set_colorkey((181,230,29))
        
        self.rect = self.image.get_rect(midbottom=position)

class Physics(Drawable):
    def __init__(self, position, width, height, image="assets/chara-1.png"):
        super().__init__(position, width, height, image)
        
        self.vel = Vector2((0,0))

    def update(self):
        self.vel += GRAVITY 
        self.vel -=self.vel * FRIC
        self.position += self.vel 
        self.rect.midbottom = self.position 

class Player(Physics):
    def __init__(self, position, width, height, image="assets/chara-1.png"):
        super().__init__(position, width, height, image)
        self.score = 0
        self.health = 3
          
    def move(self,direction):
        if direction == "left":
            self.vel -= MOVE_STRENGTH
        elif direction == "right":
            self.vel += MOVE_STRENGTH
        elif direction =="up":
            self.vel -= LIFT_STRENGTH
        elif direction =="down":
            self.vel += LIFT_STRENGTH

    def jump(self):
        self.vel += JUMP_STRENGTH

class Monster(Physics):
    def __init__(self, position, width, height, image="assets/monster.png"):
        super().__init__(position, width, height, image)
    

    def update(self):
        self.position += self.vel
        self.rect.midbottom = self.position

class Coin(Physics):
    def __init__(self, position, width, height, image="assets/coin.png"):
        super().__init__(position, width, height, image)
    def update(self):
        self.rect.midbottom = self.position

class Text(Sprite):
    def __init__(self, text, size, position, *groups) -> None:
        super().__init__(*groups)
        self.text = text
        self.position = Vector2(position)
        self.font = Font(None,size)
        self.image = self.font.render(self.text,True,TEXTCOLOUR)
        self.image.set_colorkey(BACKGROUNDCOLOUR)
        self.rect = self.image.get_rect(midbottom=position)
    def update(self):
        self.image = self.font.render(self.text,True,TEXTCOLOUR)
        self.rect = self.image.get_rect(midbottom=self.position)