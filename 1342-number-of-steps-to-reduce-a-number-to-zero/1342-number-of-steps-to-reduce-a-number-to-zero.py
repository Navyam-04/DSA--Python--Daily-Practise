class Solution:
    def numberOfSteps(self, num: int) -> int:
        step=0
        while num>0:
            if num%2==0:
                step=step+1
                num=num//2
            else:
                step=step+1
                num=num-1
        return step
        