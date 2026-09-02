class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            total = 0
       
            while num>0:
                digit=num%10
                total+=digit
                num//=10
            num=total
        return num

        