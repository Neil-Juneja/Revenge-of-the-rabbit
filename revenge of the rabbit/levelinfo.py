import pickle
####inp={'jump':'w','left':'a','right':'d','melee':'SPACE','range':'LCTRL','level':'level1'}
###fox=open('control_config.dat','wb')
#{lev:[screenwidth,screenheight,MX,MY,selfhealth,maxammo,turthealth,lowlev,platforms,wall,turtle,
#       healthpowerup,carrotstock,exitdoorx,exitdoory]}
inp={'level1':[800,490,0,80*5+10,5,5,3,6,
    """planks=[base,platform(0,5,725,True),platform(0,4,50,True),platform(100,3,50),
    platform(0,2,50,True),platform(100,1,250),platform(225,2,200),platform(425,2,250,True),
    platform(150,3,125,True),platform(350,3,200),platform(150,4,650,True),platform(750,3,50),
    platform(600,1,200)]""",
    "boards=[wall(150,4),wall(150,3),wall(150,2),wall(425,1),wall(425,2),wall(550,3)]",
    """shoal=[turtle(1,600,6,200,200,40),turtle(2,0,5,300,200,30),turtle(2,170,1,200,200,40),
    turtle(2,175,3,100,200,40),turtle(2,350,3,200,300,40),
    turtle(2,375,4,425,200,30),turtle(2,450,2,200,200,20)]""",
    "heartpower=[healthpowerup(750,3),healthpowerup(500,3),healthpowerup(5,4),healthpowerup(225,2)]",
    "carrotbox=[carrotrestock(125,3),carrotrestock(550,4)]","SCREEN_WIDTH-door_exit.get_width()",
    "80-door_exit.get_height()"],
    'level2':[1000,650,750,80*3+10,7,5,3,8,
    """planks=[base,platform(600,4,400),platform(500,6,400,True),platform(500,5,100,True),platform(940,7,60),
        platform(50,7,150),platform(100,6,50),platform(50,5,40),platform(0,4,50),platform(125,4,300),
        platform(0,3,50),platform(100,2,200),platform(300,1,900),platform(300,3,600),
        platform(160,3,50,True),platform(0,1,200),platform(250,6,300),platform(425,5,75)]""",
    """boards=[wall(500,4),wall(500,5),wall(500,6),wall(990,5),wall(990,6),wall(990,7),wall(200,8),wall(150,6),
        wall(150,5),wall(150,3),wall(300,2)]""",
    """shoal=[turtle(1,0,8,200,100,20,0,200),turtle(2,0,1,200,500),turtle(1,400,1,600,300,20,300),turtle(2,300,3,200,400),
       turtle(1,150,4,250,100,20,125,425),turtle(1,525,6,375,100,20,500,900),turtle(2,225,8,350,300),turtle(2,600,8,400,300),
       turtle(2,250,6,250,200)]""",
    "heartpower=[healthpowerup(150,8),healthpowerup(250,2),healthpowerup(450,5)]",
    "carrotbox=[carrotrestock(175,3),carrotrestock(10,4),carrotrestock(960,7)]",
    "SCREEN_WIDTH-door_exit.get_width()","80-door_exit.get_height()"],
    }
fox=open('levels.dat','wb')
#fox=open('datasheet.dat','wb')
#{level:[best time,allmelee bool,nodamage bool]}
'''inp={'level1':[0],'level2':[0],'level3':[0],'level4':[0],'level5':[0],'level6':[0],'level7':[0]
     ,'level8':[0],'level9':[0],'level10':[0]}'''
pickle.dump(inp,fox)
fox.close()
fox=open('datasheet.dat','rb')
while True:
    try:
        dat=pickle.load(fox)
    except EOFError:
        break
'''for i in dat:
    if i=='o':
        break
    else:'''
print(dat)
fox.close()

