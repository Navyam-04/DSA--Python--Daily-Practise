class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if not s:
            return s
        left=0
        right=len(s)-1
        while left < right:
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
        return s
        