#Bubble sort version 2 with swap funciton

def swap(data,a,b):
    temp = data[a]
    data[a] = data[b]
    data[b] = temp


def bubble_sort(data):
    n = len(data)
    
    for i in range(0,n-1): #loop over list
        for j in range(0,n-i-1): #loop over the sublist
            if data[j] > data[j+1]:
                swap(data,j,j+1)
            print(f"Loop: {i} , J: {j} , {data}")


data = [4,2,5,3,1,7,6]
bubble_sort(data)



print(f"Sorted: {data}")


