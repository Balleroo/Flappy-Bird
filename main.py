import pygame
import random
import neat


"""Flappy Bird Machine Learning Simulator
    Displays a playable Flappy Bird Game, but uses Machine learning to be able to solve the game over time
    Implemented Base, BG, Pipe, and Bird objects to be able to play game
   
   
   Things need to implement:
   -Game Over Screen
   -Main Menu
   -Machine learning 
   -Bird Rotating in middle and not edge(maybe later)
"""

#GLOBAL VARIABLES
WINDOW_X = 600 
WINDOW_Y = 800
clockTicker = 0
JUMPCLOCKGAP = 10
MIDDLE = 376
score = 0

#Objects and Object Methods I need to Add
class Base:
    
    VELOCITY = 3
    BASE_GAP = 481
    WIDTH = 336 * 2
    HEIGHT = 112 * 2
    
    def __init__(self,image,x, y):
        self.image = image
        self.x = x
        self.y = y
    
        
    def movepos(self):
        self.x -= self.VELOCITY
        if self.x < - self.BASE_GAP:
            self.x = self.BASE_GAP
        
    def draw(self,win):
        pygame.Surface.blit(win,self.image, (self.x, self.y))
        
        
class BG:
    WIDTH = 288 * 2
    HEIGHT = 512 * 2
    def __init__(self,image,x,y):
        self.image = image
        self.x = x
        self.y = y
    
    def draw(self,win):
        pygame.Surface.blit(win,self.image, (self.x, self.y))
        
        
class Bird:
    WIDTH = 34 * 2
    HEIGHT = 24 * 2
    
    TICK = 10
    ANIMATION_COUNT = 0
    
    ESCAPE_VEL = 10
    GRAV = 0.5
    
    ROTATE_SPEED = 2.5
    
    def __init__(self,image,x,y):
        self.image = image
        self.x = x
        self.y = y
        self.vel = 1
        self.displacement = 0
    
        self.imgDisp = 1
        self.lastDisp = 2
    
        self.rotation = 25
        self.rotatetime = 0
        
        
        
        
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
            
            
        
        #Speed and displacement update
        self.vel += self.GRAV 
        self.displacement += self.vel
        #Max falling speed determined by Escape veloctiy
        if self.vel > self.ESCAPE_VEL:
            self.vel = self.ESCAPE_VEL
        
        
        
        #Just jumped
        if self.rotatetime > 0:
            self.rotatetime -= 1
        else:
            #Speed and displacement update
            self.rotation -= self.ROTATE_SPEED
            
        #Rotation wil be at max at -90
        if self.rotation < -90:
            self.rotation = -90
            
        self.y = self.displacement + MIDDLE
        
        pygame.Surface.blit(win,pygame.transform.rotate(self.image[self.imgDisp],self.rotation), (self.x, self.y))
    
    def jump(self):
        self.vel = -8
        self.rotation = 25
        self.rotatetime = 25
        
    def get_mask(self):
        return pygame.mask.from_surface(self.image[self.imgDisp])
        
        
        

class Pipe:
    WIDTH = 52 * 2
    HEIGHT = 320 * 2
    VELOCITY = 3
    RANDOM_LOW = -200
    RANDOM_HIGH = 200
    GAP = 400
    
    pipe_passed = 0
    
    def __init__(self,image,x):
        self.image = image
        self.x = x
        self.y = random.randint(self.RANDOM_LOW,self.RANDOM_HIGH)
        
    def draw(self,win):
        
        pygame.Surface.blit(win,pygame.transform.flip(self.image, False, True) , (self.x, self.y - self.GAP))
        pygame.Surface.blit(win,self.image, (self.x, self.y + self.GAP))
        
    def movepos(self):
        self.x -= self.VELOCITY
        if self.x <= - 100:
            self.x = 700 
            self.y = random.randint(self.RANDOM_LOW,self.RANDOM_HIGH)
            self.pipe_passed = 0
    
    def hit(self,bird):
        
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(pygame.transform.flip(self.image, False, True))
        bottom_mask = pygame.mask.from_surface(self.image)
        top_offset = (self.x - bird.x, self.y - self.GAP - round(bird.y))
        bottom_offset = (self.x - bird.x, self.y + self.GAP - round(bird.y))

        b_point = bird_mask.overlap(bottom_mask, bottom_offset)
        t_point = bird_mask.overlap(top_mask,top_offset)

        if b_point or t_point:
            return True

        return False


#Initialzing Pygame
pygame.init()
win = pygame.display.set_mode((WINDOW_X,WINDOW_Y))
my_font = pygame.font.SysFont('Comic Sans MS', 34)
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
bird = Bird(birdImage, 266, MIDDLE)

pipe1 = Pipe(pipeImage,900)

pipe2 = Pipe(pipeImage,1300)

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

    if True in pygame.key.get_pressed():
        if clockTicker == 0:
            bird.jump()
            clockTicker = JUMPCLOCKGAP
            
    if clockTicker > 0:
        clockTicker -= 1
        
    #Bird to Base collison detector
    if bird.y + 48 > 700:
        print("Bird hit Base")
        
    #Bird to Pipe collison detector
    if pipe1.hit(bird):
        print("bird hit pipe1")
    if pipe2.hit(bird):
        print("bird hit pipe2")
    
    if pipe1.x < bird.x and pipe1.pipe_passed == 0:
        score += 1
        pipe1.pipe_passed = 1
    if pipe2.x < bird.x and pipe2.pipe_passed == 0:
        score += 1
        pipe2.pipe_passed = 1
    
    
    #Pipe Printing
    pipe1.draw(win)
    pipe1.movepos()
    pipe2.draw(win)
    pipe2.movepos()

    #Base Printing
    base1.draw(win)
    base1.movepos()
    base2.draw(win)
    base2.movepos()
    
    #Score Printing
    win.blit(my_font.render(f'Score: {score}', False, (255, 255, 255)), (450,0))
    
    pygame.display.flip()