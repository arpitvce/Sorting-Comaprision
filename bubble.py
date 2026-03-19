def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(i,len(arr)-1):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

