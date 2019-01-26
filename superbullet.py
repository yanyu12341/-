import pygame

import plane

from pygame.locals import *

class bullet(pygame.sprite.Sprite):

    def __init__(self,bgsize,Plane_rect_top,Plane_rect_left,Plane_speed):

        pygame.sprite.Sprite.__init__(self)
        
        self.active = True
        
        self.image1 = pygame.image.load("spb4.png").convert_alpha()
        
        self.image2 = [pygame.image.load("b1.png").convert_alpha(),\
        pygame.image.load("b2.png").convert_alpha(),\
        pygame.image.load("b3.png").convert_alpha()]
        
        self.mask = pygame.mask.from_surface(self.image1)
        
        self.rect = self.image1.get_rect()
        
        self.rect2 = self.image1.get_rect()
        
        self.width,self.height= bgsize[0],bgsize[1]
        
        self.rect.top = Plane_rect_top - 50
        
        self.rect.left = Plane_rect_left+15
        
        self.speed = Plane_speed + 5
        
        self.rect2.left = self.rect.left - 387/2
        
        self.rect2.top = self.rect.top - (442+100)/2
        
    def launch(self):
    
        self.rect.top -= self.speed
        
        self.rect2.top -= self.speed
        