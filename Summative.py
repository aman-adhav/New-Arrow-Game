from pygame import*
import pygame
from random import*
import time
init()
RED = (255,0,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
TONE = (100, 100, 100)
GREEN = (100, 255, 100)
BLUE = (0, 0, 255)
size = width,height = 800,600
screen = display.set_mode(size)
enviroP = image.load("enviro.png")
amanlogo = image.load("amanlogo.png")
running = True
myclock = pygame.time.Clock()
count = 0
MENUSTATE = 0
QUITSTATE = 1
PLAYSTATE = 2
arch = image.load("archer.png")
blubal = image.load("brokencomputer.gif")
button = 0
run = True
mx = my = 0
arrow = image.load("arrow.jpg")
shot = False
shotx = 0
shoty = 0
y1 = 600
expl = image.load("explo.png")
balloon = True
explo = False
exploy = 0
explotime = 0
y2 = 0
b = 0
speed = [-0.1,-0.2,-0.3,-0.4,-0.5,-0.6,-0.7,-0.8,-0.9,-1,-1.3,-1.5,-1.7,-2.1,-2.3] 
shuffle(speed)
arrows = 9
count = 0

def drawscreen(x,y,button,balloon,shot,y1):
    global explo,exploy,explotime,y2, arrows,b
    #if evnt.type != MOUSEBUTTONDOWN:
    results = [shot, balloon]
    pygame.draw.rect(screen,WHITE,(0,0,800,600))
    screen.blit(arch, Rect(50, y, size[0], size[1]))
    fontTitle = font.SysFont("Impact",width/15)
    string = "Arrows: " + str(arrows)
    titleText = fontTitle.render(string, 1, RED)
    titleSize = fontTitle.size("The Greatest Game EVER")
    screen.blit(titleText, (width/3 - titleSize[0]/2, height/10 - titleSize[1]/2, titleSize[0], titleSize[1]))
    
    font1 = font.SysFont("Impact",width/15)
    string1 = "Destroyed: " + str(b)
    title = font1.render(string1, 1, RED)
    title1 = font1.size("The Greatest Game EVER")
    screen.blit(title, (width/1.1 - title1[0]/2, height/10 - title1[1]/2, title1[0], title1[1]))
    if balloon == True:
        size1 = blubal.get_rect().size
        balRect = Rect(600,y1, size1[0], size1[1])
        screen.blit(blubal, balRect)
    if shot == True:
        size2 = arrow.get_rect().size
        arrowRect = Rect(shotx,shoty+65,size2[0], size2[1])
        screen.blit(arrow, arrowRect)
    if explo == True:
        screen.blit(expl, Rect(600,exploy,size[0], size[1]))
    if balloon == True and shot == True:
        if arrowRect.colliderect(balRect) == True:
            screen.blit(expl, Rect(600,y1,size[0], size[1]))
            exploy = y1
            explotime = 100
            results[0] = False
            results[1] = False
            explo = True
            arrows += 1
    display.flip()
    return results
def checkButtonMenu(button, mouseX, mouseY):
    if button == 1:
        if checkPlayMenu(mouseX, mouseY) == True:
            return PLAYSTATE
        elif checkQuitMenu(mouseX, mouseY) == True:
            return QUITSTATE
    
# check if mouse is within the play menu box
def checkPlayMenu(mouseX, mouseY):
    playMenuLeft = width/4
    playMenuWidth = width/2
    playMenuTop = height/4
    playMenuHeight = height/5
  
    if mouseX >= playMenuLeft and mouseX <= playMenuLeft + playMenuWidth and mouseY >= playMenuTop and mouseY <= playMenuTop + playMenuHeight:
        return True
    return False

#check if mouse is within the quit menu box
def checkQuitMenu(mouseX, mouseY):
    playMenuLeft = width/4
    playMenuWidth = width/2
    playMenuTop = height/2
    playMenuHeight = height/5
  
    if mouseX >= playMenuLeft and mouseX <= playMenuLeft + playMenuWidth and mouseY >= playMenuTop and mouseY <= playMenuTop + playMenuHeight:
        return True
    return False

# paint the menu screen
def paintMenu(mouseX, mouseY):
  # title fonts
    screen.blit(enviroP, Rect(50, 25, size[0], size[1]))
    # current colour fonts
    fontMenu = font.SysFont("Impact",width/12)	
    menuText1 = fontMenu.render("Play Game:", 1, RED)
    menuText2 = fontMenu.render("Quit Game:", 1, RED)
    text1Size = fontMenu.size("Play Game:")
    text2Size = fontMenu.size("Quit Game:")
  
    # determine the colour of the menu options background
    colMenu1 = TONE
    colMenu2 = TONE
    if checkPlayMenu(mouseX, mouseY):
        colMenu1 = GREEN
    
    if checkQuitMenu(mouseX, mouseY):
        colMenu2 = GREEN
    
  
  # draw the menu options
    pygame.draw.rect(screen, colMenu1, (width/4, height/4, width/2, height/5))
    screen.blit(menuText1, (width/2 - text1Size[0]/2, height/4 + height/10 - text1Size[1]/2, text1Size[0], text1Size[1]))
    pygame.draw.rect(screen, colMenu2, (width/4, height/2, width/2, height/5))
    screen.blit(menuText2, (width/2 - text2Size[0]/2, height/2 + height/10 - text2Size[1]/2, text1Size[0], text1Size[1]))
    display.flip()

#######################################################################
########                 GAME FUNCTIONS                   #############
#######################################################################

def paintGame(mouseX, mouseY):
    global shot,shotx,shoty,y1,b,exploy,explotime,explo, run, mx,my,arrows,balloon,button,arrows,speed,y2,m1,m2
    while run == True:
        for evnt in pygame.event.get():
            if evnt.type == pygame.QUIT:
                run = False
            if evnt.type == MOUSEMOTION:
                mx,my = evnt.pos
            if evnt.type == MOUSEBUTTONDOWN:
                mx, my = evnt.pos          
                button = evnt.button
                if shot == False:
                    shot = True
                    shotx = 50
                    shoty = my
                    
        temp = drawscreen(mx,my,button,balloon,shot,y1)
        shot = temp[0]
        balloon = temp[1]
        if y1 > 0:
            y1 += speed[y2]
            if balloon == False:
                y2 += 1
                if y2 == 15:
                    y2 = 0
                    shuffle(speed)
        else:
            y1 = 600
        if shot == True:
            shotx += 2.5
            if shotx > 800:
                shot = False
                arrows += -1
                if arrows <= 0:
                    font2 = font.SysFont("Impact",width/15)
                    string2 = "Game Over \n Best Score: " + str(b)
                    titlee = font2.render(string2, 1, RED)
                    title11 = font2.size("The Greatest Game EVER")
                    screen.blit(titlee, (width/3 - title11[0]/2, height/5 - title11[1]/2, title11[0], title11[1]))
                    run = False
                    for evnt in pygame.event.get():
                        if evnt.type == pygame.QUIT:
                            quit()
                    
        if balloon == False:
            balloon = True
            y1 = 0
        if explo == True:
            explotime -= 10
            if explotime == 0:
                explo = False
                b += 1
        display.flip()
    
def draw(screen):
    screen.fill(WHITE)
    display.flip()
    pygame.time.wait(180)
gameState = MENUSTATE  # menuState
m1 = m2 = 0
button1 = 0
while running == True:
    if count <= 5:
        screen.fill(RED)
        display.flip()
        pygame.time.wait(180)
        draw(screen)
    if count == 6:
        screen.fill(BLACK)
        screen.blit(amanlogo, Rect(100, 100, size[0], size[1]))
        display.flip()
        pygame.time.wait(2000)
        screen.fill(WHITE)
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False
    count += 1
    if count > 6:
        myclock.tick(480)
        #screen.blit(enviroP, Rect(50, 50, size[0], size[1]))
    if gameState == MENUSTATE:
        paintMenu(m1, m2)               # draw the main menu
    elif gameState == QUITSTATE:
        running = False                 # quit the game
    elif gameState == PLAYSTATE:
        paintGame(m1, m2)               # draw the game screen
       
    for evnt in event.get():          # check for events
        if evnt.type == QUIT:
            running = False
        if evnt.type == MOUSEMOTION:
            m1, m2 = evnt.pos
        if evnt.type == MOUSEBUTTONDOWN:
            button1 = evnt.button
            m1, m2 = evnt.pos
            if gameState == MENUSTATE:
                gameState = checkButtonMenu(button1, m1, m2)
            elif gameState == PLAYSTATE:
                gameState = checkButtonGame(button1, m1, m2)
    display.flip()

quit()
        
            

        