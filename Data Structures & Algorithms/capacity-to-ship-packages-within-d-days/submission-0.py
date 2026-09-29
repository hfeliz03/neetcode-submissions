class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        maxCap = sum(weights)
        minCap = max(weights)
        def greedy(capacity):
            curDays = 1
            curCap = capacity
            for w in weights:
                if curCap - w >= 0:
                    curCap -= w
                else:
                    curCap = capacity - w
                    curDays += 1

            return curDays

        while minCap < maxCap:
            mid = (maxCap + minCap) // 2
            daysSpent = greedy(mid)
            if daysSpent <= days:
                maxCap = mid 
            else:
                minCap = mid + 1

        return minCap