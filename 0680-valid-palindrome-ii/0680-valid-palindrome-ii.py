class Solution:
    def validPalindrome(self, s: str) -> bool:

        def palindrome_helper(arr, left, right):
            while left < right:
                if arr[left] != arr[right]:
                    return False

                left += 1
                right -= 1

            return True

        if len(s) == 1:
            return True

        left = 0
        right = len(s) - 1

        while left < right:

            if s[left] != s[right]:
                return palindrome_helper(s, left + 1, right) or palindrome_helper(s, left, right - 1)

            left += 1
            right -= 1

        return True