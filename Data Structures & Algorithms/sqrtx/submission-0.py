class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: return x
        if x < 4: return 1
        l, r = 2, x/2
        while l <= r:
            mid = (l + r) / 2
            if math.floor(mid*mid) == x: return math.floor(mid)
            elif mid*mid > x: r = mid 
            else: l = mid
        return 0