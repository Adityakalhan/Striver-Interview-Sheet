class Solution:
    def getSmallest(self,arr) :
        res = float("inf")
        ind = -1
        for i,val in enumerate(arr) :
            if val < res :
                res = val
                ind = i
        return ind,res

    def swap(self,nums,i,j) :
        nums[i],nums[j] = nums[j],nums[i]

    def nextGreater(self,arr,ele) :
        res = float("inf")
        ind = -1
        for i,val in enumerate(arr) :
            if val > ele and res > val :
                res = val
                ind = i
        return ind,val

    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        ### Phase 1 -> swapping with the next greater element
        n = len(nums)
        last,prev = n-1,n-2
        while prev >= 0 :
            ind,val = self.nextGreater(nums[prev + 1:],nums[prev]) 
            if ind != -1 :
                break
            prev -= 1

        if prev == -1 :
            nums.reverse()
            return
        self.swap(nums,ind+prev+1,prev)

        #Phase 1 complete
        #Phase 2 -> Keep Replacing with smallest element to the right
        
        ptr = prev + 1
        while ptr < n :
            ele = nums[ptr]
            ind,val = self.getSmallest(nums[ptr+1 : ])
            if ind == -1 :
                break
            if val < ele :
                self.swap(nums,ind + ptr + 1,ptr)

            ptr += 1