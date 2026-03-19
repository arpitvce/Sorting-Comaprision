import time
import bubble
import mergesort
import random

n=int(input("Enter Size Of Array To Be Sorted:"))
arr=[random.randint(-100000,100000) for _ in range(0,n)]
arr1=arr.copy()
arr2=arr.copy()
# Deep Copying Two Arrays

start=time.perf_counter()
bubble.bubblesort(arr1)
end=time.perf_counter()
print(f"Time by Bubble Sort:{end-start:.6f}")


start=time.perf_counter()
mergesort.sort(arr2)
end=time.perf_counter()
print(f"Time By Merge Sort:{end-start:.6f}")




