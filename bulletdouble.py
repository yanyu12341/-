import pygame

import plane

from pygame.locals import *

class bullet(pygame.sprite.Sprite):

    def __init__(self,bgsize,Plane_rect_top,Plane_rect_left,Plane_speed):

        pygame.sprite.Sprite.__init__(self)
        
        self.active = True
        
        self.image1 = pygame.image.load("bulletx2.png").convert_alpha()
        
        self.mask = pygame.mask.from_surface(self.image1)
        
        self.rect = self.image1.get_rect()
        
        self.width,self.height= bgsize[0],bgsize[1]
        
        self.rect.top = Plane_rect_top - 50
        
        self.rect.left = Plane_rect_left
        
        self.speed = Plane_speed + 5
        
    def launch(self):
    
        self.rect.top -= self.speed
        