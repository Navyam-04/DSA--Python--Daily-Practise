class Solution:
    def checkPerfectNumber(self, n: int) -> bool:
        if n<=1:
            return False
        d_sum=1
        limit=int(n**0.5)
        for i in range(2,limit+1):
            if n%i==0:
                d_sum=d_sum+i
                if i!= n//i:
                    d_sum=d_sum+(n//i)
        return d_sum==n
        