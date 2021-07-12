s = "AB340E"
#should be 171,52,14

def hexToDec(hex):
    try:
        int(hex, 16)
        return int(hex,16)
    except ValueError:
        return ("not a valid hex")
        
for a in range(0,6,2):
    print(hexToDec(s[a]+s[a+1]))