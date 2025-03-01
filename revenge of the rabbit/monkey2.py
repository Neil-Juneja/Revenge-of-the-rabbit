import pygame,random,os,time,pickle,sys
from tkinter import messagebox as mb
import tkinter as tk
import traceback

'''screenfo=tk.Tk()
screenwidthinit=screenfo.winfo_screenwidth()

screenheightinit=screenfo.winfo_screenheight()
screenfo.destroy()'''

pygame.font.init()
pygame.mixer.init()
#font=pygame.font.SysFont('courier new')
#load control
fox=open('control_config.dat','rb')
try:
    dat=pickle.load(fox)
except EOFError:
    pass
#################################
fox.seek(0)
fox.close()
usercontrol=list(dat.values())
rightcontrol=getattr(pygame,'K_'+usercontrol[2])
leftcontrol=getattr(pygame,'K_'+usercontrol[1])
jumpcontrol=getattr(pygame,'K_'+usercontrol[0])
meleecontrol=getattr(pygame,'K_'+usercontrol[3])
rangecontrol=getattr(pygame,'K_'+usercontrol[4])
#load leveldetails
fox=open('levels.dat','rb')
try:
    dat=pickle.load(fox)
except EOFError:
    pass
###################################
fox.seek(0)
fox.close()
for i in dat:
    if i==usercontrol[-1]:
        levelinfo=dat[usercontrol[-1]]
        break
else:
    print('no level selected')
    quit()
# 
SCREEN_WIDTH=levelinfo[0]
SCREEN_HEIGHT=levelinfo[1]
pygame.display.set_caption('revenge of the rabbit')
icon = pygame.image.load("rabbit.png")
pygame.display.set_icon(icon)
WIN=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))#,pygame.FULLSCREEN)
#pygame.display.set_mode((0,0))
#pygame.RESIZABLE()
MX=levelinfo[2]
MY=levelinfo[3]
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
#
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
                pygame.mixer.Channel(2).play(pygame.mixer.Sound('throwsound1.mp3'))
                carrotbelt.pop()
        if carrotstorageL==[]:
            if current_monkey==monkey_image3:
                carrotstorageL.append(carrotvel(self.x,self.y-self.img.get_height()/2+35,sword_image3))
                carrotstorageL[0].lim-=100
                maxcarrot-=1
                pygame.mixer.Channel(2).play(pygame.mixer.Sound('throwsound1.mp3'))
                carrotbelt.pop()

#
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
                pygame.mixer.Channel(3).play(pygame.mixer.Sound('collide.mp3'))
            elif MY<self.y:
                MY=self.y-current_monkey.get_height()+1
                fall=False

class wall():
    def __init__(self,x,ymult):
        self.width=15
        self.height=90
        self.y=80*(ymult-1)+1
        self.x=x
        self.rect=pygame.Rect(self.x,self.y,self.width,self.height)
    def draw(self):
        pygame.draw.rect(WIN,(60,60,60),self.rect)
    def collision(self):
        global MX
        if self.rect.colliderect(monkey_rect):
            pygame.mixer.Channel(3).play(pygame.mixer.Sound('collide.mp3'))
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
    def __init__(self,type_,x,y,distance,range_,freq=20,leftlim=0,rightlim=(SCREEN_WIDTH+turtle_image2.get_width())):
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
        self.timer=0
        self.rightlim=rightlim
        self.leftlim=leftlim
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
                
        #melee
        elif self.type==1:
            if self.trigger.colliderect(monkey_rect):
                self.alert=False
                if self.freq!=50:
                    self.freq+=1
                else:
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
                            self.freq=0
                            healthbar.pop()
                            pygame.draw.rect(WIN,(200,0,0),monkey_rect )
                            self.headbutt=1
            else:
                self.timer+=1
                if self.timer==50:
                    self.timer=0
                    self.alert=True
            if self.headbutt==1:
                if self.direct==0 :
                    if self.x<0 or self.x< self.leftlim:
                        pass
                    else:
                        self.x-=20
                elif self.direct==1:
                    if self.x + self.widt> SCREEN_WIDTH or self.x > self.rightlim:
                        pass
                    else:
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


#
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
monkey_health=levelinfo[4]
monkeyhealth=monkey_health
healthbar=[]
for i in range(monkey_health):
    healthbar.append(health)
carrotbelt=[]
maxcarrot=levelinfo[5]
maxxcarrot=maxcarrot
for i in range(maxcarrot):
    carrotbelt.append(carroticon)
