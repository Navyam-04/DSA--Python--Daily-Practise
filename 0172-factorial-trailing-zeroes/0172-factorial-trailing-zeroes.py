class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        count=0
        power_5=5
        while(n//power_5)>0:
            count=count+(n//power_5)
            power_5=power_5*5
        return count

        