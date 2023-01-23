import pygame
import os
pygame.init()
pygame.mixer.init() 
current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)
#Misc. Variables---------------------------------
showdebug=-1
redball_thrown=0
blueball_thrown=0
zoomies=5
ballzoomies=1
redballer_health=3
blueballer_health=3
rounds=3
b2skin=2
b1skin=1

#----------------Create Window-------------------
width=1800
height=1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Baller Brawl HD32K Blueller and Blebert DLC")

#----------------Create Baller1-----------------
baller1=pygame.image.load(os.path.join(current_dir, "Images", "baller.png"))
baller1_rect = baller1.get_rect()
baller1_x, baller1_y = 50, 50
#pixels per frame
baller1_speed = 1
baller1_rect.width = 200
baller1_rect.x,baller1_rect.y = baller1_x,baller1_y
def skincheckballer1():
    global baller1
    if b1skin==1:
        baller1=pygame.image.load(os.path.join(current_dir, "Images", "baller.png"))
    elif b1skin==-1:
        baller1=pygame.image.load(os.path.join(current_dir, "Images", "BallerConfused.png"))
    elif b1skin==2:
        baller1=pygame.image.load(os.path.join(current_dir, "Images", "baller2.png"))
    elif b1skin==-2:
        baller1=pygame.image.load(os.path.join(current_dir, "Images", "Baller2Confused.png"))
    elif b1skin==3:
        baller1=pygame.image.load(os.path.join(current_dir, "Images", "crusher.png"))
    elif b1skin==-3:
        baller1=pygame.image.load(os.path.join(current_dir, "Images", "crusherconfused.png"))
    elif b1skin==4:
        baller1=pygame.image.load(os.path.join(current_dir, "Images", "buffballer.png"))
    elif b1skin==-4:
        baller1=pygame.image.load(os.path.join(current_dir, "Images", "buffballerconfused.png"))
    elif b1skin==5:
        baller1=pygame.image.load(os.path.join(current_dir, "Images", "shaggyballer.png"))
    elif b1skin==-5:
        baller1=pygame.image.load(os.path.join(current_dir, "Images", "shaggyballerconfused.png"))
    elif b1skin==6:
        baller1=pygame.image.load(os.path.join(current_dir, "Images", "piercer.png"))
    elif b1skin==-6:
        baller1=pygame.image.load(os.path.join(current_dir, "Images", "piercerconfused.png"))
#--------------Create Baller2--------------------

baller2=pygame.image.load(os.path.join(current_dir, "Images", "baller2.png"))
baller2_rect = baller2.get_rect()
baller2_x, baller2_y = 1500, 50
#pixels per frame
baller2_speed = 1
baller2_rect.width=200
baller2_rect.x,baller2_rect.y = baller2_x,baller2_y
def skincheckballer2():
    global baller2
    if b2skin==1:
        baller2=pygame.image.load(os.path.join(current_dir, "Images", "baller.png"))
    elif b2skin==-1:
        baller2=pygame.image.load(os.path.join(current_dir, "Images", "BallerConfused.png"))
    elif b2skin==2:
        baller2=pygame.image.load(os.path.join(current_dir, "Images", "baller2.png"))
    elif b2skin==-2:
        baller2=pygame.image.load(os.path.join(current_dir, "Images", "Baller2Confused.png"))
    elif b2skin==3:
        baller2=pygame.image.load(os.path.join(current_dir, "Images", "crusher.png"))
    elif b2skin==-3:
        baller2=pygame.image.load(os.path.join(current_dir, "Images", "crusherconfused.png"))
    elif b2skin==4:
        baller2=pygame.image.load(os.path.join(current_dir, "Images", "buffballer.png"))
    elif b2skin==-4:
        baller2=pygame.image.load(os.path.join(current_dir, "Images", "buffballerconfused.png"))
    elif b2skin==5:
        baller2=pygame.image.load(os.path.join(current_dir, "Images", "shaggyballer.png"))
    elif b2skin==-5:
        baller2=pygame.image.load(os.path.join(current_dir, "Images", "shaggyballerconfused.png"))
    elif b2skin==6:
        baller2=pygame.image.load(os.path.join(current_dir, "Images", "piercer2.png"))
    elif b2skin==-6:
        baller2=pygame.image.load(os.path.join(current_dir, "Images", "piercer2confused.png"))
