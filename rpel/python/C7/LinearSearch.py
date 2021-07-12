def linearsearch(arr, x):
   for i in range(len(arr)):
      if arr[i] == x:
         return i
   return -1


arr = ['p','y','t','h','o','n']

index = linearsearch(arr,'h')
if index>-1:
    print(index)
else:
    print("not found")
    