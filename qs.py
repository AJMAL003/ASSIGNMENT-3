import time

def partition(arr, low, high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot
 
    for j in range(low, high):
 
       
        if arr[j] <= pivot:
 
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
 
 
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
 
        
        pi = partition(arr, low, high)
 
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
 

arr = [2.5,3.5,3.0,1.2,6.5,8.9,7.4,6.3]
n = len(arr)
start = time.time()
time.sleep(1)
quickSort(arr, 0, n-1)
end = time.time()
print("Sorted array is:")
for i in range(n):
    print("%f" % arr[i])

print("Execution Time: ",end - start-1)
