import pygame,random,os
import tkinter as tk
from tkinter import messagebox as mb
pygame.font.init()

#def introscreen():

SCREEN_WIDTH=800
SCREEN_HEIGHT=650
MX=250
#MY=565
MY=480
b=pygame.image.load(os.path.join('wall.png'))
bg=pygame.transform.scale(b,(800,650))
monkey_image1=pygame.image.load(os.path.join('rabbit.png'))
monkey_image2=pygame.transform.scale(monkey_image1,(40,40))
monkey_image3=pygame.transform.flip(monkey_image2,True,False)
dead_monkey1=pygame.image.load(os.path.join('dead_rabbit.png'))
dead_monkey2=pygame.transform.scale(dead_monkey1,(80,80))
current_monkey=monkey_image2
sword_image1=pygame.image.load(os.path.join('carrot.png'))
sword_image2=pygame.transform.scale(sword_image1,(25,15))
sword_image3=pygame.transform.flip(sword_image2,True,False)
current_sword=sword_image2
sword_position=MX+monkey_image2.get_width()
turtle_image1=pygame.image.load(os.path.join('turtle_melee.png'))
turtle_image2=pygame.transform.scale(turtle_image1,(40,30))
turtle_image3=pygame.transform.flip(turtle_image2,True,False)
turtleran_image1=pygame.image.load(os.path.join('turtle_range.png'))
turtleran_image2=pygame.transform.scale(turtleran_image1,(40,30))
turtleran_image3=pygame.transform.flip(turtleran_image2,True,False)
door_image1=pygame.image.load(os.path.join('door.png'))
door_exit=pygame.transform.scale(door_image1,(60,80))
door_entery=pygame.transform.flip(door_exit,True,False)
#
class monkey(pygame.sprite.Sprite):
    def __init__(self):
        self.x=MX
        self.y=MY
        self.img=current_monkey
        self.hitbox=self.img.get_rect()
        self.sword=current_sword
        self.swordpos=sword_position
        self.swordbox=self.sword.get_rect()
    def draw(self):
        WIN.blit(self.img,(self.x,self.y))
        self.hitbox.topleft = (self.x, self.y)
    def bite(self):
        WIN.blit(self.sword,(self.swordpos,self.y+self.sword.get_height()/2+10))
#
class platform():
    def __init__(self,x,ymult,length):
        self.height=10
        self.length=length
        self.x=x
        self.y=ymult*80
        self.color=(134,89,45)
        self.Rect=pygame.Rect(self.x,self.y,self.length,self.height)

    def draw(self):
        p=pygame.draw.rect(WIN,(60,60,60),self.Rect)
        return p
    def collision(self):
        global isjump,fall,MY,MX,midjump
        #stubedtoeonacorner
        if MX <=self.x+VEL:
            if self.Rect.colliderect(monkey_rect):
                MX-=VEL
        elif MX>=self.x+self.length-VEL:
            if self.Rect.colliderect(monkey_rect):
                MX+=VEL
        #tellmeareyourereal
        if  self.Rect.colliderect(monkey_rect):
            if midjump==True:
                isjump=False
                midjump=False
            if MY>=self.y-8:
                fall=True
            elif MY<self.y:
                MY=self.y-current_monkey.get_height()+1
                fall=False


class wall():
    def __init__(self,x,ymult):
        self.width=15
        self.height=90
        self.y=80*(ymult-1)+5
        self.x=x
        self.rect=pygame.Rect(self.x,self.y,self.width,self.height)
    def draw(self):
        pygame.draw.rect(WIN,(60,60,60),self.rect)
    def collision(self):
        global MX
        if self.rect.colliderect(monkey_rect):
            if MX<=self.x+5:
                MX-=VEL
            elif MX>self.x+6:
                MX+=VEL
class ammunition():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.lim=bullet_limit
        self.distance=0
    def draw(self):
        p=pygame.draw.rect(WIN,(0,0,255),(self.x,self.y,10,5))
        return p
