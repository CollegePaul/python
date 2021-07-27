import pygame
import os

from pygame import draw
from spriteSheet import SpriteSheet

class Level():
    #level will be load from a file
    platforms = [[0,0,0,0,0,0,0,0,"k",0,"i",0,0,0,0,"i",0,0,0,0,0,0,0,0,0,0,0,0,"k",0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"k",0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"p","k",0,0,"p",0,0,0,0],
                 [1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"k"],
                 [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"w","w","w",0,"p",0,0,0,0,0,0,0,0,0,0],
                 [1,1,1,1,0,0,0,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,"p",0,0,0,0,0,0,0,"w","w","w",2,2,2,2,2,2,1,1,1],
                 [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,"x","x"],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"x","x"],
                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

    keycount = 0

    def __init__(self,title,number,blocks):
        self.title = title
        self.number = number
        self.wall = blocks.get_image(0,0,8,8)
        self.key = blocks.get_image(0,32,8,8)
        self.ice = blocks.get_image(0,40,8,8)
        self.ground = blocks.get_image(0,8,8,8)
        self.plant = blocks.get_image(8,40,8,8)
        self.plant.fill((0,225,0), special_flags = pygame.BLEND_MULT) #this will depend on the level
        self.rubble = blocks.get_image(8,8,8,8)
        self.conveyer = blocks.get_image(8,16,8,8)

        
    def draw(self,surface,FONT):
        #draw the side walls
        for n in range(0,16):
            surface.blit(self.wall, (0,n*8))
            surface.blit(self.wall, (248,n*8))
        
        #draw the level title
        self.drawTitle(surface,FONT)

        self.drawBlocks(surface)


    def drawTitle(self,surface, FONT):

         #to be put in a function drawTitle maybe in level class
        # (256 - (len string * 8)) /2 = 72
        text_image = FONT.render(self.title, True, (0,0,0)) #Render text image.
        surface.blit(text_image, (72,128)) #Draw image to screen.

    def drawBlocks(self,surface):
        h,v = 1,0
        tempKey = self.key 
        tempKey.fill((h*3,h*3,0), special_flags = pygame.BLEND_RGB_SUB)
        for row in self.platforms:
            for block in row:
                if block == 0:
                    h+=1
                    continue
                if block == "k": #key / collectable
                    surface.blit(tempKey, (h*8,v*8))
                if block == "i": #iceicle
                    surface.blit(self.ice, (h*8,v*8))
                if block == 1: #ground
                    surface.blit(self.ground, (h*8,v*8))
                if block == "p": #plant
                    surface.blit(self.plant, (h*8,v*8))
                if block == 2: #plant
                    surface.blit(self.rubble, (h*8,v*8))
                if block == 5: #conveyer
                    surface.blit(self.conveyer, (h*8,v*8))
                if block == "w": #conveyer
                    surface.blit(self.wall, (h*8,v*8))    
                h += 1
            h = 1
            v += 1

    def getBlock(self,x,y):
        if y>15:
             return 1
        return self.platforms[y][x]