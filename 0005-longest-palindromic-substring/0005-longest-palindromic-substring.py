class Solution:
    def longestPalindrome(self, s: str) -> str:
        #here in palidrome actual if we see the center of palidrome it is mirrored means both sides are same right
        #so for even length palidromes the middle is between two ex:"bb" middle of both two
        #for odd length it has middle that is center like aba a
        #so first here we consider that  odd start  at  i and i
        #even start at i,i+1
        best_start=0
        best_end=0
        def expand_around_center(left,right):
            while left >=0 and right < len(s) and s[left]==s[right]:
                left-=1
                right+=1
            return left+1,right-1
        for i in range(len(s)):
            odd_l,odd_r=expand_around_center(i,i)
            even_l,even_r=expand_around_center(i,i+1)
            if odd_r-odd_l > best_end-best_start:
                best_start,best_end=odd_l,odd_r
            if even_r-even_l > best_end-best_start:
                best_start,best_end=even_l,even_r
        return s[best_start:best_end+1]