class turtle(pygame.sprite.Sprite):
    def __init__(self,type_,x,y,distance,freq=0):
        self.x=x
        self.y=y*80-25
        self.type=type_
        if type_==1:
            self.img1=turtle_image2
            self.img2=turtle_image3
        elif type_ ==2:
            self.img1=turtleran_image2
            self.img2=turtleran_image3
        self.freq=freq
        self.freqcount=0
        self.start=0
        if self.start==0:
            self.curimg=self.img1
            self.startx=self.x
            self.direct=0
        self.hitbox=self.curimg.get_rect()
        self.lent=self.curimg.get_height()
        self.widt=self.curimg.get_width()
        self.health=turtle_health
        self.distance=distance
        self.alert=True
        self.trigcheck=0
        self.subtrigcheck=0
        self.trigger=pygame.Rect(self.x+self.curimg.get_width(),self.y+self.curimg.get_height()-80,self.distance,80)
        self.headbutt=0
        self.stopcharge=0
    def draw(self):
        WIN.blit(self.curimg,(self.x,self.y))
    def movement(self):
        start=self.startx
        end=self.startx+self.distance
        if self.start==0:
            self.x=random.randint(start,end)
        if self.x<=start:
            self.curimg=self.img1
            self.direct=0
        elif self.x>=end:
            self.curimg=self.img2
            self.direct=1
        if self.direct==0:
            self.x+=turtVEL
            self.trigger=pygame.Rect(self.x+self.curimg.get_width(),self.y+self.curimg.get_height()-70,self.distance,65)
        elif self.direct==1:
            self.x-=turtVEL
            self.trigger=pygame.Rect(self.x-self.distance,self.y+self.curimg.get_height()-70,self.distance,65)
    
    def action(self):
        global shoal,turtle_armouryL,turtle_armouryR,monkey_health
        if self.start==0:
            self.start=1
        if swordout !=0:
            turt_rect = pygame.Rect(self.x, self.y, self.widt, self.lent)
            if sword_rect.colliderect(turt_rect):
                self.health-=1
                pygame.draw.rect(WIN,(255,255,255),(self.x,self.y,self.widt,self.lent))
                if self.health<=0:
                    shoal.remove(self)
        if self.type==2:
            if self.trigger.colliderect(monkey_rect):
                self.alert=False
                if self.freq!=self.freqcount:
                    self.freqcount+=1
                elif self.direct==0:
                    self.freqcount=0
                    turtle_armouryR.append(ammunition(self.x+self.curimg.get_width(),self.y+self.curimg.get_height()/2))
                elif self.direct==1:
                    self.freqcount=0
                    turtle_armouryL.append(ammunition(self.x,self.y+self.curimg.get_height()/2))
                self.subtrigcheck=1
            elif self.subtrigcheck==1:
                if self.direct==0:
                    self.direct=1
                elif self.direct==1:
                    self.direct=0
                self.trigcheck+=1
            if self.trigcheck==50:
                self.alert=True
                self.trigcheck=0
                self.subtrigcheck=0
                self.freqcount=0
        elif self.type==1:
            if self.trigger.colliderect(monkey_rect):
                self.alert=False
                p=pygame.Rect(self.x+10,self.y,self.curimg.get_width(),self.curimg.get_height())
                #pygame.draw.rect(WIN,(255,0,5),p)
                if self.stopcharge==0:
                    if p.colliderect(monkey_rect)==False:
                        if self.direct==0:
                            self.x+=ammoVEL
                        elif self.direct==1:
                            self.x-=ammoVEL
                    else:
                        monkey_health-=1
                        self.headbutt=1
            if self.headbutt==1:
                if self.direct==0:
                    self.x-=20
                elif self.direct==1:
                    self.x+=20
                self.stopcharge+=1
            if self.stopcharge==prechargepause:
                self.headbutt=0
                self.stopcharge=0
                

