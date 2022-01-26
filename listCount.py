#list count

#built in function
numbers = [2, 3, 5, 2, 11, 2, 7]
count_n = numbers.count(2)
print('Built in, Count of 2:', count_n)

#custom function
def count(data,item):
    count = 0
    for i in range(0, len(data)-1):
        if item == data[i]:
            count+=1
    return count

count_n = count(numbers, 2)
print('Custom, Count of 2:', count_n)
