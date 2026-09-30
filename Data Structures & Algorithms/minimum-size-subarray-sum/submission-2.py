class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, 0
        minLen = n + 1

        curSum = 0
        while r < n:
            if curSum + nums[r] < target:
                curSum += nums[r]
                r += 1
            else:
                minLen = min(minLen, r - l + 1)
                curSum -= nums[l]
                l += 1
        return minLen if minLen <= n else 0