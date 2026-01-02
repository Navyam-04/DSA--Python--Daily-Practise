def sumOfDigits(n):
    if n==0:return 0
    n=abs(n)
    sum=0
    while n>0:
        digit=n%10
        sum=sum+digit
        n=n//10
    return sum
# Test the function
if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(f"The sum of digits in {num} is {sumOfDigits(num)}")