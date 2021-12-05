#sets

fruit = {"apple", "banana", "cherry"}
print(fruit) 
#{'apple', 'cherry', 'banana'}

print(len(fruit)) #3
print(type(fruit)) #<class 'set'>

print("banana" in fruit) #True
fruit.add("orange") #adds orange

fruit.remove("banana") #removes banana

for x in fruit:
  print(x)
#apple
#cherry
#orange