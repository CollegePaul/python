"""
    This code is from Wireframe magazine issue 54
    file:///C:/Users/paulsmith/Downloads/Wireframe54.pdf
    some small changes may be made, or additional or change comments.

"""



class Cpu:
    """this class represents the CHIP 8 CPU"""

    #game ram starts at 0x200 / 512
    PROGRAM_START_ADDRESS  = 0x200
    #the chip 8 works with 16 bit/2 byte opcodes
    WORD_SIZE_IN_BYTES = 2
    #V[15/0xF] is used a carry/no borrow flag for certain ops
    ARITHMETIC_FLAG_REGISTER_ADDRESS = 0xF
    FRAME_BUFFER_WIDTH = 64
    FRAME_BUFFER_HEIGHT = 32

    def _init_(self):
        # 4k of RAM
        self.ram = [0] * 4096
        self.program_counter = self.PROGRAM_START_ADDRESS
        self.index_register = 0
        self.general_purpose_registers = [0] * 16
