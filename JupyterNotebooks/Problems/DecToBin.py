"""
Decimal to Binary
Your task is to make a function that will convert a whole number in the range 0 to 255 into an 8 digit string, to represent that number in binary.

Eg.  12 in decimal would output "00001100"
"""

numbers = [128,64,32,16,8,4,2,1]

def get_number(min, max):
    done = False

    while not done:
        num = input(f"Enter number ({min} - {max}): ")
        try:
            num = int(num)
            
            if num < min or num > max:
                print(f"Number out of range ({min} to {max})")
            else:
                done = True
        except:
            print("Please enter a whole number")

    return num

def dec_to_bin_8():
    n = get_number(0, 255)

    bin_nums = [128,64,32,16,8,4,2,1]
    output = ""

    for i in range(0,8):
        if n >= bin_nums[i]:
            output = output + "1"
            n = n - bin_nums[i]
        else:
            output = output + "0"
    return output


print(dec_to_bin_8())
        



