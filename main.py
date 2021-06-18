import pygame
import math
import random

# initialize the pygame
pygame.init()

screen = pygame.display.set_mode((1000, 800))

# background
background = pygame.image.load('bg3.png')
# title and icon
pygame.display.set_caption("KILL_CORONA")
icon = pygame.image.load('virus.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('jet.png')
playerX = 650
playerY = 700
playerX_change = 0

# enemy
enemyImg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies=15

for i in range(num_of_enemies):
    enemyImg .append(pygame.image.load('coronavirus.png'))
    enemyX .append (random.randint(0, 1000))
    enemyY .append (random.randint(50, 100))
    enemyX_change .append (5)
    enemyY_change .append (10)



# bullet
bulletImg = pygame.image.load('vaccine.png')
bulletX = 0
bulletY = 700
bulletX_change = 0
bulletY_change = 20
bullet_state = "ready"

#score

score_value=0
font = pygame.font.Font('freesansbold.ttf',64)

textX=10
textY=10

#Game over text
over_font = pygame.font.Font('freesansbold.ttf',128)

def show_score(X,Y):
    score =font.render("SCORE : "+str(score_value),True,(0,0,0))
    screen.blit(score, (X, Y))

def game_over_text():
    over_text = font.render("GAME OVER ", True, (255, 0, 0))
    screen.blit(over_text, (300,350))

def player(X, Y):
    screen.blit(playerImg, (X, Y))


def enemy(X, Y, i):
    screen.blit(enemyImg[i], (X, Y))


def fire_bullet(X,Y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(X + 10, Y + 10))

def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2))+ (math.pow(enemyY-bulletY,2)))
    if distance < 27:
        return True
    else:
        return False

# game loop
running = True
while running:
    # RGB - RED , GREEN, BLUE
    screen.fill((0, 0, 0))
    # background image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check ehether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -10
            if event.key == pygame.K_RIGHT:
                playerX_change = 10
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(playerX, bulletY)




        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key== pygame.K_RIGHT:

                playerX_change = 0
    # boundaries
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 936:
        playerX = 936
    # virus movement
    for i in range(num_of_enemies):
        #game over
        if enemyY[i]>640:
            for j in range(num_of_enemies):
                enemyY[j]=2000
            game_over_text()
            break



        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 10
            enemyY [i]+= enemyY_change[i]
        elif enemyX[i] >= 936:
            enemyX [i]= 936
            enemyX_change[i] = -10
            enemyY[i] += enemyY_change[i]

            # collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 700
            bullet_state = "ready"
            score_value += 1

            enemyX[i] = random.randint(0, 1000)
            enemyY[i] = random.randint(50, 100)

        enemy(enemyX[i], enemyY[i], i)


#soap movement
    if bulletY <=0 :
        bulletY=700
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX,bulletY)
        bulletY-=bulletY_change




    player(playerX, playerY)
    show_score(textX, textY)



    pygame.display.update()
