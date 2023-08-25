class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        hashmap = {}
        for ele in nums :
            if ele not in hashmap :
                hashmap[ele] = 1
            else :
                hashmap[ele] += 1
        res = []
        for i in range(3) :
            if i in hashmap :
                for j in range(hashmap[i]) :
                    res.append(i)
            else :
                continue
        for i in range(len(res)) :
            nums[i] = res[i]
        return nums
    
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red,blue,i = 0,len(nums) - 1,0

        while blue >= i :
            if nums[i] == 0 :
                nums[red],nums[i] = nums[i],nums[red]
                red += 1
                i += 1
            elif nums[i] == 2 :
                nums[blue],nums[i] = nums[i],nums[blue]
                blue -= 1
            else :
                i += 1
        return nums