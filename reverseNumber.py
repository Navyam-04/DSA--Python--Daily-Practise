def reverseNumber(n):
    sigh=-1 if n<0 else 1
    n=abs(n)
    rev=0
    while n>0:
        digit=n%10
        rev=(rev*10)+digit
        n=n//10
    if rev > 2**31 - 1 or rev < -2**31:
        return 0

    return rev*sigh

print(reverseNumber(123))
print(reverseNumber(-1456))

