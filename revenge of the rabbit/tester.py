import pygame,random,os,time
import tkinter as tk
from tkinter import messagebox as mb
pygame.font.init()
def introscreen():
    def button(win,x,y,text,color,command):
        but=tk.Button(win,width=8,height=4,text=text,bg=color,command=command)
        but.place(x=x,y=y)
    def end():
        global win_
        win_.destroy()
    global win_
    win_=tk.Tk()
    win_.geometry('800x650')
    win_.configure(bg='grey')
    win_.attributes('-topmost',True)
    bg=tk.PhotoImage(file='beta_menu_.png')
    background=tk.Label(win_,image=bg)
    background.place(x=-2,y=-2)
    button(win_,450,420,'begin','grey',end)
    win_.mainloop()
    mb.showinfo('introduction','welcome to revenge of the rabbit,\nthis is a beta version of the game and may have some bugs.\nplease contact neil and inform him of said bugs so the game can be improved.\nalso note this is a stripped version of the game and only consists of one level.the game may open in your taskbar instead of over your other overlays. Enjoy')
    mb.showinfo('controls',"'w': is jump\n'a': is left\n'd': is right\nspacebar: attack\nspacebar+left control for ranged attack\nto complete the game kill all the turtles and hit the exit door")
#introscreen()
SCREEN_WIDTH=1000
SCREEN_HEIGHT=650
pygame.display.set_caption('revenge of the rabbit')
icon = pygame.image.load("rabbit.png")
pygame.display.set_icon(icon)
WIN=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
MX=750
MY=80*3+10
b=pygame.image.load(os.path.join('wall.png'))
bg=pygame.transform.scale(b,(SCREEN_WIDTH,SCREEN_HEIGHT))
monkey_image1=pygame.image.load(os.path.join('rabbit.png'))
monkey_image2=pygame.transform.scale(monkey_image1,(40,40))
monkey_image3=pygame.transform.flip(monkey_image2,True,False)
dead_monkey1=pygame.image.load(os.path.join('dead_rabbit.png'))
dead_monkey2=pygame.transform.scale(dead_monkey1,(80,80))
current_monkey=monkey_image2
sword_image1=pygame.image.load(os.path.join('carrot.png'))
sword_image2=pygame.transform.scale(sword_image1,(45,15))
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
heart=pygame.image.load(os.path.join('heart.png'))
heartpow=pygame.transform.scale(heart,(35,35))
health=pygame.transform.scale(heart,(25,25))
carrotpo=pygame.transform.scale(sword_image1,(35,25))
carrotpow=pygame.transform.rotate(carrotpo,270)
carroticon=pygame.transform.rotate(sword_image1,270)
class carrotvel():
    def __init__(self,x,y,img,lim=0):
        self.x=x
        self.y=y
        self.lim=lim
        self.limtest=lim
        self.img=img
        self.rect=pygame.Rect(self.x,self.y,self.img.get_width(),self.img.get_height())
    def draw(self):
        WIN.blit(self.img,(self.x,self.y))
        self.rect=pygame.Rect(self.x,self.y,self.img.get_width(),self.img.get_height())
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
    def nunchuks(self):
        global maxcarrot,carrotbelt
        if carrotstorageR==[]:
            if current_monkey==monkey_image2:
                carrotstorageR.append(carrotvel(self.x+self.img.get_width(),self.y-self.img.get_height()/2+35,sword_image2))
                carrotstorageR[0].lim+=100
                maxcarrot-=1
                carrotbelt.pop()
        if carrotstorageL==[]:
            if current_monkey==monkey_image3:
                carrotstorageL.append(carrotvel(self.x,self.y-self.img.get_height()/2+35,sword_image3))
                carrotstorageL[0].lim-=100
                maxcarrot-=1
                carrotbelt.pop()
