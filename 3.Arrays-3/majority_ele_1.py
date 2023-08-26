class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        cnt = 1
        cnadidate = nums[0]
        for ele in nums[1:] :
            if ele == cnadidate :
                cnt += 1
            else :
                cnt -= 1
                if cnt <= 0 :
                    cnadidate = ele
                    cnt = 1
        return cnadidate