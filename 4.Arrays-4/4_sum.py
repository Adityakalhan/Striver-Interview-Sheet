class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        prev_i,prev_j = None,None
        res = set()
        for i in range(n) :
            for j in range(i + 1,n) :
                lo,hi = j+1,n-1
                while lo < hi :
                    search = target - (nums[i] + nums[j])
                    sum_window = nums[lo] + nums[hi]
                    if sum_window == search :
                        small_ans = (nums[i],nums[j],nums[lo],nums[hi])
                        res.add(small_ans)
                        lo += 1
                        hi -= 1                    
                    elif sum_window > search :
                        hi -= 1
                    
                    else :
                        lo += 1
        return list(res)
                    