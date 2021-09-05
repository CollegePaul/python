"""This is the entry point to the programme"""

import argparse
import keyboard_input
import renderer
import rom_loader
import pygame

from cpu import Cpu

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--rom", required = True, type = str,
        help="the name of the rom to run in the emulator")
    args = parser.parse_args()

    cpu = Cpu()
    clock = pygame.time.Clock()
    rom_bytes = rom_loader.get_rom_bytes(args.rom)
    cpu.load_rom(rom_bytes)
     
    pygame.deisplay.set_caption("pychip8")
    pygame.init()

    #main looop
    while True:
        keyboard_input.handel_input(cpu)

        #runs best at 500hz
        #update loop runs at 60 fps. 60 * 8 = 480 whic is close

        for _ in range(8):
            cpu.emulate_cycle()

            cpu.update_timers()
            renderer.render(cpu.frame_buffer)

            #delay until next frame
            clock.tick(60)