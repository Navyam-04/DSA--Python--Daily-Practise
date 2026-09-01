class Solution:
    # Function to calculate the sum of squares of first 'number' natural numbers
    def sumOfSquares(self, n):
        sum=0
        for i in range(1,n+1):
            sum=sum+(i**2)
            i=i+1
        return sum
        # code here
        