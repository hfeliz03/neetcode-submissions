class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        startIndex = -1
        res = []
        
        for i, num in enumerate(arr):
            if num < x:
                startIndex = i
                continue
            elif (num > x and abs(num - x) < abs(arr[startIndex] - x)) or num == x:
                startIndex = i
        
            break
        
        if startIndex != -1: res = [arr[startIndex]]
        l = startIndex - 1
        r = startIndex + 1
        

        while len(res) < k:
            if l >= 0 and r < len(arr):
                if abs(x - arr[l]) <= abs(x - arr[r]):
                    res.append(arr[l])
                    l -= 1
                else:
                    res.append(arr[r]) 
                    r += 1
            elif l >= 0:
                res.append(arr[l])
                l -= 1
            else:
                res.append(arr[r])
                r += 1
        
        return sorted(res)

