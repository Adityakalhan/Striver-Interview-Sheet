class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        hs = set(nums)
        max_len = 0
        
        for ele in nums :
            cur = 1
            l = 1
            if ele-1 not in hs :
                while ele + l in hs :
                    cur += 1
                    l += 1
            max_len = max(cur,max_len)
        
        return max_len