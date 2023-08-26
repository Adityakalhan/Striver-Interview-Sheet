
class Solution:
    def merge(self,arr,low,mid,high) :
        left = low
        right = mid + 1
        temp = []
        while left <= mid and right <= high :
            if arr[left] <= arr[right] :
                temp.append(arr[left])
                left += 1
            else :
                temp.append(arr[right])
                right += 1
        while left <= mid :
            temp.append(arr[left])
            left += 1
        while right <= high :
            temp.append(arr[right])
            right += 1
        for i in range(low,high + 1) :
            arr[i] = temp[i - low]
        
    def mergeSort(self,arr,low,high) :
        count = 0 
        if low >= high :
            return 0
        mid = (low + high)//2
        count += self.mergeSort(arr,low,mid)
        count += self.mergeSort(arr,mid + 1,high)
        count += self.countPairs(arr, low, mid, high)
        self.merge(arr,low,mid,high)
        return count
    def countPairs(self,arr, low, mid, high):
        right = mid + 1
        count = 0
        for i in range(low,mid + 1) :
            while right <= high and arr[i] > arr[right] * 2 :
                right += 1
            count += (right - (mid + 1) )
        return count


    def reversePairs(self, nums: list[int]) -> int:
        c = self.mergeSort(nums,0,len(nums) - 1)
        return c