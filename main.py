import pygame
import random
import math
from pygame import mixer
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode( SIZE )
background = pygame.image.load("eclipse.jpg")


mixer.music.load("Background.wav")
mixer.music.play(-1)

pygame.display.set_caption("Space Invaders")

icon = pygame.image.load("space-invaders (1).png")
pygame.display.set_icon( icon )


player_ing =  pygame.image.load("nave-espacial.png")
player_x = 360
player_y = 500
player_x_change = 0
 
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
number_enemies = 10
for item in range(number_enemies):
 enemy_img.append( pygame.image.load("ufo.png"))  
 enemy_x.append(random.randint(0,100))
 enemy_y.append (random.randint(50, 150))
 enemy_x_change.append( 1)
 enemy_y_change.append (60)

bullet_img = pygame.image.load("bullet.png")
bullet_x = 0
bullet_y = 500
bullet_state = "ready"
bullet_y_change = 2

score = 0

score_font = pygame.font.Font("font.otf", 32)

text_x = 20
text_y = 20
def text(text_x,text_y):
    score_text = score_font.render("Score: " +str(score), True, (254, 254, 254))
    screen.blit(score_text, (text_x,text_y))


def player(x, y):
    screen.blit(player_ing, (x, y))    

def enemy(x, y, item):
        screen.blit(enemy_img[item], (x, y)) 
def fire(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img,(x + 20, y + 10))
def hitbox(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt((enemy_x - bullet_x)**2 + (enemy_y - bullet_y)**2)
    if distance < 27:
        return True
    else:
        return False


running = True
while running: 
    RGB = (20,80,120)
    screen.fill( RGB )
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                player_x_change -= 1

            if event.key == pygame.K_RIGHT:   
                player_x_change = 1
            
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound("shoot.wav")
                    bullet_x = player_x
                    fire(player_x, bullet_y)

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_d or pygame.K_a:
                player_x_change = 0

            
    player_x += player_x_change
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736
    
    for item in range(number_enemies):
        enemy_x[item] += enemy_x_change[item]
        if enemy_x[item] >= 736:
            enemy_x[item] -= enemy_x_change[item]
            enemy_x_change[item] = -1
            enemy_y[item] += enemy_y_change[item]
        elif enemy_x[item] <= 0:
            enemy_x_change[item] = 1
            enemy_y[item] += enemy_y_change[item]
        
        collition = hitbox(enemy_x[item], enemy_y[item], bullet_x, bullet_y)
        
        if collition: 
            explotion_sound = mixer.Sound("hit.wav")
            explotion_sound.play()
            bullet_state == "ready"
            score += 1
            enemy_x[item] = random.randint(0,100)
            enemy_y[item] = random.randint(50, 150)
        enemy(enemy_x[item], enemy_y[item], item)

    if bullet_y <= 0:
        bullet_y = 500
        bullet_state = "ready"

    if bullet_state == "fire":
        fire(bullet_x, bullet_y)
        bullet_y -= bullet_y_change
    

    
 
    player(player_x, player_y)

    text(text_x, text_y)
    
    
    pygame.display.update()