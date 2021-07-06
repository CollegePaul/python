#solution 1
def fizbuzz1():
    c3 = 1
    c5 = 1
    n=1
    while n<= 100:
        if c3 == 3 and c5 == 5:
            print("Fizzbuzz")
            c3=0
            c5=0
        elif c3 == 3:
            print("Fizz")
            c3=0
        elif c5 == 5:
            print("Buzz")
            c5=0
        else:
            print(n)
        n+=1
        c3+=1
        c5+=1

#solution 2
def fizbuzz2():
    for n in range(1,101):
        if n%3 == 0 and n%5 == 0:
            print("Fizzbuzz")
        elif n%3 == 0:
            print("Fizz")
        elif n%5 == 0:
            print("Buzz")
        else:
            print(n)

# soution 3
def fizbuzz3():
    modList = [(3,"Fizz"),(5,"Buzz")]
    
    for i in range(1,101):
        out = ""
        for mod in modList:
            if i % mod[0] == 0:
                out += mod[1]
        
        if out== "":
            print(i)
        else:
            print(out)


fizbuzz3()