class platform():
    def __init__(self,x,ymult,length,overlap=False):
        self.height=10
        self.length=length
        self.x=x
        self.y=ymult*80
        self.color=(134,89,45)
        self.Rect=pygame.Rect(self.x,self.y,self.length,self.height)
        self.overlap=overlap
    def draw(self):
        p=pygame.draw.rect(WIN,(60,60,60),self.Rect)
        if self.x!=0 and self.overlap==False:
            q=pygame.draw.rect(WIN,(0,102,0),(self.x,self.y,current_monkey.get_width(),self.height))
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
        self.height=89
        self.y=80*(ymult-1)+1
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
    def __init__(self,type_,x,y,distance,range_,freq=20):
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
        self.lent=self.curimg.get_height()
        self.widt=self.curimg.get_width()
        self.health=turtle_health
        self.distance=distance
        self.alert=True
        self.trigcheck=0
        self.subtrigcheck=0
        self.range=range_
        self.trigger=pygame.Rect(self.x+self.curimg.get_width(),self.y+self.curimg.get_height()-80,self.range,80)
        self.headbutt=0
        self.stopcharge=0
    def draw(self):
        WIN.blit(self.curimg,(self.x,self.y))
        self.hitbox=pygame.Rect(self.x,self.y,self.curimg.get_width(),self.curimg.get_height())
        self.rect=pygame.Rect(self.x, self.y, self.widt, self.lent)
        if self.health<=0:
            shoal.remove(self)
    def movement(self):
        start=self.startx
        end=self.startx+self.distance-self.curimg.get_width()
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
            self.trigger=pygame.Rect(self.x+self.curimg.get_width(),self.y+self.curimg.get_height()-70,self.range,65)
        elif self.direct==1:
            self.x-=turtVEL
            self.trigger=pygame.Rect(self.x-self.range,self.y+self.curimg.get_height()-70,self.range,65)
    def action(self):
        global shoal,turtle_armouryL,turtle_armouryR,monkey_health,healthbar
        if self.start==0:
            self.start=1
        if swordout !=0:
            turt_rect = pygame.Rect(self.x, self.y, self.widt, self.lent)
            if sword_rect.colliderect(turt_rect):
                self.health-=1
                pygame.draw.rect(WIN,(255,255,255),(self.x,self.y,self.widt,self.lent))
                if self.health<=0 and self in shoal:
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
                        healthbar.pop()
                        pygame.draw.rect(WIN,(200,0,0),monkey_rect )
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
class healthpowerup():
    def __init__(self,x,ymult):
        self.x=x
        self.y=ymult*80-40
        self.rect=pygame.Rect(self.x,self.y,heartpow.get_width(),heartpow.get_height())
    def draw(self):
        WIN.blit(heartpow,(self.x,self.y))
    def restore(self):
        global monkey_health,healthbar,heartpower
        if self.rect.colliderect(monkey_rect):
            if len(healthbar)<monkeyhealth:
                monkey_health+=1
                healthbar.append(health)
                heartpower.remove(self)
class carrotrestock():
    def __init__(self,x,ymult):
        self.x=x
        self.y=ymult*80-40
        self.rect=pygame.Rect(self.x,self.y,carrotpow.get_width(),carrotpow.get_height())
    def draw(self):
        WIN.blit(carrotpow,(self.x,self.y))
    def resupply(self):
        global maxcarrot,maxxcarrot,carrotbelt
        if self.rect.colliderect(monkey_rect):
            if len(carrotbelt)<maxxcarrot:
                maxcarrot+=1
                carrotbelt.append(carroticon)
                carrotbox.remove(self)
VEL=5
turtVEL=2
ammoVEL=8
FPS=60
RUN=True
isjump=False
jumpcount=8
ogjump=jumpcount
swordout=0
sworddelay=0
swordtime=5
monkey_health=5
monkeyhealth=monkey_health
healthbar=[]
for i in range(monkey_health):
    healthbar.append(health)
carrotbelt=[]
maxcarrot=5
maxxcarrot=maxcarrot
for i in range(maxcarrot):
    carrotbelt.append(carroticon)
carrotstorageL=[]
carrotstorageR=[]
turtle_health=3*swordtime
turtle_armouryL=[]
turtle_armouryR=[]
bullet_limit=500
bullet_freq=10
prechargepause=15
LOWLEV=8
base=platform(0,LOWLEV,SCREEN_WIDTH)
planks=[base,platform(600,4,400),platform(500,6,400,True),platform(500,5,100,True),platform(940,7,60),
        platform(50,7,150),platform(100,6,50),platform(50,5,40),platform(0,4,50),platform(125,4,300),
        platform(0,3,50),platform(100,2,200),platform(300,1,900),platform(300,3,600),
        platform(160,3,50,True),platform(0,1,200),platform(250,6,300),platform(425,5,75)]
boards=[wall(500,4),wall(500,5),wall(500,6),wall(990,5),wall(990,6),wall(990,7),wall(200,8),wall(150,6),
        wall(150,5),wall(150,3),wall(300,2)]
shoal=[turtle(1,0,8,200,100,20),turtle(2,0,1,200,500),turtle(1,400,1,600,300),turtle(2,300,3,200,400),
       turtle(1,150,4,250,100),turtle(1,525,6,375,100),turtle(2,225,8,350,300),turtle(2,600,8,400,300),
       turtle(2,250,6,250,200)]
