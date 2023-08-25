def repeated(arr,n) :
    slow = fast = arr[0]-1

    while True :
        slow = arr[slow] - 1
        fast = arr[arr[fast]] - 1
        if slow == fast :
            break
    slow = arr[0]
    while fast != slow :
        fast = arr[fast] - 1
        slow = arr[slow] - 1
    
    return slow + 1
def missingAndRepeating(arr, n):
    # Write your code here
    rep = repeated(arr,n)
    s = sum(arr)
    actual_sum = (n*(n+1))/2
    diff = actual_sum - s
    missing = rep - diff

    return [rep,missing]
    