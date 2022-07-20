def bubble_sort(data):
    n = len(data)
    
    for i in range(0,n-1): #loop over list
        for j in range(0,n-i-1): #loop over the sublist
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j] #swap
    return data

unsorted_data = [4,2,5,3,1,7,6]
sorted_data = bubble_sort(unsorted_data)
print(sorted_data)

