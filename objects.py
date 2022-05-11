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
        self.position += self.vel 
        self.rect.midbottom = self.position

class Player(Physics):
    pass
