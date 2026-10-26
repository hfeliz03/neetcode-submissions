class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        res = ""
        minStr = str1 if len(str1)<len(str2) else str2
        r = len(minStr) - 1
        while r >= 0:
            if minStr[:r+1] * (len(str1) // (len(minStr[:r+1]))) == str1 and minStr[:r+1] * (len(str2) // (len(minStr[:r+1]))) == str2:
                res = minStr[:r+1]
                break
            r -= 1
        return res