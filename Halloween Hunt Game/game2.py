import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((650, 500))
bg = pygame.image.load('C:/Users/Tanya/Desktop/Halloween Hunt Game/halloween.jpg')
bg1=pygame.transform.scale(bg, (650, 500))
pygame.display.set_caption("HAPPY HALLOWEEN!")
icon=pygame.image.load("C:/Users/Tanya/Desktop/Halloween Hunt Game/hat.png")
pygame.display.set_icon(icon)
predator = pygame.image.load("C:/Users/Tanya/Desktop/Halloween Hunt Game/witch.png")
x = 290
y = 380
xchange = 0
def predator1(x1, y1):
    screen.blit(predator, (x1, y1))

prey = []
xp = []
yp = []
xpchange = []
ypchange = []
no_of_prey = 5

for j in range(no_of_prey):
    prey.append(pygame.image.load("C:/Users/Tanya/Desktop/Halloween Hunt Game/skeleton.png"))
    xp.append(random.randint(0, 628))
    yp.append(random.randint(5, 90))
    xpchange.append(1)
    ypchange.append(30)

def prey1(x1, y1, j):
    screen.blit(prey[j], (x1, y1))
web = pygame.image.load("C:/Users/Tanya/Desktop/Halloween Hunt Game/smoke.png")
xweb=0
yweb=380
xwchange=0
ywchange=0.7
web_state="pause"

def throw_web(x,y):
    global web_state
    web_state = "throw"
    screen.blit(web,(x+16, y+10))

score_value = 0
font = pygame.font.Font("freesansbold.ttf", 20)
textx=10
texty=10

def show_score(x,y):
    score = font.render("Score :" + str(score_value), True, (0,0,0))
    screen.blit(score, (x,y))

finish = pygame.font.Font('freesansbold.ttf', 65)

def game_over():
    finished = finish.render("GAME OVER", True, (0,0,0))
    screen.blit(finished, (135, 210))

def collision(xp,yp,xweb,yweb):
    dist = math.sqrt((math.pow(xp-xweb, 2))+(math.pow(yp-yweb, 2)))
    if dist < 27:
        return True
    else:
        return False

run = True
while run:
    screen.blit(bg1, (0,0))

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False

        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                xchange = -0.7
            if i.key == pygame.K_RIGHT:
                xchange = 0.7
            if i.key == pygame.K_SPACE:
                if web_state is "pause":
                    xweb = x
                    throw_web(xweb, yweb)
        if i.type == pygame.KEYUP:
            xchange = 0

    x += xchange
    if x <=0:
        x = 0
    elif x>=586:
        x=586

    for j in range(no_of_prey):
        
        if yp[j]>300:
            for k in range(no_of_prey):
                yp[k]=2000
            game_over()
            break
        xp[j] += xpchange[j]
        if xp[j] <= 0:
            xpchange[j] = 0.15
            yp[j] += ypchange[j]
        elif xp[j] >= 586:
            xpchange[j] = -0.15
            yp[j] += ypchange[j]
        
        col = collision(xp[j], yp[j], xweb, yweb)
        if col:
            yweb = 380
            web_state = "pause"
            score_value += 1
            xp[j] = random.randint(0,628)
            yp[j] = random.randint(5,150)

        prey1(xp[j], yp[j], j)

    if yweb <=0:
        yweb = 380
        web_state = "pause"

    if web_state is "throw":
        throw_web(xweb, yweb)
        yweb -= ywchange

    predator1(x, y)
    show_score(textx, texty)
    pygame.display.update()



