
#binary search
data = [1,3,6,8,12,13,16,19,21,24,25,40,45,50]
val =  12
found = False
index_pos = -1


while not found:
    mid_index = len(data)//2
    mid_value = data[mid_index]
    if val == mid_value:
        found = True
    elif val < mid_value:
        data = data[:mid_index]
    else:
        index_pos += mid_index
        data = data[mid_index:]

    if len(data) == 1:
        if val == data[0]:
            found = True
        break

if found:   
    print("Found")
else:
    print("Not found")

        
    