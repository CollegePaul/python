from abc import ABC


class BinaryAdd(ABC):
   
    def add(num1:str, num2:str):
        
        num1_length = len(num1)
        num2_length = len(num2)

        #deal here with unqual lengths

        #adding from lsb to msb
        result = "0" * num1_length  #black bit string for result
        carry = 0
        for bit in range(num1_length-1, -1, -1): 

            #case  1 + 1 + carry0 = 0 + carry1
            if num1[bit] == "1" and num2[bit] == "1" and carry == 0:
                result[bit] = "0"
                carry = 1

            #case  1 + 1 + carry1 = 1 + carry1
            elif num1[bit] == "1" and num2[bit] == "1" and carry == 1:
                result[bit] = "0"
                carry = 1

            #case  1 + 0 + carry0 =  1 + carry0
            elif num1[bit] == "1" and num2[bit] == "0" and carry == 1:
                result[bit] = "1"
                carry = 0

            #case  0 + 1 + carry0 =  1 + carry0
            elif num1[bit] == "0" and num2[bit] == "1" and carry == 1:
                result[bit] = "1"
                carry = 0
            


      