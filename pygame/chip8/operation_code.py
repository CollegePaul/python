class Opcode:
    """This class represents the instructions and data of an opcode."""

    def __init__(self, word) -> None:
        """This class takes in a 2 byte value/word and parses the bytes to store them in
        different attributes for later use.
        """
        #use bitwise AND with a mask to extract nibbles
        #a word should be no more than 16 bits

        self.word = word & 0xFFFF

        #we just want the most significan nibble, so bitshift right
        self.a = (word & 0xF000) >> 12

        self.nnn = word & 0x0FFF
        self.nn = word & 0x00FF
        self.n = word & 0x000F

        #where we dont use the lower nibbles, bitshift
        self.x = (word & 0x0F00) >> 8

        #eg we want 0x4 not 0x40
        self.y = (word & 0x00F0) >> 4

        #structure    a,x,y,n or OxAXYN are individual nibbles
        #opcode.word, opcode.nn, and opcode.nnn are groups of nibbles.


