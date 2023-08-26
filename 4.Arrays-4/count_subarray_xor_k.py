def subarraysWithSumK(a: [int], b: int) -> int:
    ans = 0
    n = len(a)
    for i in range(n) :
        xorr = 0
        for j in range(i,n) :
            xorr = xorr ^ a[j]
            
            if xorr == b :
                ans += 1
    return ans
def subarraysWithSumK(a: [int], k: int) -> int:
    cnt,hs,xr = 0,{0 : 1},0
    for ele in a :
        xr = xr ^ ele
        x = xr ^ k 
        if x in hs :
            cnt += hs[x]
        hs[xr] = hs.get(xr,0) + 1
    return cnt