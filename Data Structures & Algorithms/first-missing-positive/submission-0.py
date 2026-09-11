class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums) 
        i = 0
        while i < n:
            correct = nums[i] - 1
            if 1 <= nums[i] <= n and nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1

        for i, num in enumerate(nums):
            if num != i + 1: return i + 1

        return len(nums) + 1
