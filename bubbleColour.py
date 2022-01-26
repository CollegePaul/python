#Bubble sort version 2 with swap funciton
from colorama import Fore
from colorama import Style

def swap(data,a,b):
    temp = data[a]
    data[a] = data[b]
    data[b] = temp


def bubble_sort(data):
    n = len(data)
    
    for i in range(0,n-1): #loop over list
        for j in range(0,n-i-1): #loop over the sublist
            swapped = False
            if data[j] > data[j+1]:
                swap(data,j,j+1)
                swapped = True
            if swapped:
                print(f"{Fore.GREEN}Loop: {i} , J: {j} , {data}{Style.RESET_ALL}")
            else:
                print(f"Loop: {i} , J: {j} , {data}")


data = [4,2,5,3,1,7,6]
bubble_sort(data)



print(f"{Fore.GREEN}Sorted: {data} {Style.RESET_ALL}")

