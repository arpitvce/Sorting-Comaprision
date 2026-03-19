from bubble import bubblesort
from mergesort import sort
import time
import random
import matplotlib.pyplot as plt

def measuretime(func,arr):
    start=time.perf_counter()
    func(arr.copy())
    end=time.perf_counter()
    return end-start

sizes=[0,10,100,200,300,400,500,600,700,800,900,1000,2000]
arraybubble=[]
arraymerge=[]


def average_time(func,sizes):
    for size in sizes:
        arr=[random.randint(-10000,10000) for _ in range(size)]
        t1=func(bubblesort,arr.copy())
        arraybubble.append(t1)
        t2=func(sort,arr.copy())
        arraymerge.append(t2)


    timeb=sum(arraybubble)/len(arraybubble)
    timem=sum(arraymerge)/len(arraymerge)
    return timeb,timem

a,b=average_time(measuretime,sizes)


plt.plot(sizes,arraybubble,label="bubblesort")
plt.plot(sizes,arraymerge,label="mergesort")

plt.xlabel("Input Size")
plt.ylabel("Algorithm Runtime")
plt.title("Algorithm Comparision")
plt.legend()
plt.show()

plt.savefig("result.png")

print("Average Time of Bubble sort:",a)
print("Average Time of Merge Sort:",b)





