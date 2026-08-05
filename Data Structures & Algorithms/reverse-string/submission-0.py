class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #s = s[::-1]    # reassigns the variable
        s[:] = s[::-1] # replaces the contents of the same list