"""
Problem - remove item from a list

run the code, look at this in debug mode to see what happens


"""

list = ["a","b","c","d","e"]

print("Start: " + str(list))


""" 
Comment out the code below to look at the other examples
use controll /  or  command / to toggle block comment
"""
for i in range(0, len(list)):
    if list[i]=="c":
       # list.remove("c")  #alternative way of removing, also does not work
        del list[i]


print("End: " + str(list))


"""
how can we fix this?
Why does the following example work?

Solution 1
"""

# for i in range( len(list)-1,-1,-1):
#     if list[i]=="c":
#        # list.remove("c")  #will work now also
#         del list[i]

# print("End: " + str(list))


"""
There is a better way
Why is this different ?
"""

# for item in list:
#     if item == "c":
#         list.remove(item)

#print("End: " + str(list))