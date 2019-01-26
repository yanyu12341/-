import pygame

from pygame.locals import *

import sys

from  random import *

import plane

import enemy1

import enemy2

import bullet

import superbullet

import bulletdouble

import enemy1bullet

pygame.init()

pygame.mixer.init()

bgsize = width,height = 640,800

screen = pygame.display.set_mode(bgsize)

pygame.display.set_caption("first game")

bg = pygame.image.load('bg11.jpg').convert()

bg_rect = bg.get_rect()

bg2 = pygame.image.load('bg22.jpg').convert()

bg2_rect = bg2.get_rect()

bg2_rect.top = - bg2_rect.height-(bg_rect.height-height)

bg_rect.top = - (bg_rect.height-height)

gameover = pygame.image.load('gover.png').convert_alpha()

Plane=plane.Plane(bgsize)
 
pygame.mixer.music.load("吉森信 - Gun's & Roses (Paradise Lunch).ogg")

destroyed = [pygame.image.load('1.png').convert_alpha(),\
pygame.image.load('2.png').convert_alpha(),\
pygame.image.load('3.png').convert_alpha(),\
pygame.image.load('4.png').convert_alpha(),\
pygame.image.load('5.png').convert_alpha(),\
pygame.image.load('6.png').convert_alpha()]

destroyed_en1 = [pygame.image.load('1的副本.png').convert_alpha(),\
pygame.image.load('2的副本.png').convert_alpha(),\
pygame.image.load('3的副本.png').convert_alpha(),\
pygame.image.load('4的副本.png').convert_alpha(),\
pygame.image.load('5的副本.png').convert_alpha(),\
pygame.image.load('6的副本.png').convert_alpha()]

playagain = pygame.image.load('再玩一次.png').convert_alpha()
        
def add_bullet(g2):

    bt = bullet.bullet(bgsize,Plane.rect.top,Plane.rect.left,Plane.speed)
    
    g2.add(bt)
    
def add_bulletx2(g2):

    bt = bulletdouble.bullet(bgsize,Plane.rect.top,Plane.rect.left,Plane.speed)
    
    g2.add(bt)
    
def add_en1bullet(g2,en1_rect_top,en1_rect_left,en1_speed):

    bt = enemy1bullet.bullet(bgsize,en1_rect_top,en1_rect_left,en1_speed)
        
    g2.add(bt)
    
def add_spbullet(g2):

    bt = superbullet.bullet(bgsize,Plane.rect.top,Plane.rect.left,Plane.speed)
    
    g2.add(bt)

def add_enemy1(g1,g2,num):#大飞机

    for i in range(num):
    
        e1 = enemy1.enemy1(bgsize)
        
        g1.add(e1)
        
        g2.add(e1)
        
def add_enemy2(g1,g2,num):#小飞机

    for i in range(num):
    
        e2 = enemy2.enemy2(bgsize)
        
        g1.add(e2)
        
        g2.add(e2)