carrotstorageL=[]
carrotstorageR=[]
turtle_health=levelinfo[6]*swordtime
turtle_armouryL=[]
turtle_armouryR=[]
bullet_limit=500
bullet_freq=10
prechargepause=15
LOWLEV=levelinfo[7]
base=platform(0,LOWLEV,SCREEN_WIDTH)
exec(levelinfo[8])
exec(levelinfo[9])
exec(levelinfo[10])
exec(levelinfo[11])
exec(levelinfo[12])
exit_door_x=int(eval(levelinfo[13]))
exit_door_y=int(eval(levelinfo[14]))
entry_doorx=MX
entry_doory=MY
fall=True
midjump=False
curwood_x=0
curwood_y=0
curwood_len=0
cat=0
start=time.time()
overhealth=monkey_health+len(heartpower)
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
    #rightcontrol='keys[pygame.K_'+str(usercontrol[2])+']'
    if keys[rightcontrol]:
        if MX>=SCREEN_WIDTH-monkey_image2.get_width():
            pass
        else:
            current_monkey=monkey_image2
            current_sword=sword_image2
            sword_position=MX+monkey_image2.get_width()
            MX+=VEL
    if keys[leftcontrol]:
        if MX<=0:
            pass
        else:
            current_monkey=monkey_image3
            current_sword=sword_image3
            sword_position=MX-current_sword.get_width()
            MX-=VEL
    if keys[jumpcontrol] and fall==False:
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('jumpsound1.mp3'))
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
        if keys[meleecontrol] and keys[rangecontrol] == False:
            swordout=swordtime
            pygame.mixer.Channel(4).play(pygame.mixer.Sound('slashsound.mp3'))

    if keys[pygame.K_ESCAPE]:
        try:
            continueconfirm=mb.askokcancel('pause','Do you want to quit the level? Progress will be lost.')
        except tk.TclError:
            traceback.print_exc()
        if continueconfirm:
            RUN=False
        else:
            time.sleep(1)
#throwcarrot
    if keys[rangecontrol] and carrotbelt!=[]:
        final_monkey.nunchuks()
        
#
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
#gimme strength
    for strength in heartpower:
        strength.draw()
        strength.restore()
#runninglow
    for bull in carrotbox:
        bull.draw()
        bull.resupply()
#nolightsaber
    for turt in shoal:
        if turt.x<=0:
            turt.direct=0
        if turt.x+turt.widt>=SCREEN_WIDTH:
            turt.direct=1
        if turt.alert==True:
            turt.movement()
        
        turt.draw()
        #pygame.draw.rect(WIN,(255,0,255),turt.trigger)
        turt.action()
        #pygame.draw.rect(WIN,(255,0,0),turt.hitbox)
        '''if pygame.Rect(turt.x,turt.y,turt.curimg.get_width(),turt.curimg.get_height()).colliderect(monkey_rect):
            monkey_health-=1
            if current_monkey==monkey_image1:
                MX-=VEL*12
            else:
                MX+=VEL*12
            healthbar.pop()
            pygame.draw.rect(WIN,(200,0,0),monkey_rect)'''

#morelikethwak
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
#pewpew
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
        mb.showinfo('death','you died')
        RUN=False
#completion
    if exit_rect.colliderect(monkey_rect) and swordout==True and shoal== []:
        end=time.time()
        fox=open('control_config.dat','rb')
        try:
            dat=pickle.load(fox)
        except EOFError:
            pass
        fox.close()
        fox=open('datasheet.dat','rb')
        try:
            datp=pickle.load(fox)
        except EOFError:
            pass
        ##########################333
        fox.seek(0)
        fox.close()
        if datp==None:
            datp={}
        curlev=dat['level']
        olddata=datp[curlev]
        if olddata!=[]:
            olddata.pop(0)
        olddata.insert(0,int(end-start))
        if len(olddata)>1:
            pass
        else:
            if overhealth==(len(heartpower)+len(healthbar)):
                olddata.insert(1,True)
        datp[curlev]=olddata
        fox=open('datasheet.dat','wb')
        pickle.dump(datp,fox)
        fox.close()
        pygame.time.delay(1000)
        WIN.fill((255,255,255))
        pygame.display.update()
        mb.showinfo('completion','congratulations!,you completed the level in'+str(int(end-start))+'seconds')
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

sys.path.append('introscreen.py')
import introscreen

exit()