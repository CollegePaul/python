from operation_code import Opcode
import operations


def find_operation(word):
    opcode = Opcode(word)

    if word == 0x00E0:
        return operations.clear_display

    if word == 0x00EE:
        return operations.return_from_function

    if opcode.a == 0x1:
        return operations.goto

    if opcode.a == 0x2:
        return operations.call_function
    
    if opcode.a == 0x3:
        return operations.skip_if_equal

    if opcode.a == 0x4:
        return operations.skip_if_not_equal
    
    if opcode.a == 0x5:
        return operations.skip_if_x_y_equal

    if opcode.a == 0x6:
        return operations.set_x
        

