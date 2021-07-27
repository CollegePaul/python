#tutorial from Tech with Tim

import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My first game!")

WHITE = (255,255,255)
BLACK = (0, 0, 0)

FPS = 60
VEL = 4 #ship speed
BULLET_VEL = 7
BORDER = pygame.Rect((WIDTH/2) -5, 0, 10, HEIGHT)
MAX_BULLETS = 3

#background
BACKGROUND_IMAGE = pygame.image.load(os.path.join('Assets','space.png'))
BACKGROUND = pygame.transform.scale(BACKGROUND_IMAGE, (WIDTH,HEIGHT))

#spaceship size
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 40, 55

#yellow ship
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets','spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_HEIGHT, SPACESHIP_WIDTH)), 90) #resize the ship

#red ship
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets','spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_HEIGHT, SPACESHIP_WIDTH)),270) #resize the ship

def draw_window(red, yellow):
    #WIN.fill(WHITE) #background colour
    WIN.blit(BACKGROUND,(0,0))
    pygame.draw.rect(WIN,BLACK, BORDER)

    #pygame.draw.rect(WIN,BLACK, yellow) #debug ship collision area
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))



    #redraw display
    pygame.display.update()

def yellow_handle_movement(key_pressed, yellow):
    if key_pressed[pygame.K_a] and yellow.x - VEL > 0: #left
        yellow.x -= VEL
    if key_pressed[pygame.K_d] and yellow.x + VEL + SPACESHIP_WIDTH < BORDER.x: #right
        yellow.x += VEL
    if key_pressed[pygame.K_w] and yellow.y - VEL > 0: #up
        yellow.y -= VEL
    if key_pressed[pygame.K_s] and yellow.y + VEL + SPACESHIP_HEIGHT < HEIGHT: #down
        yellow.y += VEL

def red_handle_movement(key_pressed, red):
    if key_pressed[pygame.K_j] and red.x - VEL > BORDER.x + 10: #left
        red.x -= VEL
    if key_pressed[pygame.K_l] and red.x + VEL + SPACESHIP_WIDTH < WIDTH: #right
        red.x += VEL
    if key_pressed[pygame.K_i] and red.y - VEL > 0: #up
        red.y -= VEL
    if key_pressed[pygame.K_k] and red.y + VEL + SPACESHIP_HEIGHT < HEIGHT: #down
        red.y += VEL
        
def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            #1.06 https://www.youtube.com/watch?v=jO6qQDNa2UY
            yellow_bullets.remove(bullet)

def main():
    #red ship position
    red = pygame.Rect(700,300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100,300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    yellow_bullets = []
    red_bullets = []

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        #loop over all of the pygame events
        for event in pygame.event.get():
            #allow the user to quit
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_v and len(yellow_bullets<MAX_BULLETS):
                    bullet = pygame.Rect(yellow.x + SPACESHIP_WIDTH, yellow.y + (SPACESHIP_HEIGHT/2) -2, 10,4)
                    yellow_bullets.append(bullet)

                if event.key == pygame.K_n and len(red_bullets<MAX_BULLETS):
                    bullet = pygame.Rect(red.x , red.y + (SPACESHIP_HEIGHT/2) -2, 10,4)
                    red_bullets.append(bullet)

        #get the user input
        key_pressed = pygame.key.get_pressed()
        yellow_handle_movement(key_pressed, yellow)
        red_handle_movement(key_pressed, red)


        #draw loop
        draw_window(red, yellow)

    pygame.quit()






if __name__ == "__main__":
    main()
