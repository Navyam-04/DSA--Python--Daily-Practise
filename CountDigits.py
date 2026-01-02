def countDigits(n):
    n=abs(n)
    if n==0: return 1
    count=0
    while n>0:
        n=n//10
        count=count+1
    return count
# Test the function
if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(f"The number of digits in {num} is {countDigits(num)}")