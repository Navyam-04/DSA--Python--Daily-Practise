class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
    
        while left < right:
        # HIDDEN TRAP: Safely skip non-alphanumeric characters from the left
            while left < right and not s[left].isalnum():
                left += 1
            
        # Safely skip non-alphanumeric characters from the right
            while left < right and not s[right].isalnum():
                right -= 1
            
        # Compare the lowercase versions of the valid characters
            if s[left].lower() != s[right].lower():
                return False
            
        # Move both pointers inward for the next comparison
            left += 1
            right -= 1
        
        return True
        