#
def level(planks=[],boards=[],shoal=[],exit_door_x=SCREEN_WIDTH-door_exit.get_width(),
          exit_door_y=80-door_exit.get_height(),VEL=5,turtVEL=2,ammoVEL=8,jumpcount=8,
          swordtime=5,monkey_health=10,turtle_health=3*5# 5 is value of swordtime
          ,bullet_limit=500,bullet_freq=10,prechargepause=15,LOWLEV=8):
    #maindef
    global b,bg,monkey_image1,monkey_image2,monkey_image3,MX,MY,SCREEN_HEIGHT,SCREEN_WIDTH
    global dead_monkey1,dead_monkey2,current_monkey,sword_image1,sword_image2,sword_image3
    global current_sword,sword_position,turtle_image1,turtle_image2,turtle_image3,WIN
    global turtleran_image1,turtleran_image2,turtleran_image3,door_image1,door_exit,door_entery
    pygame.display.set_caption('revenge of the rabbit')
    print(SCREEN_HEIGHT,SCREEN_HEIGHT)
    WIN=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    #minordef
    global FPS,RUN,isjump,ogjump,swordout,sworddelay,turtle_armouryL,turtle_armouryR
    global entry_doorx,entry_doory,fall,midjump,cat
    FPS=60
    RUN=True
    isjump=False
    ogjump=jumpcount
    swordout=0
    sworddelay=0
    turtle_armouryL=[]
    turtle_armouryR=[]  
    base=platform(0,8,SCREEN_WIDTH)
    #planks=[platform(300,6,150),platform(200,3,150),platform(200,5,150),platform(250,4,150),platform(300,2,200),platform(329,1,450)]
    planks.insert(0,base)
    #boards=[wall(300,8)]
    #shoal=[turtle(2,200,5,150,40),turtle(2,300,6,100,30),turtle(1,500,8,100,50)]
    #exit_door_x=SCREEN_WIDTH-door_exit.get_width()
    #exit_door_y=80-door_exit.get_height()
    entry_doorx=MX
    entry_doory=MY
    fall=True
    midjump=False
    curwood_x=0
    curwood_y=0
    curwood_len=0
    cat=0
    global_vars = locals() 
    globals().update(global_vars)
    while RUN:
        pygame.time.Clock().tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
    #controls
        if MX<=0:
            MX+=VEL
        if MX>=SCREEN_WIDTH-current_monkey.get_width():
            MX-+VEL
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            if MX>=SCREEN_WIDTH-monkey_image2.get_width():
                pass
            else:
                current_monkey=monkey_image2
                current_sword=sword_image2
                sword_position=MX+monkey_image2.get_width()
                MX+=VEL
        if keys[pygame.K_a]:
            if MX<=0:
                pass
            else:
                current_monkey=monkey_image3
                current_sword=sword_image3
                sword_position=MX-current_sword.get_width()
                MX-=VEL
        if keys[pygame.K_w]and fall==False:
                isjump = True
                midjump=True
        if (isjump):
            if jumpcount>= -8:
                neg = 1
                if jumpcount < 0:
                    neg = -1 
                MY-=(jumpcount**2)/2*neg 
                jumpcount -=1
            else:
                isjump = False
                jumpcount = 8
                midjump=False
        if sworddelay>swordtime*3:
            if keys[pygame.K_SPACE]:
                swordout=swordtime
        


    #
        final_monkey=monkey()
        #WIN.fill((0,0,0))
        WIN.blit(bg,(0,0))
        exit_rect=pygame.Rect(SCREEN_WIDTH-door_exit.get_width()/2,exit_door_y,door_exit.get_width(),door_exit.get_height())
        exit_door=WIN.blit(door_entery,(entry_doorx,entry_doory))
        exit_door=WIN.blit(door_exit,(exit_door_x,exit_door_y))
        final_monkey.draw()
        monkey_rect = pygame.Rect(MX,MY,monkey_image2.get_width(),monkey_image2.get_height())
        sword_rect = pygame.Rect(final_monkey.swordpos, MY + final_monkey.sword.get_height() / 2 +10, sword_image2.get_width(), sword_image2.get_height())

    #solids
        for board in boards:
            board.draw()
            board.collision()   
        cat=0 
        for wood in planks:
            p=wood.draw()
            wood.collision()
            if wood.Rect.colliderect(monkey_rect) :
                curwood_x=wood.x
                curwood_y=wood.y
                curwood_len=wood.length
                cat=1
        if cat==0 and isjump==False:
            fall=True
        
        #print(MX,curwood_x,curwood_len)
        #print(MY+current_monkey.get_height(),curwood_y)

    #nolightsaber
        for turt in shoal: 
            if turt.alert==True:
                turt.movement()
            turt.draw()
            #pygame.draw.rect(WIN,(255,0,255),turt.trigger)
            turt.action()
    #pewpew
        for ammo in turtle_armouryL:
            p=ammo.draw()
            ammo.x-=ammoVEL
            ammo.distance+=ammoVEL
            if ammo.distance>=ammo.lim:
                turtle_armouryL.remove(ammo)
            elif p.colliderect(monkey_rect):
                monkey_health-=1
                turtle_armouryL.remove(ammo)
        for ammo in turtle_armouryR:
            p=ammo.draw()
            ammo.x+=ammoVEL
            ammo.distance+=ammoVEL
            if ammo.distance>=ammo.lim:
                turtle_armouryR.remove(ammo)
            elif p.colliderect(monkey_rect):
                monkey_health-=1
                turtle_armouryR.remove(ammo)
    #ohnogravity

        if MY>80*LOWLEV-current_monkey.get_height()-2:
            #MY=80*LOWLEV-current_monkey.get_height()-1
            fall=False
    
        if fall==True and MY<80*LOWLEV-current_monkey.get_height()-1 :
            MY+=VEL
        
    #monkeygone
        if monkey_health<=0:
            current_monkey=dead_monkey2
            monkey_rect=pygame.Rect(MX,MY,monkey_image2.get_width()+20,monkey_image2.get_height()+20)
            pygame.draw.rect(WIN,(136,136,136),monkey_rect)
            final_monkey=monkey()
            final_monkey.draw()
            pygame.display.update()
            pygame.time.delay(3000)
            RUN=False
    #completion
        if exit_rect.colliderect(monkey_rect) and swordout==True:
            pygame.time.delay(1000)
            WIN.fill((255,255,255))
            pygame.display.update()
            pygame.time.delay(1000)
            RUN=False
    #holdingoutacarrotrequierseffort
        if swordout!=0:
            sworddelay=0
            swordout-=1
            final_monkey.bite()
        else:
            sworddelay+=1
        if isjump==False and jumpcount!=ogjump:
            jumpcount=ogjump
    #killeveryone and replaceemwithclones
        pygame.display.update()
    pygame.quit()
level([platform(300,6,150),platform(200,3,150),platform(200,5,150),platform(250,4,150),platform(300,2,200),platform(329,1,450)],
      [wall(300,8)],
      [turtle(2,200,5,150,40),turtle(2,300,6,100,30),turtle(1,500,8,100,50)],
      SCREEN_WIDTH-door_exit.get_width(),
      80-door_exit.get_height()) 