class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        quads = set()
        for a in range(n-3):
            for b in range(a+1,n-2):
                l, r = b + 1,  n-1
                curTarget = nums[a] + nums[b]
                while l < r: 
                    if nums[l] + nums[r] + curTarget == target: 
                        quads.add((nums[a], nums[b], nums[l], nums[r]))
                        l += 1
                        r -= 1
                    elif nums[l] + nums[r] + curTarget > target: 
                        r -= 1
                    else: 
                        l += 1
        return [list(quad) for quad in quads]