import pygame
import random


#Objects and Object Methods I need to Add
class Base:
    
    VELOCITY = 3
    BASE_GAP = 481
    HEIGHT = 700
    
    def __init__(self,image,x, y):
        self.image = image
        self.x = x
        self.y = y
        
    def movePos(self):
        self.x -= self.VELOCITY
        if self.x < - self.BASE_GAP:
            self.x = self.BASE_GAP
        
    def draw(self,win):
        pygame.Surface.blit(win,self.image, (self.x, self.y))
        
class BG:
    def __init__(self,image,x,y):
        self.image = image
        self.x = x
        self.y = y
    
    def draw(self,win):
        pygame.Surface.blit(win,self.image, (self.x, self.y))
        
        
class Bird:
    
    TICK = 10
    WIDTH = 266
    ANIMATION_COUNT = 0
    imgDisp = 1
    lastDisp = 2
    
    def __init__(self,image,x,y):
        self.image = image
        self.x = x
        self.y = y
        
    def draw(self,win):
        
        self.ANIMATION_COUNT += 1
        if self.ANIMATION_COUNT % self.TICK == 0:    
            if self.imgDisp == 1 and self.lastDisp == 2:
                self.lastDisp = self.imgDisp
                self.imgDisp = 0
            elif self.imgDisp == 0 and self.lastDisp == 1:
                self.lastDisp = self.imgDisp
                self.imgDisp = 1
            elif self.imgDisp == 1 and self.lastDisp == 0:
                self.lastDisp = self.imgDisp
                self.imgDisp = 2
            elif self.imgDisp == 2 and self.lastDisp == 1:
                self.lastDisp = self.imgDisp
                self.imgDisp = 1
            
                
        pygame.Surface.blit(win,self.image[self.imgDisp], (self.x, self.y))
        
        

class Pipe:
    
    def __init__(self,image,x,y):
        self.image = image
        self.x = x
        self.y = y
        
    def draw(self,win):
        
        pygame.Surface.blit(win,self.image, (self.x, self.y))
        pygame.Surface.blit(win,self.image, (self.x, self.y))
        



#Initialzing Pygame
WINDOW_X = 600  #600
WINDOW_Y = 800  #800
pygame.init()
win = pygame.display.set_mode((WINDOW_X,WINDOW_Y))
clock = pygame.time.Clock()

pygame.display.set_caption('Flappy Bird')


#Importing the images needded
baseImage = pygame.transform.scale2x(pygame.image.load("imgs/base.png").convert_alpha())
bgImage = pygame.transform.scale(pygame.image.load("imgs/bg.png").convert_alpha(), (600, 900))

birdImage = [0,0,0]
for i in range(1,4):
    birdImage[i-1] = pygame.transform.scale2x(pygame.image.load(f"imgs/bird{i}.png").convert_alpha())

pipeImage = pygame.transform.scale2x(pygame.image.load("imgs/pipe.png").convert_alpha())


#initializing the objects for later use
bg = BG(bgImage, 00, -100)
base1 = Base(baseImage, 0, 700)
base2 = Base(baseImage, 481,  700)
bird = Bird(birdImage, 266, 376)
pipe = Pipe(pipeImage)

#The Pygame being ran in while loop below
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False
        
    #Background Printing
    bg.draw(win)

            
    #Bird Printing
    bird.draw(win)

    #Pipe Printing
    #pipe.draw(win)


    #Base Printing
    base1.draw(win)
    base1.movePos()
    base2.draw(win)
    base2.movePos()
    
    pygame.display.flip()