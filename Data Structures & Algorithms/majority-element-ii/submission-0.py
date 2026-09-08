class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        twoMost = defaultdict(int)
        for num in nums:
            twoMost[num] += 1

        def getMax(dictionary):
            maxAppears = -1
            maxAppearsVal = -1
            for key, value in twoMost.items():
                if value > maxAppearsVal:
                    maxAppears = key
                    maxAppearsVal = value
            return (maxAppears, maxAppearsVal)

        top1, top1Val = getMax(twoMost)
        if top1Val <= len(nums)//3: return []
        del twoMost[top1]

        top2, top2Val = getMax(twoMost)
        if top2Val <= len(nums)//3: return [top1]

        return [top1, top2]