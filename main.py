import pygame
import random
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode( SIZE )
background = pygame.image.load("eclipse.jpg")

pygame.display.set_caption("Space Invaders")

icon = pygame.image.load("space-invaders (1).png")
pygame.display.set_icon( icon )

enemy_img = pygame.image.load("ufo.png") 
enemy_x = random.randint(0,100)
enemy_y = random.randint(50, 150)
enemy_x_change = 0.2
enemy_y_change = 20


player_ing =  pygame.image.load("nave-espacial.png")
player_x = 360
player_y = 500
player_x_change = 0
def player(x, y):
    screen.blit(player_ing, (x, y))    
def enemy(x, y):
        screen.blit(enemy_img, (x, y)) 

running = True
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                player_x_change -= 1

            if event.key == pygame.K_RIGHT:   
                player_x_change = 1

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_d or pygame.K_a:
                player_x_change = 0

            
    player_x += player_x_change
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736
    enemy_x += enemy_x_change
    if enemy_x >= 736:
        enemy_x -= enemy_x_change
        enemy_x_change = -0.2
        enemy_y += enemy_y_change
    elif enemy_x <= 0:
        enemy_x_change = 0.2
        enemy_y += enemy_y_change
 

   

    RGB = (20,80,120)
    screen.fill( RGB )
    screen.blit(background, (0,0))
    player(player_x, player_y)
    enemy(enemy_x, enemy_y)
    enemy(enemy_x, enemy_y)
    
    pygame.display.update()