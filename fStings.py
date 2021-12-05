# f-strings require python 3.6 and higher

#insterting variables into a string
name, age = "Paul" , 49
print( f"Hello I am {name}. I am {age}." )
#Hello I am Paul. I am 48.

# this includes ability to do the calculation inline
print (f"{2 * 5}") #10


print(f"{name.lower()} is lowercase.")
#paul

#use to fix decimal places - outputs £10.13
d= 10.1294
print( f"£{d:.2f}" ) #£10.13