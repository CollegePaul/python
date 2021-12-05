"""
This module defines the renderer object and realated methods for rendering
"""

import pygame

WHITE = pygame.Color(255, 255, 255)
BLACK = pygame.Color(0,0,0)

SCALE = 10

#the CHIP-8 display ran at 64 * 32 Pixels, so its scaled for display on modern SCREEN

screen = pygame.display.set_mode((640,320))

def render(frame_buffer):
    """This method will draw everything"""

    screen.fill(BLACK)

    for x in range(64):
        for y in range(32):
            if frame_buffer[x][y]:
                pygame.draw.rect(
                    screen, 
                    WHITE, 
                    (x * SCALE, y * SCALE, SCALE, SCALE))
    
    pygame.display.update()