import pygame
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

screen = pygame.display.set_mode( SIZE )
pygame.display.set_caption("Space Invaders")

icon = pygame.image.load("space-invaders (1).png")
pygame.display.set_icon( icon )

player_ing =  pygame.image.load("nave-espacial.png")
player_x = 360
player_y = 500
player_x_change = 0
def player(x, y):
    screen.blit(player_ing, (x, y))    

running = True
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_a:
                player_x_change -= 1

            if event.key == pygame.K_d:   
                player_x_change = 1

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_d or pygame.K_a:
                player_x_change = 0

            
    player_x += player_x_change
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    RGB = (20,80,120)
    screen.fill( RGB )
    player(player_x, player_y)
    
    
    pygame.display.update()