def main():

    score = 0
    
    score_font = pygame.font.Font(None,36)

    runing = True
    
    clock = pygame.time.Clock()
    
    pygame.mixer.music.play()
    
    enemies = pygame.sprite.Group()#所有敌机
    
    enemy1 = pygame.sprite.Group()#敌机1
    
    en1 = add_enemy1(enemies,enemy1,randint(3,5))
    
    enemy2 = pygame.sprite.Group()#敌机2
    
    en2 = add_enemy2(enemies,enemy2,randint(5,10))
    
    bullets = pygame.sprite.Group()#子弹
    
    spbullets = pygame.sprite.Group()#超级子弹
    
    en1bullets = pygame.sprite.Group()
    
    bd = False
    
    en1left = 0
    
    en2left = 0
    
    k = 1#此参数用于将游戏结束后剩余飞机计数删除
    
    delay = 100#延时参数
    
    delay2 =100#延时参数
    
    delay3 =100#延时参数
    
    delay4 =100#延时参数
    
    run = 1
    
    x = 0#延时参数
    
    y = 0#延时参数
    
    num1 = 0
    
    num2 = 0
    
    num3 = 0
    
    level = 0#难度计数

    while runing:
    
        status = 0 
        
        screen.blit(bg,bg_rect)#背景打印
        
        screen.blit(bg2,bg2_rect)
        
        bg_rect.top += 5
        
        bg2_rect.top += 5
        
        print (bg_rect.top)
        
        print (bg2_rect.top)
        
        if bg2_rect.top == height:
            
            bg2_rect.top = - bg2_rect.height-(bg_rect.height-height)
            
        if bg_rect.top == height:
        
            bg_rect.top = - bg2_rect.height-(bg_rect.height-height)
        
        for event in pygame.event.get():
        
            if event.type == QUIT:
            
                pygame.quit()
                
                sys.exit()
                
        score_text = score_font.render("Score:%s"% score,True,(255,255,255))
        
        screen.blit(score_text,(10,5))
                
        bt = bullet.bullet(bgsize,Plane.rect.top,Plane.rect.left,Plane.speed)
                
        key_pressed = pygame.key.get_pressed()
        
        if key_pressed[K_w] or key_pressed[K_UP]: 
        
            Plane.moveup()
            
        if key_pressed[K_s] or key_pressed[K_DOWN]: 
        
            Plane.movedown()
            
        if key_pressed[K_a] or key_pressed[K_LEFT]:
        
            Plane.moveleft()
            
            status = -1
            
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
        
            Plane.moveright()
            
            status = 1
            
        if key_pressed[K_j] or key_pressed[K_SPACE]:
        
            if level < 3:
        
                if not delay % 10:
            
                    add_bullet(bullets)
                
            else:
            
                if not delay % 5:
            
                    add_bulletx2(bullets)
                
            delay -= 1
                
            if delay == 0:
            
                delay == 100
                
                
        if key_pressed[K_p] or key_pressed[K_c]:
        
            if not delay2 % 10:
        
                sp= add_spbullet(spbullets)
                
            delay2 -= 1
                
            if delay2 == 0:
            
                delay2 == 100
            
        
        for each in enemy1:
        
            if each.active:
            
                enemy1.remove(each)
                
                while pygame.sprite.spritecollide(each,enemy1,False,pygame.sprite.collide_mask):
                
                    each.rect.top -= 200
                    
                enemy1.add(each)
            
                screen.blit(each.image1,each.rect)
            
                each.move()
                
                ##敌机生成发射子弹集合
                
                if level > 2:
                
                    if not delay4 % 80:
                
                        add_en1bullet(en1bullets,each.rect.top,each.rect.left,each.speed)
                    
                    delay4 -= 1
                    
                    if delay4 == 0:
                    
                        delay4 = 100
                        
                print ('yesyes')
                    
            else:
            
                each.rect.top += 20
                
                enemy1.remove(each)
                
                while pygame.sprite.spritecollide(each,enemy1,False,pygame.sprite.collide_mask):
                
                    each.rect.top += 20
                
                enemy1.add(each)
            
                screen.blit(destroyed_en1[num1],each.rect)
                
                print ('num1:' + str(num1))
                
                num1 += 1
                
                if num1 == 6:
                
                    num1 = 0
                
                    enemy1.remove(each)
                    
                    if Plane.active:
                    
                        score += 2000 
                    
            
        for each in enemy2:
        
            if each.active:
            
                screen.blit(each.image1,each.rect)
               
                each.move()
                                
            else:
            
                screen.blit(destroyed[num2],each.rect)
                
                num2 += 1
                
                if num2 == 6:
                
                    enemy2.remove(each)
                    
                    if Plane.active:
                    
                        score += 1000
                    
                    num2 = 0
                
        for each in bullets:
        
            screen.blit(each.image1,each.rect)
            
            each.launch()
            
            for it in enemy1:
            
                bd = pygame.sprite.collide_rect(each, it)
                
                if bd:
                
                    it.life -= 1
                    
                    if not it.life:
                
                        it.active = False
                    
                    bullets.remove(each)
                    
            for p in enemy2:
            
                bd2 = pygame.sprite.collide_rect(each, p)
                
                if bd2:
                
                    p.life -= 1
                
                    if not p.life:
                
                        p.active = False
                    
                    bullets.remove(each)
                    
            if each.rect.top < 0:
            
                bullets.remove(each)
                
                
        for each in spbullets:
        
            if each.active:
        
                screen.blit(each.image1,each.rect)
        
                each.launch()
                
            else: 
            
                screen.blit(each.image2[y],each.rect2)
                
                if not(delay3 % 6):
                
                    y += 1
                    
                delay3 -= 1
                
                if delay3 == 0:
            
                    delay3 = 100
                
                print (y)
                
                if y == 3:
                
                    spbullets.remove(each)
                    
                    y = 0
                
                
            for i in enemy1:
        
                bd3 = pygame.sprite.collide_rect(i, each)
                
                if bd3 :
        
                    for p in enemy1:
            
                        p.active = False
                
                    for e in enemy2:
            
                        e.active = False
                        
                    each.active = False
            
            for e in enemy2:
        
                bd4 = pygame.sprite.collide_rect(e, each)
                
                if bd4:
        
                    for p in enemy1:
            
                        p.active = False
                
                    for e in enemy2:
            
                        e.active = False
                        
                    each.active = False
                    
                    
            
        for each in en1bullets:

        
            screen.blit(each.image1,each.rect)
        
            each.launch()
            
             
            bd5 = pygame.sprite.collide_rect(each, Plane)
            
            if bd5:
                
                Plane.active = False
                
            if each.rect.top > height:
            
                en1bullets.remove(each)
                    
                
        ed = pygame.sprite.spritecollide(Plane,enemy1,False,pygame.sprite.collide_mask)
        
        ed2 = pygame.sprite.spritecollide(Plane,enemy2,False,pygame.sprite.collide_mask)
        
        if ed or ed2:
        
            Plane.active = False
            
            for e in enemies:
            
                e.active = False
                    
        if not enemy1 and not enemy2 and Plane.active:
        
            level += 1
        
            enemies = pygame.sprite.Group()#所有敌机
    
            enemy1 = pygame.sprite.Group()#敌机1
    
            en1 = add_enemy1(enemies,enemy1,10)
    
            enemy2 = pygame.sprite.Group()#敌机2
    
            en2 = add_enemy2(enemies,enemy2,randint(10,15))    
            
        if level == 3:
        
            pass
            
        if Plane.active:
        
            if status == 0:
        
                screen.blit(Plane.image1,Plane.rect)
                
            elif status == 1:
            
                screen.blit(Plane.image3,Plane.rect)
                
            elif status == -1:
            
                screen.blit(Plane.image2,Plane.rect)
                
            
        else:
            
            screen.blit(gameover,(0,0))
                
            with open('record.txt','r') as f:
            
                score_recorded = int(f.read())
                
            if score>score_recorded:
            
                with open('record.txt','w') as f:
            
                    f.write(str(score))
                    
            over_text = score_font.render("Best Score: %s"% score_recorded,True,(255,255,255))
            
            screen.blit(over_text,(220,250))
            
            screen.blit(playagain,(250,300))
            
            for i in enemy1:
            
                i.active = False
                
                
            for e in enemy2:
            
                e.active = False
                
            run =0       
                
            if pygame.mouse.get_pressed()[0]:
            
                pos = pygame.mouse.get_pos()
                
                if 250 < pos[0] < 400 and 300 < pos[1] < 375:
                
                    Plane.active = True
                    
                    score = 0
                    
                    level = 0
            
        x += 1
        
        if x == 3:
            
            num3 += 1
            
            x = 0
            
        if num3 == 8:
        
            num3 = 0
    
        pygame.display.update()
        
        pygame.display.flip()
        
        clock.tick(30)
        
if __name__=='__main__':

    main()    
    
    