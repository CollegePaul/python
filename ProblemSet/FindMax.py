#Find the maximum number in a list

def find_max (L):
    max = 0
    for x in L:
        if x > max:
            max = x
    return max

nums = [2,34,24,63,82,25,78,21,43,73,93,49,48,65,36]

print(find_max(nums))


#linear time
