#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        #Code here
        if sum(arr) == 0 :
            return n
        hashmap = {}
        s = 0
        maxi = 0
        for i in range(n) :
            s += arr[i]
            if s == 0 :
                maxi = i + 1
            if s in hashmap :
                maxi = max(maxi,i - hashmap[s])
            else :
                hashmap[s] = i
        return maxi