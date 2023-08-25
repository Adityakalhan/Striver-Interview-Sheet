def merge(arr,lo,mid,hi) :
    left = lo
    right = mid + 1
    count = 0
    temp = []
    while left <= mid and right <= hi :
        if arr[left] <= arr[right] :
            temp.append(arr[left])
            left += 1
           
        else :
            count += (mid - left + 1)
            temp.append(arr[right])
            right += 1
    while left <= mid :
        temp.append(arr[left])
        left += 1
    while right <= hi :
        temp.append(arr[right])
        right += 1
    
    for i in range(lo,hi + 1) :
        arr[i] = temp[i-lo]
    return count
    
def mergeSort(arr,lo,hi) :
    count = 0
    if lo >= hi :
        return 0
    
    mid = (lo + hi)//2
    count += mergeSort(arr,lo,mid)
    count += mergeSort(arr,mid + 1,hi)
    count += merge(arr,lo,mid,hi)
    return count   
def getInversions(arr, n) :
	# Write your code here.
    count = mergeSort(arr,0,n-1)
    return count
