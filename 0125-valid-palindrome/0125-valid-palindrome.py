class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_chars=[]
        for char in s:
            if char.isalnum():
                cleaned_chars.append(char.lower())
        cleaned_s="".join(cleaned_chars)
        return cleaned_s==cleaned_s[::-1]
        