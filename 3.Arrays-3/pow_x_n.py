class Solution:
    def myPow(self, x: float, n: int) -> float:
        def half_power(x,p) :
            if p == 0 or p == 1 :
                return x ** p
            if p%2 == 0 :
                mul = half_power(x,p//2)
                return mul * mul
            else :
                mul = half_power(x,p-1)
                return x * mul 
        if n < 0 :
            return 1/half_power(x,-n)
        return half_power(x,n)