#--------------Create redball-------------------------
redball=pygame.image.load(os.path.join(current_dir, "Images", "reddodgeball.png"))
redball_rect = redball.get_rect()
redball_rect.x=10000
redball_rect.y=10000
def skincheckredball():
    global redball
    global b1skin
    if b1skin == 3 or b1skin == -3:
        redball=pygame.image.load(os.path.join(current_dir, "Images", "crusherball.png"))
    elif b1skin == 5 or b1skin == -5:
        redball=pygame.image.load(os.path.join(current_dir, "Images", "shaggyball.png"))
    elif b1skin == 6 or b1skin == -6:
        redball=pygame.image.load(os.path.join(current_dir, "Images", "piercerball.png"))

#--------------Create blueball------------------------
blueball=pygame.image.load(os.path.join(current_dir, "Images", "bluedodgeball.png"))
blueball_rect = blueball.get_rect()
blueball_rect.x=10000
blueball_rect.y=10000
def skincheckblueball():
    global blueball
    global b2skin
    if b2skin == 3 or b2skin == -3:
        blueball=pygame.image.load(os.path.join(current_dir, "Images", "crusherball2.png"))
    elif b2skin == 5 or b2skin == -5:
        blueball=pygame.image.load(os.path.join(current_dir, "Images", "shaggyball.png"))
    elif b2skin == 6 or b2skin == -6:
        blueball=pygame.image.load(os.path.join(current_dir, "Images", "piercerball2.png"))
#----------------Create Halves--------------------
left_half_rect = pygame.Rect(0, 0, width/2, height)
right_half_rect = pygame.Rect(width/2, 0, width/2, height)

#Create Borders------------------------------------
outlinetop = pygame.Rect(0, 0, width, 20)
outlineleft = pygame.Rect(0, 0, 20, height)
outlineright = pygame.Rect(width-20, 0, 20, height)
outlinebottom = pygame.Rect(0, height-20, width, 20)

#Create hearts-------------------------------------
blueheart1=pygame.image.load(os.path.join(current_dir, "Images", "blueheart.png"))
blueheart2=pygame.image.load(os.path.join(current_dir, "Images", "blueheart.png"))
blueheart3=pygame.image.load(os.path.join(current_dir, "Images", "blueheart.png"))
redheart1=pygame.image.load(os.path.join(current_dir, "Images", "redheart.png"))
redheart2=pygame.image.load(os.path.join(current_dir, "Images", "redheart.png"))
redheart3=pygame.image.load(os.path.join(current_dir, "Images", "redheart.png"))
blueheart1_rect=blueheart1.get_rect()
blueheart2_rect=blueheart2.get_rect()
blueheart3_rect=blueheart3.get_rect()
redheart1_rect=redheart1.get_rect()
redheart2_rect=redheart3.get_rect()
redheart3_rect=redheart1.get_rect()
blueheart1_rect.x, blueheart1_rect.y=50, 50
blueheart2_rect.x, blueheart2_rect.y=100, 50
blueheart3_rect.x, blueheart3_rect.y=150, 50
redheart1_rect.x, redheart1_rect.y=1700, 50
redheart2_rect.x, redheart2_rect.y=1650, 50
redheart3_rect.x, redheart3_rect.y=1600, 50

