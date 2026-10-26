class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        i = 0
        res = ""
        while columnNumber > 0:
            print(res)
            columnNumber -= 1
            res = chr((columnNumber%26 + 65)) + res
            columnNumber //= 26
        return res