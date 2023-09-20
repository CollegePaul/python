import pygame
import os
from spriteSheet import SpriteSheet
from level import Level

class Player():
    x = 16
    y = 104
    #Images
    #sprite = pygame.image.load(os.path.join('images','characters.png'))
    frames = [] #a list of all the sprites for walking
    frame_no = 0
    #x_offset = [0,1,0,-1,-1,0,1,0]
    x_offset = [0,1,0,-1,1,2,3,2]
   
    y_jump = [4,4,3,3,2,2,1,1,0,0,-1,-1,-2,-2,-3,-3,-4,-4]
    y_jump_counter = 0
    jumping = False
    terminal_velocity = False
    tv_counter = 0
    
    facing = 0 # 0 is right, 4 is left

    def __init__(self,level):
        sprite_sheet = SpriteSheet("characters.png")
        self.level = level
        #this will need to change as he is 10 wide at some points
    
        #right sprites
        sprite = sprite_sheet.get_image(0,0,8,16)
        self.frames.append(sprite)
        sprite = sprite_sheet.get_image(19,0,6,16)
        self.frames.append(sprite)
        sprite = sprite_sheet.get_image(36,0,8,16)
        self.frames.append(sprite)
        sprite = sprite_sheet.get_image(53,0,10,16)
        self.frames.append(sprite)

        #left sprites
        sprite = sprite_sheet.get_image(65,0,10,16)
        self.frames.append(sprite)
        sprite = sprite_sheet.get_image(84,0,8,16)
        self.frames.append(sprite)
        sprite = sprite_sheet.get_image(103,0,6,16)
        self.frames.append(sprite)
        sprite = sprite_sheet.get_image(120,0,8,16)
        self.frames.append(sprite)
        

    def update(self):

        #check block under willy as we may be falling
        under_block = self.level.getBlock(int(self.x/8),int((self.y + 16)/8))


        #if falling cant jump
        #like starting second half of jump routine

        if self.jumping:  #if jumping

            #we can only add the jump counter on if less than list length
            if self.y_jump_counter < len(self.y_jump):
                self.y -= self.y_jump[self.y_jump_counter]
                self.y_jump_counter += 1


            #fallinf
            if under_block == 1 and self.y_jump_counter>9:  #falling only
                 self.jumping = False #hits something
        else: # not jumping
            pass
           


            # #falling - check if hits a platform
            # under_block = self.level.getBlock(int(self.x/8),int((self.y + 16)/8))
            # #print(under_block)
            # if under_block == 1 and self.y_jump_counter>9:  #falling only
            #     self.jumping = False
            #     if self.tv_counter >=4:
            #         print("you dieddddddd")
            #     if self.terminal_velocity == True:
            #         print("you died")
            # elif self.terminal_velocity == False:
            #     if self.y_jump_counter >= len(self.y_jump):
            #         self.terminal_velocity == True
            #         self.y += 4
            #         self.tv_counter += 1
                   
            #     else:#apply vertical movement
            #         self.y -= self.y_jump[self.y_jump_counter]
            #         self.y_jump_counter += 1
                
            
    
        

    def draw(self,surface):
        self.frame_no = int((self.x/2)) % 4 
       
        surface.blit(self.frames[self.frame_no + self.facing], (self.x + self.x_offset[self.frame_no + self.facing],self.y))

    #just need to fix a slight ofset problem on the left face

    def handle_keys(self,key_pressed):
        if key_pressed[pygame.K_o]: #left
            if self.facing == 0:
                self.facing = 4
                
            else:       
                if self.x > 8:
                    self.x -= 2
           
        if key_pressed[pygame.K_p]: #right
            if self.facing == 4:
                self.facing = 0
            else:
                self.x += 2
        
        if key_pressed[pygame.K_SPACE] and self.jumping == False: #jump
            self.jumping = True
            self.y_jump_counter = 0
            self.tv_counter = 0

        #frame will be a mod of position

      