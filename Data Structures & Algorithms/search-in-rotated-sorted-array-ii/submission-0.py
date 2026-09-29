class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # return True if target in set(nums) else False 
        li, ri = 0, len(nums) - 1
        while li <= ri:
            mi = (li + ri) // 2
            if nums[mi] == target: return True
            if nums[li] == nums[mi] == nums[ri]:
                li += 1
                ri -= 1
            elif nums[li] <= nums[mi]:
                # left half sorted
                if nums[li] <= target < nums[mi]:
                    ri = mi - 1
                else:
                    li = mi + 1
            else:
                # right half sorted
                if nums[mi] < target <= nums[ri]:
                    li = mi + 1
                else:
                    ri = mi - 1
        return False   