#Prepare Text---------------------------------------
font = pygame.font.Font(None, 72)
def type(text):
    text_surf = font.render(text, True, (0, 0, 0))
    text_rect = text_surf.get_rect()
    text_rect.center = (width//2, height//2)
    screen.blit(text_surf, text_rect)
    pygame.display.update()
def whitetype(text):
    text_surf = font.render(text, True, (255, 255, 255))
    text_rect = text_surf.get_rect()
    text_rect.center = (width//2, height//2)
    screen.blit(text_surf, text_rect)
    pygame.display.update()

#Sound Effects
bonk=pygame.mixer.Sound(os.path.join(current_dir, "sounds", "bonk", "bonk.mp3"))
bonk.set_volume(1)
huh=pygame.mixer.Sound((os.path.join(current_dir, "sounds", "huh", "huh.mp3")))
huh.set_volume(0.1)

b1skin, b2skin = 1, 2
#Prestart Loop------------------------------------------------------------------------
prestart=True
while prestart:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            prestart = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                prestart = False
            


    #Change Skins
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and event.type == pygame.KEYDOWN:
            b2skin=b2skin+1
            print(b2skin)
        if keys[pygame.K_w] and event.type == pygame.KEYDOWN:
            b1skin=b1skin+1
            print(b1skin)
        if keys[pygame.K_DOWN] and event.type == pygame.KEYDOWN:
            b2skin=b2skin-1
            print(b2skin)
        if keys[pygame.K_s] and event.type == pygame.KEYDOWN:
            b1skin=b1skin-1
            print(b1skin)
        
    
    #Blit Ballers
    skincheckballer1()
    skincheckballer2()
    print(baller1)
    screen.blit(baller2, baller2_rect)
    screen.blit(baller1, baller1_rect)
    pygame.display.update()
    #Type 
    whitetype("1. Baller, 2. Blueler, 3. Crusher, 4. Buffballer, 5. Shaggyballer, 6. Piercer")



#-----------------------------------------------------------------------------------------#
#-------------------------------Main Loop-------------------------------------------------#
#-----------------------------------------------------------------------------------------#
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # ---Baller1 Controls------------------------------------------------------------------------
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        baller1_x -= baller1_speed*zoomies
    if keys[pygame.K_d]:
        baller1_x += baller1_speed*zoomies
    if keys[pygame.K_w]:
        baller1_y -= baller1_speed*zoomies
    if keys[pygame.K_s]:
        baller1_y += baller1_speed*zoomies
    baller1_rect.x,baller1_rect.y = baller1_x,baller1_y

    # ---Baller2 Controls------------------------------------------------------------------------
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        baller2_x -= baller2_speed*zoomies
    if keys[pygame.K_RIGHT]:
        baller2_x += baller2_speed*zoomies
    if keys[pygame.K_UP]:
        baller2_y -= baller2_speed*zoomies
    if keys[pygame.K_DOWN]:
        baller2_y += baller2_speed*zoomies
    baller2_rect.x, baller2_rect.y = baller2_x, baller2_y

    #--------Debug Rect Options---------
    if keys[pygame.K_b]:
        showdebug=-1
    if keys[pygame.K_v]:
        showdebug=1

    #----Reverse Controls if touching edge Baller1-----
    if baller1_rect.right > width/2:
        baller1_speed=-1*baller1_speed
        b1skin=-1*b1skin
    if baller1_rect.left < 20:
        baller1_speed=-1*baller1_speed
        b1skin=-1*b1skin
    if baller1_rect.top < 20:
        baller1_speed=-1*baller1_speed
        b1skin=-1*b1skin
    if baller1_rect.bottom > height-20:
        baller1_speed=-1*baller1_speed
        b1skin=-1*b1skin
    if baller1_speed==-1:
        huh.play()

    #-------Reverse Controls if touching edge Baller2-------
    if baller2_rect.left < width/2:
        baller2_speed=-1*baller2_speed
        b2skin=-1*b2skin
    if baller2_rect.right > width-20:
        baller2_speed=-1*baller2_speed
        b2skin=-1*b2skin
    if baller2_rect.top < 20:
        baller2_speed=-1*baller2_speed
        b2skin=-1*b2skin
    if baller2_rect.bottom > height-20:
        baller2_speed=-1*baller2_speed
        b2skin=-1*b2skin
    if baller2_speed==-1:
        huh.play()

#Colorcourt----------------------------------
    screen.fill((255,0,0), left_half_rect)
    screen.fill((0,0,255), right_half_rect)

#Colorborder---------------------------------
    screen.fill((0,0,0), outlinetop)
    screen.fill((0,0,0), outlineleft)
    screen.fill((0,0,0), outlineright)
    screen.fill((0,0,0), outlinebottom)

#Draw Baller1--------------------------------------
    if showdebug == 1:
        screen.fill((255,255,255), baller1_rect)
    screen.blit(baller1, baller1_rect)  # Draw the image
    skincheckballer1()
    
#Draw Baller2--------------------------------------
    if showdebug == 1:
        screen.fill((255,255,255), baller2_rect)
    screen.blit(baller2, baller2_rect) # Draw the image
    skincheckballer2()
#redballs---------------------------------------
    skincheckredball()
    if showdebug == 1:
        screen.fill((255,40,20), redball_rect)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LSHIFT]:
        if redball_thrown==0:
            redball_rect.x, redball_rect.y = baller1_x+50, baller1_y
            redball_thrown = 1
    if redball_thrown==1:
        redball_rect.x = redball_rect.x+10*ballzoomies
    if redball_rect.x > width-120:
        redball_thrown=0
    screen.blit(redball, redball_rect)
    if redball_rect.left < baller2_rect.right:
        if redball_rect.right > baller2_rect.left:
            if redball_rect.top < baller2_rect.bottom:
                if redball_rect.bottom > baller2_rect.top:
                    bonk.play()
                    redball_rect.x=10000
                    if redball_thrown==1:
                        blueballer_health-=1
                    redball_thrown=0
                    if blueballer_health==0:
                        redheart1=pygame.image.load(os.path.join(current_dir, "Images", "redheartdead.png"))
                        redheart2=pygame.image.load(os.path.join(current_dir, "Images", "redheartdead.png"))
                        redheart3=pygame.image.load(os.path.join(current_dir, "Images", "redheartdead.png"))
                        type("1st Baller Wins")
                        pygame.time.wait(2000)
                        running=False
    
#blueballs
    skincheckblueball()
    if showdebug == 1:
        screen.fill((20,40,255), blueball_rect)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_KP0]:
           if blueball_thrown==0:
            blueball_rect.x, blueball_rect.y = baller2_x+95, baller2_y
            blueball_thrown =1
    if blueball_thrown==1:    
        blueball_rect.x = blueball_rect.x-10*ballzoomies
    if blueball_rect.x <20:
        blueball_thrown=0
    screen.blit(blueball, blueball_rect)
    if blueball_rect.left < baller1_rect.right:
        if blueball_rect.right > baller1_rect.left:
            if blueball_rect.top < baller1_rect.bottom:
                if blueball_rect.bottom > baller1_rect.top:
                    bonk.play()
                    blueball_rect.x=10000
                    if blueball_thrown==1:    
                        redballer_health-=1
                    blueball_thrown=0
                    if redballer_health==0:
                        blueheart3=pygame.image.load(os.path.join(current_dir, "Images", "blueheartdead.png"))
                        blueheart2=pygame.image.load(os.path.join(current_dir, "Images", "blueheartdead.png"))
                        blueheart1=pygame.image.load(os.path.join(current_dir, "Images", "blueheartdead.png"))
                        type("2nd Baller Wins")
                        pygame.time.wait(2000)
                        running=False

