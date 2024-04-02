import pygame
import random


#Objects and Object Methods I need to Add
class Base:
    
    xPos = 0
    yPos = 700
    
    def __init__(self,image):
        self.image = image
        
    def movePos(self):
        self.xPos -= 3
        
        
class BG:
    
    xPos = 0
    yPos = -100
    
    def __init__(self,image):
        self.image = image
        
    def movePos(self):
        self.xPos -= 3
        
        
class Bird:
    def __init__(self,image1,image2,image3,x,y):
        self.image1 = image1
        self.image2 = image2
        self.image3 = image3
        self.x = x
        self.y = y

class Pipe:
    def __init__(self,image,x,y):
        self.image = image
        self.x = x
        self.y = y
        



#Initialzing Pygame
WINDOW_X = 600
WINDOW_Y = 800
pygame.init()
win = pygame.display.set_mode((WINDOW_X,WINDOW_Y))
clock = pygame.time.Clock()

pygame.display.set_caption('Flappy Bird') 


#Importing the images needded
baseImage = pygame.transform.scale2x(pygame.image.load("imgs/base.png").convert_alpha())
bgImage = pygame.transform.scale2x(pygame.image.load("imgs/bg.png").convert_alpha())
bird1Image = pygame.transform.scale2x(pygame.image.load("imgs/bird1.png").convert_alpha())
bird2Image = pygame.transform.scale2x(pygame.image.load("imgs/bird2.png").convert_alpha())
bird3Image = pygame.transform.scale2x(pygame.image.load("imgs/bird3.png").convert_alpha())
pipeImage = pygame.transform.scale2x(pygame.image.load("imgs/pipe.png").convert_alpha())

#initializing the objects for later use
bg = BG(bgImage)
base = Base(baseImage)


pygame.display.set_icon(bird1Image)

#The Pygame being ran in while loop below
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False
        
    pygame.Surface.blit(win,bg.image, (bg.xPos,bg.yPos))
    pygame.Surface.blit(win,base.image, (base.xPos,base.yPos))
    pygame.display.flip()
    
    bg.movePos()
    base.movePos()