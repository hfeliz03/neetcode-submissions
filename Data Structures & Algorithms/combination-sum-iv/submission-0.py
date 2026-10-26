from functools import cache
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(rem):
            if rem == 0: return 1
            if rem < 0: return 0

            res = 0
            for num in nums:
                res += dfs(rem - num)

            return res

        return dfs(target)