#redhearts
    if blueballer_health==2:
        redheart3=pygame.image.load(os.path.join(current_dir, "Images", "redheartdead.png"))
    if blueballer_health==1:
        redheart3=pygame.image.load(os.path.join(current_dir, "Images", "redheartdead.png"))
        redheart2=pygame.image.load(os.path.join(current_dir, "Images", "redheartdead.png"))
    screen.blit(redheart1, redheart1_rect)
    screen.blit(redheart2, redheart2_rect)
    screen.blit(redheart3, redheart3_rect)
    
#bluehearts
    if redballer_health==2:
        blueheart3=pygame.image.load(os.path.join(current_dir, "Images", "blueheartdead.png"))
    if redballer_health==1:
        blueheart3=pygame.image.load(os.path.join(current_dir, "Images", "blueheartdead.png"))
        blueheart2=pygame.image.load(os.path.join(current_dir, "Images", "blueheartdead.png"))
    screen.blit(blueheart1, blueheart1_rect)
    screen.blit(blueheart2, blueheart2_rect)
    screen.blit(blueheart3, blueheart3_rect)

#------Update Screen-------------------
    pygame.display.update()  # Update the screen

#-----------------------------------------------------------------------------------------#
#------------------------End of Main Loop-------------------------------------------------#
#-----------------------------------------------------------------------------------------#    


pygame.quit()
