#Basic Sorting

fruit = ['melon', 'apple', 'orange']

fruit.sort()
print(fruit)
 #['apple', 'melon', 'orange']

fruit.sort(reverse=True)
print(fruit)
 #['orange', 'melon', 'apple']

 #Advanced Sorting
fruits = ['melon', 'pear', 'orange']

def length(item):
    return len(item)

fruits.sort(key=length)
print(fruits)
#['pear', 'melon', 'orange']
