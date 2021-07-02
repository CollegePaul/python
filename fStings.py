# f-strings require python 3.6 and higher

#insterting variables into a string
name = "Paul"
age =  48
print( f"Hello I am {name}. I am {age}." )

# this includes ability to do the calculation inline
print (f"{2 * 5}")

#rmove capitals
print(f"{name.lower()} is my name with no captials.")

#use to fix decimal places - outputs £10.13
d= 10.1294
print( f'£{d:.2f}' )