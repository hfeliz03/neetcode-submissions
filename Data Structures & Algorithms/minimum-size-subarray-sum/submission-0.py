class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target: return 0
        elif sum(nums) == target: return len(nums)
        elif target in set(nums): return 1
        
        n = len(nums)
        l, r = 0, 0
        minLen = n

        curSum = 0
        while r < n:
            if curSum + nums[r] < target:
                curSum += nums[r]
                r += 1
            else:
                minLen = min(minLen, r - l + 1)
                curSum -= nums[l]
                l += 1
        return minLen