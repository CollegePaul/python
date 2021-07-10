'''
Handling errors
In this example we are trying to divide x by x
if x is = "a" this would crash, but we can catch the error
if x is = 0  this would crash for a different reason.

you can just have 1 except:  and this will catch all errors,
but not give the specific feeback

'''

x = 0
answer = 0

try:
    answer = x / x
except TypeError:
    print("please enter a valid number")
except ArithmeticError:
    print("That value is not allowed")


print("Answer: " , answer) #the program did not crash


'''
We can also raise an exception, this will crash the programm, 2 are shown below.
'''

y = -1
if y < 0:
  raise Exception("Sorry, no numbers below zero")

z = "hello"
if not type(z) is int:
  raise TypeError("Only integers are allowed")


print("our prgramme has raised an error and this line was not printed")