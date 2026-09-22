class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        l, r = 0, n-1
        boats = 0
        while l <= r:
            curWeight = limit
            carries = 0
            while carries < 2 and people[r] <= curWeight:
                curWeight -= people[r]
                r -= 1
                carries += 1
            while carries < 2 and l < r and people[l] <= curWeight:
                curWeight -= people[l]
                l += 1 
                carries += 1
            boats += 1
        return boats