heartpower=[healthpowerup(150,8),healthpowerup(250,2),healthpowerup(450,5)]
carrotbox=[carrotrestock(175,3),carrotrestock(10,4),carrotrestock(960,7)]
exit_door_x=SCREEN_WIDTH-door_exit.get_width()
exit_door_y=80-door_exit.get_height()
entry_doorx=MX
entry_doory=MY
fall=True
midjump=False
curwood_x=0
curwood_y=0
curwood_len=0
cat=0
start=time.time()
while RUN:
    pygame.time.Clock().tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
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
        if keys[pygame.K_SPACE] and keys[pygame.K_LCTRL] == False:
            swordout=swordtime
    if keys[pygame.K_LCTRL] and keys[pygame.K_SPACE] and carrotbelt!=[]:
        final_monkey.nunchuks()
    final_monkey=monkey()
    #WIN.fill((0,0,0))
    WIN.blit(bg,(0,0))
    exit_rect=pygame.Rect(SCREEN_WIDTH-door_exit.get_width()/2,exit_door_y,door_exit.get_width(),door_exit.get_height())
    exit_door=WIN.blit(door_entery,(entry_doorx,entry_doory))
    exit_door=WIN.blit(door_exit,(exit_door_x,exit_door_y))
    heartx=0
    for hearts in healthbar:
        WIN.blit(hearts,(heartx,0))
        heartx+=health.get_width()
    carx=2
    for car in carrotbelt:
        WIN.blit(car,(carx,heart.get_height()+2))
        carx+=carroticon.get_width()+3
    final_monkey.draw()
    monkey_rect = pygame.Rect(MX,MY,monkey_image2.get_width(),monkey_image2.get_height())
    sword_rect = pygame.Rect(final_monkey.swordpos, MY + final_monkey.sword.get_height() / 2 +10, sword_image2.get_width(), sword_image2.get_height())
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
    for strength in heartpower:
        strength.draw()
        strength.restore()
    for bull in carrotbox:
        bull.draw()
        bull.resupply()
    for turt in shoal: 
        if turt.alert==True:
            turt.movement()
        #pygame.draw.rect(WIN,(255,0,255),turt.trigger)

        turt.draw()
        turt.action()
    for carrot in carrotstorageL:
        carrot.draw()
        carrot.x-=ammoVEL
        carrot.limtest-=ammoVEL
        for turt in shoal:
            if turt.rect.colliderect(carrot.rect)and carrotstorageL!=[]:
                carrotstorageL.remove(carrot)
                turt.health-=10
                pygame.draw.rect(WIN,(255,255,255),(turt.x,turt.y,turt.widt,turt.lent))
        if carrot.limtest<=carrot.lim and carrotstorageL!=[]:
            carrotstorageL.remove(carrot)
        for walle in boards:
            if carrot.rect.colliderect(walle.rect):
                carrotstorageL.remove(carrot)
    for carrot in carrotstorageR:
        carrot.draw()
        carrot.x+=ammoVEL
        carrot.limtest+=ammoVEL
        for turt in shoal:
            if turt.rect.colliderect(carrot.rect)and carrotstorageR!=[]:
                carrotstorageR.remove(carrot)
                turt.health-=10
                pygame.draw.rect(WIN,(255,255,255),(turt.x,turt.y,turt.widt,turt.lent))

        if carrot.limtest>=carrot.lim and carrotstorageR!=[]:
            carrotstorageR.remove(carrot)
        for walle in boards:
            if carrot.rect.colliderect(walle.rect):
                carrotstorageR.remove(carrot)
    for ammo in turtle_armouryL:
        p=ammo.draw()
        ammo.x-=ammoVEL
        ammo.distance+=ammoVEL
        for wood in boards:
            if p.colliderect(wood.rect):
                turtle_armouryL.remove(ammo)
        if ammo.distance>=ammo.lim:
            turtle_armouryL.remove(ammo)
        if p.colliderect(monkey_rect):
            pygame.draw.rect(WIN,(200,0,0),monkey_rect )
            monkey_health-=1
            healthbar.pop()
            turtle_armouryL.remove(ammo)
    for ammo in turtle_armouryR:
        p=ammo.draw()
        ammo.x+=ammoVEL
        ammo.distance+=ammoVEL
        for wood in boards:
            if p.colliderect(wood.rect):
                turtle_armouryR.remove(ammo)
        if ammo.distance>=ammo.lim:
           turtle_armouryR.remove(ammo)
        if p.colliderect(monkey_rect):
            pygame.draw.rect(WIN,(200,0,0),monkey_rect )
            monkey_health-=1
            healthbar.pop()
            turtle_armouryR.remove(ammo)
    if MY>80*LOWLEV-current_monkey.get_height()-2:
        fall=False
    if fall==True and MY<80*LOWLEV-current_monkey.get_height()-1 :
        MY+=ammoVEL
    if monkey_health<=0:
        current_monkey=dead_monkey2
        monkey_rect=pygame.Rect(MX,MY,monkey_image2.get_width()+20,monkey_image2.get_height()+20)
        pygame.draw.rect(WIN,(136,136,136),monkey_rect)
        final_monkey=monkey()
        final_monkey.draw()
        pygame.display.update()
        pygame.time.delay(3000)
        end=time.time()
        mb.showinfo('death','you died')
        RUN=False
    if exit_rect.colliderect(monkey_rect) and swordout==True and shoal== []:
        pygame.time.delay(1000)
        WIN.fill((255,255,255))
        pygame.display.update()
        end=time.time()
        mb.showinfo('completion','congratulations!,you completed the level in '+str(int(end-start))+'seconds')
        mb.showinfo('thanks for playing')
        pygame.time.delay(1000)
        RUN=False
    if swordout!=0:
        sworddelay=0
        swordout-=1
        final_monkey.bite()
    else:
        sworddelay+=1
    if isjump==False and jumpcount!=ogjump:
        jumpcount=ogjump
    pygame.display.update()
pygame.quit()