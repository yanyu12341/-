import pygame

from pygame.locals import *

class Plane(pygame.sprite.Sprite):

    def __init__(self,bgsize):

        pygame.sprite.Sprite.__init__(self)
        
        self.active = True
        
        self.image1 = pygame.image.load("未标题-2.png").convert_alpha()
        
        self.image2 = pygame.image.load("未标题-4.png").convert_alpha()
        
        self.image3 = pygame.image.load("成套的全民飞机大站和雷霆战机素材-leitingzhanji_爱给网_aigei_com.png").convert_alpha()
        
        self.rect = self.image1.get_rect()
        
        self.mask = pygame.mask.from_surface(self.image1)
        
        self.width,self.height= bgsize[0],bgsize[1]
        
        self.rect.left = self.width//2-self.rect.width//2
        
        self.rect.top = self.height-60-self.rect.height
        
        self.speed = 10
        
    def moveup(self):
    
        if self.rect.top>0:
        
            self.rect.top -= self.speed
            
        if self.rect.top == 0:
        
            self.rect.top == 0
            
    def movedown(self):
      
        if self.rect.top < self.height- (self.rect.height+60):
        
            self.rect.top += self.speed
            
        if self.rect.top == self.height- (self.rect.height+60): 

            self.rect.top == self.height- (self.rect.height+60)
            
    def moveleft(self):
    
        if self.rect.left > 0:
        
            self.rect.left -= self.speed
        
        if self.rect.left == 0:
        
            self.rect.left == 0
            
    def moveright(self):
    
        if self.rect.left < self.width-self.rect.width:
        
            self.rect.left += self.speed
            
        if self.rect.left == self.width-self.rect.width:
        
            self.rect.left == self.width-self.rect.width


