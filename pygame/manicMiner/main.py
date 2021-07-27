import pygame
import os
from player import Player
from spriteSheet import SpriteSheet
from level import Level

pygame.init()
WIDTH, HEIGHT = 256, 192
SCALE = 3

WIN = pygame.display.set_mode((WIDTH*SCALE, HEIGHT*SCALE)) #Scaled display
pygame.display.set_caption("Manic Miner")

#The surface that will be drawn on
SCREEN = pygame.Surface((WIDTH,HEIGHT))
BLOCKS = SpriteSheet("blocks.png")
FPS = 12

#Global colours
B_RED = (255,0,0)
RED = (215,0,0)

#Images
BACKGROUND = pygame.image.load(os.path.join('images','window.png'))

FONT = pygame.font.Font("zxsp.ttf", 8)

level = Level("Central Cavern",1,BLOCKS)
player = Player(level)
air = 224



#Main draw function
def draw_window():
    
    #pygame.draw.rect(SCREEN,[255,255,255],[0,0,WIDTH,HEIGHT], 0)
    SCREEN.blit(BACKGROUND, (0,0)) # The main background for each level

    player.draw(SCREEN)

   

    #draw the current level
    level.draw(SCREEN,FONT)

    pygame.draw.rect(SCREEN, [255,255,255], [32, 138, air, 4], 0)
    
    #scale the surface onto our scaled window and draw
    WIN.blit(pygame.transform.scale(SCREEN, WIN.get_rect().size),(0,0))
    pygame.display.update()

#Main Gmae loop
def main():
    
    clock = pygame.time.Clock()
    tick_count =0

    run = True
    while run:
        clock.tick(FPS)
        tick_count+=1
        if tick_count == 60: 
            tick_count = 0
        #loop over all of the pygame events
        for event in pygame.event.get():
            #allow the user to quit
            if event.type == pygame.QUIT:
                run = False

        #best keeping track of this in the player itself
        #if tick_count % 2 == 0:
        global air
        #air -=1
        
        key_pressed = pygame.key.get_pressed()
        player.handle_keys(key_pressed)

        player.update()


        draw_window()

    pygame.quit()


if __name__ == "__main__":
    main()
