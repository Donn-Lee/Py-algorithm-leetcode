def bubble_sort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(0,i):
            if arr[j]> arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr
import random
x = random.sample(range(1000),10)
print(bubble_sort(x))