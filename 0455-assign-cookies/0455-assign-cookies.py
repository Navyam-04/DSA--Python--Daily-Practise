class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        s.sort()
        g.sort()
        child_i=0
        cookies_j=0
        while child_i < len(g)  and  cookies_j < len(s) :
            if s[cookies_j] >= g[child_i]:
                child_i+=1
            cookies_j+=1
        return child_i

        