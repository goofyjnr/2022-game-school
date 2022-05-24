
from pygame import Vector2


#game window
WINDOW_WITDTH = 910
WINDOW_HEIGHT = 520

#colours
BACKGROUNDCOLOUR = (70,60,78)
TEXTCOLOUR = (255,255,255)

#Frames per second
FPS = 30

#game world physics
GRAVITY = Vector2(0,0)
FRIC = 0.08 #Friction


#player stuff
JUMP_STRENGTH = Vector2(0,-10)
MOVE_STRENGTH =  Vector2(5,0)
LIFT_STRENGTH = Vector2(0,5)
