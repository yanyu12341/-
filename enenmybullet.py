import pygame

import plane

from pygame.locals import *

class bullet(pygame.sprite.Sprite):

    def __init__(self,bgsize,enemy1_rect_top,enemy1_rect_left,enemy1_speed):

        pygame.sprite.Sprite.__init__(self)
        
        self.active = True
        
        self.image1 = pygame.image.load("enemybullet.png").convert_alpha()
        
        self.image2 = pygame.image.load("792284025d5323e7f42de76bc43251e2.png").convert_alpha()
        
        self.mask = pygame.mask.from_surface(self.image1)
        
        self.rect = self.image1.get_rect()
        
        self.width,self.height= bgsize[0],bgsize[1]
        
        self.rect.top = enemy1_rect_top + 50
        
        self.rect.left = enemy1_rect_left + 15
        
        self.speed = enemy1_speed + 5
        
    def launch(self):
    
        self.rect.top += self.speed
        