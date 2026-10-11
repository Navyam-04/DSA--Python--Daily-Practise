class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_chars=set()
        max_length=0
        left=0
        for right in range(len(s)):
            while s[right] in window_chars:
                window_chars.remove(s[left])
                left+=1
            window_chars.add(s[right])
            max_length=max(max_length,right-left+1)
        return max_length

        