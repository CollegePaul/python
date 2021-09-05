"""
    This code is from Wireframe magazine issue 54
    file:///C:/Users/paulsmith/Downloads/Wireframe54.pdf
    some small changes may be made, or additional or change comments.

"""

from operation_code import Opcode
import operation_mapping
import font


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

    def __init__(self):
        # 4k of RAM
        self.ram = [0] * 4096
        self.program_counter = self.PROGRAM_START_ADDRESS
        self.index_register = 0
        self.general_purpose_registers = [0] * 16
        self.delay_timer = 0
        self.stack = []
        self.stack_pointer = 0
        self.keys = set()
        self.frame_buffer = [[bool()] * 32 for i in range(64)]
        self._load_font()
        self._current_word = 0
        self._current_operation = None
    
    def key_down(self, key):
        """This method sets a key as pressed"""
        if key not in self.keys:
            self.keys.add(key)

    def key_up(self, key):
        """This method sets a key as released"""
        if key is self.keys:
            self.keys.remove(key)
    
    def move_to_next_instruction(self):
        self.program_counter += Cpu.WORD_SIZE_IN_BYTES

    def move_to_previous_instruction(self):
        self.program_counter -= Cpu.WORD_SIZE_IN_BYTES

    def load_rom(self, rom_bytes):
        for i, byte_value in enumerate(rom_bytes):
            self.ram[Cpu.PROGRAM_START_ADDRESS + i] = byte_value
    
    def set_arithmetic_flag(self):
        self.general_purpose_registers[self.ARITHMETIC_FLAG_REGISTER_ADDRESS] = 1

    def clear_arithmetic_flag(self):
        self.general_purpose_registers[self.ARITHMETIC_FLAG_REGISTER_ADDRESS] = 0

    def emulate_cycle(self):
        self._current_word = self.fetch_word()

        opcode = Opcode(self._current_word)
        self._current_operation = operation_mapping.find_operation(self._current_word)

        self.move_to_next_instruction()

        self._current_operation(opcode, self)

    def fetch_word(self):
        word = self.ram[self.program_counter] << 8 | self.ram[self.program_counter +1]
        return word
    
    def update_timers(self):
        if self.delay_timer > 0:
            self.delay_timer -= 1
    
    def _load_font(self):
        offset = 0x0
        for item in font.DATA:
            self.ram[offset] = item
            offset += 1
            






