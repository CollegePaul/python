import math

negative_flag = False #is the number negative
binary_string = "" #used to store the number as a string
whole_flag = False #is the number more than 1
BIAS = 127 #the bias for the exponent (constant)
bias_exponent_string = "" #the final output of the exponent
mantissa = "" #the output for the mantissa

def whole_to_bin(num):
    """
    Accepts a whole number and converts this into a
    sring of bits
    """
    if num < 0:
        raise Exception ("Must be a postive number")

    if num == 0:
        return "0"

    out = ""
    n_bits = int(math.log2(num)) + 1       # 2**6      = 32       log2(32)  = 6
    print("BITS Needed: " + str(n_bits))
    max = 2**n_bits 

    while max>= 1:
        if  num >= max:
            out += "1"
            num = num - max
        else:
            out += "0"
        max = max/2

    out = out[1:]
    return out

def fractonal_to_bin(num):
  depth = 64 #must be at least 23 but more will be often needed for rounding or other situations
  output = ""
  counter = 0
  while True:
    num = num * 2

    if num >= 1:
      output += "1"
      num = num - 1
    else:
      output += "0"

    if num == 0:
      break

    counter += 1
    if counter > depth:
      break

  return output


while True:
    number = input("\033[0;39mEnter number to convert: ")
    try:
        number = float(number)
        break
    except:
        print("please enter a valid number")

#zero
if number == 0:
    print("\033[96m0 \033[94m00000000 \033[92m00000000000000000000000")
    raise SystemExit(0)

#Sign
if number < 0:
    negative_flag = True
    number = number * -1 #change to a positive

#whole number part
whole_number = math.floor(number)
whole_number_string = whole_to_bin(whole_number)
if whole_number > 0: 
    whole_flag = True #used to check if the exponent will positive or negative(pre bias)

#decimal part
decimal_number = number - whole_number
decimal_number_string = fractonal_to_bin(decimal_number)
print(whole_number_string)
print(decimal_number_string)

#calculate the exponent
if whole_flag == True:  #the number is 1 or more and has a positve exponent
    exponent = len(whole_number_string) -1
else: 
    #the number will have a -exponent
    counter = 0
    while True:
        if decimal_number_string[counter] == "1":
            break
        counter = counter + 1
    exponent = (counter + 1 ) * -1 

print("Exponent: ", exponent)
biased_exponent = exponent + BIAS
print("Biased Exponent: ", biased_exponent)

bias_exponent_string = whole_to_bin(biased_exponent)
print(bias_exponent_string)
if len(bias_exponent_string) < 8:
    missing = 8 - len(bias_exponent_string)
    newString = "0" * missing
    bias_exponent_string = newString + bias_exponent_string
print(bias_exponent_string)

#calculate the mantissa
if whole_flag == True: #if the number is >= 1 then the number will be added to the mantisa at the start
    whole_number_string= whole_number_string[1:] #take of the implied bit
    #print(whole_number_string)
    mantissa = whole_number_string + decimal_number_string
    mantissa = mantissa[:23] #truncate to 23 (should have rounding here)
    
else:
    #if the number is <0 then remove any leading 0's and the implied bit
    mantissa = decimal_number_string
    mantissa = mantissa[abs(exponent):]
    if len(mantissa) < 23: #add missing zeros if mantiss is not long enough
        missing = 23 - len(mantissa)
        newString = "0" * missing
        mantissa = mantissa + newString
        
       
    if len(mantissa) > 23:
        mantissa = mantissa[0:23] #truncate to 23 (should have rounding here)
 
print("Mantissa:" ,mantissa)
