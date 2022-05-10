from pygame.sprite import Sprite
from pygame.math import Vector2
from pygame.image import load

class Drawable(Sprite):
    def __init__(self,position, width,height,image):
        super().__init__(self)

        self.position = Vector2(position)
        self.image = load(image)
        self.rect = self.image.get_rect()
    pass

class Physics(Drawable):
    pass

class Player(Physics):
    pass
