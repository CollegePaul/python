pc = 0
ram = [0]*100
acc = 0
overflow = False
inbox = ""
outbox = ""
halt = False
debug = False

#          INP,STA,INP,ADD,OUT
program = ["901","350","901","150","902","000"]


def reset():
    global pc, ram, acc, overflow, inbox, outbox, halt
    pc = 0
    ram = ["000"]*100  #100 slots of memory
    acc = 0
    overflow = False  #the overflow flag, not implimented yet
    inbox = ""
    outbox = ""
    halt = False
    debug("LMC has been reset")
    

def dump():
    if not debug:
        return
    global pc, ram, acc, overflow, inbox, outbox
    print("PC:",pc)
    print("acc:",acc)
    print("overflow:", overflow)
    print("inbox:", inbox)
    print("outbox:", outbox)
    print("RAM:",ram, "\n")

def load_program(program):
    reset()
    global ram
    for x in range(0, len(program)):
        ram[x] = program[x]
    
    print("Loaded Program into RAM", len(program),"bytes")

def debug(message):
    if debug == True:
        print(message)


def step():
    global halt, ram, pc
    while not halt:
        op = ram[pc]
        output = "STEP: opcode = " + op
        debug(output)
        
        if op == "000": #hlt
            hlt()

        elif op[0] == "1": #add
            add(op[1:])

        elif op[0] == "3": #sta
            sta(op[1:])

        elif op == "901": #inp
            inp()

        elif op == "902": #out
            out()
        else:
            raise Exception("OpCode",op, " not found, program Halting")
            

        pc+=1
    
    #all done








def add(location):
   # print("adding")
    #print(location)
    location = int(location)
    global acc,ram
    value = int(ram[location])
   # print(value)
    acc_value = int(acc)
    acc_value += value
    if acc_value > 999:
        acc_value = (acc_value % 999) - 1
        
    acc = str(acc_value)
    acc_length = len(acc)
    if acc_length == 1:
        acc = "00" + acc
    elif acc_length == 2:
        acc = "0" + acc
    elif acc_length > 3:
        raise Exception("ACC value length > 3")
    else:
        output = "ADDED:", value, "to accummulator, acc:", acc
        debug(output)
            
    return

def sta(location):
    location = int(location)
    if location <0 or location > 99:
        raise Exception("Memory location",location, "is not valid")
    global acc,ram
    ram[location] = acc
    output = "Stored: ",acc, "in memory slot", location
    debug(output)
    return


def inp():
    global acc
    while True:
        acc = input("INPUT VALUE: ")
        val = acc
        try:
            val = int(val)
            if val <0 or val > 999:
                print("Value must be between 0 and 999")
            else:
                break
        except:
            print("Value must be an integer")

def out():
    global acc
    print("OUTPUT: ", acc)
    return


def hlt():
    global halt
    halt = True
    print("Going for coffee break")


load_program(program)
dump()

step()