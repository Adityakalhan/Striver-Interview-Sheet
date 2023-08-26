class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxi,start = 0,0
        d = {}
        for i in range(n) :
            if s[i] in d :
                cur = i - start
                if start < d[s[i]] + 1 :
                    start = d[s[i]] + 1
                maxi = max(maxi,cur)
            d[s[i]] = i        
        maxi = max(maxi,n - start)
        return maxi
        