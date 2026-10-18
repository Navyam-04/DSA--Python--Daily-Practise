class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False
        sub_idx=0
        target_idx=0
        while sub_idx < len(s) and target_idx < len(t):
            if s[sub_idx]==t[target_idx]:
                sub_idx+=1
            target_idx+=1
        return sub_idx == len(s)
            
         

        