#UGHHHH I WAS SO CLOSE 
class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def canSplit(largest):
            subarray = 0
            curSum = 0
            for n in nums:
                curSum += n
                if curSum > largest:
                    subarray += 1
                    curSum = n

            return subarray + 1 <= k


        l = max(nums)
        r = sum(nums)
        res = r
        while l <= r:
            m = l + ((r - l) // 2)

            if canSplit(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res

        
                