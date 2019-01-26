import pygame

from pygame.locals import *

import random

from random import *

class enemy2(pygame.sprite.Sprite):

    def __init__(self,bgsize):

        pygame.sprite.Sprite.__init__(self)
        
        self.active = True
        
        self.life = 1
        
        self.image1 = pygame.image.load('en2.png').convert_alpha()
        
        self.mask = pygame.mask.from_surface(self.image1)
        
        self.rect = self.image1.get_rect()
        
        self.width,self.height= bgsize[0],bgsize[1]
        
        self.rect.left = randint(0,self.width-self.rect.width)
        
        self.rect.top =  -self.rect.height-randint(0,1000)
       
        self.speed = randint(10,20)
        
    def move(self):
    
        self.rect.top += self.speed
        
        if self.rect.top > self.height:
        
            print (self.rect)
        
            self.rect.left = randint(0,self.width-self.rect.width)
        
            self.rect.top = -self.rect.height 
            
    
            
            
            