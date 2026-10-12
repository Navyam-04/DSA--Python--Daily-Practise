class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []
        p_count=[0]*26
        window_count=[0]*26
        result=[]
        k=len(p)
        for i in range(k):
            p_count[ord(p[i]) - ord('a')] += 1
            window_count[ord(s[i]) - ord('a')] += 1
        if p_count== window_count:
            result.append(0)
        
        for right in range(k,len(s)):
            incoming_char=s[right]
            outgoing_char=s[right-k]
            
            window_count[ord(incoming_char) - ord('a')] += 1
            window_count[ord(outgoing_char) - ord('a')] -= 1
            left=right-k+1
            if p_count == window_count:
                result.append(left)
        return result


        