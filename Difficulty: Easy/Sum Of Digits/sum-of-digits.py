class Solution:
    def sumOfDigits(self, n):
        # code here
        sum=0
        while n>0:
            digit=n%10
            sum=sum+digit
            n=n//10
        return sum
        