def merge(nums,left,mid,right):
    i=left
    j=mid+1
    temp=[]
    while i<=mid and j<=right:
        if nums[i]<nums[j]:
            temp.append(nums[i])
            i+=1
        else:
            temp.append(nums[j])
            j+=1
    while i<=mid:
        temp.append(nums[i])
        i+=1
    while j<=right:
        temp.append(nums[j])
        j+=1
    for i in range(left,right+1): # not high as range excluded the last index [ I already made this mistake]
        nums[i]=temp[i-left]
def mergesort(nums,low,high):
    if low == high:
        return
    mid=(low+high)//2
    mergesort(nums,low,mid)
    mergesort(nums,mid+1,high)
    merge(nums,low,mid,high)
def sort(nums):
    mergesort(nums,0,len(nums)-1)
    return nums


