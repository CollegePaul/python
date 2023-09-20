#load pygame library
import pygame
import os

#make a window
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

#background
BACKGROUND_IMAGE = pygame.image.load(os.path.join('Assets','space.png'))
BACKGROUND = pygame.transform.scale(BACKGROUND_IMAGE, (WIDTH,HEIGHT))

#the main draw looop
def draw_window():
    WIN.blit(BACKGROUND,(0,0))
    pygame.display.update()

#start the game
def main():
    clock = pygame.time.Clock()
    run = True

    #the main game loop
    while run:
        clock.tick(FPS)

        #process the events
        for event in pygame.event.get():
            #allow the user to quit
            if event.type == pygame.QUIT:
                run = False #exit the run loop

        #draw loop
        draw_window()

    #if we have quit the run loop, close the game window
    pygame.quit()

#make sure the programme will load the main function
if __name__ == "__main__":
    main()