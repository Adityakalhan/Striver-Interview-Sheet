class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        index_map = {nums[i] : i for i in range(n)}
        for i,val in enumerate(nums) :
            if target-val in index_map and index_map[target-val] != i :
                return [i,index_map[target-val]]
        return -1