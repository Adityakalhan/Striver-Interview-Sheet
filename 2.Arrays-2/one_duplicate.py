class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow = fast = nums[0]

        while True :
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast :
                break

        slow = nums[0]
        while fast != slow :
            fast = nums[fast]
            slow = nums[slow]
        
        return slow