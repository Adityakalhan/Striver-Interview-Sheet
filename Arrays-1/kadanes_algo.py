class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        res = -float("inf")
        s = 0 
        for ele in nums :
            s += ele
            res = max(s,res)
            if s < 0 :
                s = 0
            
        return res