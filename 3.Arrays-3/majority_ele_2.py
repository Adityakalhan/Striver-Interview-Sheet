class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        n,cnt1,cnt2,el1,el2 = len(nums),0,0,None,None
        
        for i in range(n) :
            if cnt1 == 0 and el2 != nums[i] :
                cnt1 = 1
                el1 = nums[i]
            elif cnt2 == 0 and el1 != nums[i] :
                cnt2 = 1
                el2 = nums[i]
            elif nums[i] == el1 :
                cnt1 += 1
            elif nums[i] == el2 :
                cnt2 += 1
            else :
                cnt1 -= 1
                cnt2 -= 1
        print(cnt1,cnt2)
        res = set()
        counter1,counter2 = 0,0
        for ele in nums :
            if ele == el1 :
                counter1 += 1
                if counter1 > n//3 :
                    res.add(el1)
            elif ele == el2 :
                counter2 += 1
                if counter2 > n//3 :
                    res.add(el2)
        return list(res)