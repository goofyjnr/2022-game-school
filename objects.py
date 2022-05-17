from config import *
from pygame.sprite import Sprite
from pygame.math import Vector2
from pygame.image import load
from pygame.transform import scale


class Drawable(Sprite):
    def __init__(self,position, width,height,image="assets/chara-1.png"):
        super().__init__()

        self.position = Vector2(position)
        self.image = scale(load(image),(width,height))
        
        self.rect = self.image.get_rect(midbottom=position)

class Physics(Drawable):
    def __init__(self, position, width, height, image="assets/chara-1.png"):
        super().__init__(position, width, height, image)
        
        self.vel = Vector2((0,0))

    def update(self):
        self.vel += GRAVITY
        self.position += self.vel 
        self.rect.midbottom = self.position

class Player(Physics):
    def __init__(self, position, width, height, image="assets/chara-1.png"):
        super().__init__(position, width, height, image)
          
    def move(self,direction):
        if direction == "left":
            self.vel -= MOVE_STRENGTH
        elif direction == "right":
            self.vel += MOVE_STRENGTH
        elif direction =="up":
            pass
        elif direction =="down":
            pass


    def jump(self):
        self.vel += JUMP_STRENGTH

class Barrier(Physics):
    pass   

class Platform(Physics):
    pass

