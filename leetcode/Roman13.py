
def romanToInt( s):
    """
    :type s: str
    :rtype: int
    """
    
    values = {
                    'MMM': 3000,
                    'MM': 2000,
                    'CCC': 300,
                    'CC' : 200,
                    'XXX': 30,
                    'XX': 20,
                    'III': 3,
                    'II': 2,
                    'IV': 4,
                    'IX': 9,
                    'XL': 40,
                    'XC': 90,
                    'CD': 400,
                    'CM': 900,
                    'X': 10,
                    'L': 50,
                    'C': 100,
                    'D': 500,
                    'M': 1000,
                    'I': 1,
                    'V': 5,
            }
    
    total = 0
    
    for k in values:
        if k in s:
            total += values[k]
            s = s.replace(k, "")
            
   
    
    return total

answer = romanToInt("MDCCCLXXXIV") #621  i get 611
print(answer)