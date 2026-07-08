import sys
def main():
    # 1. Basic Output
    print("--- Output ---")
    print("Hey, Striver!") 
    print("Hey, Striver!", end=" ") # Stays on same line
    print("(This is on the same line)\n")
    # 2. Single Input
    print("--- Single Input ---")
    x = int(input("Enter a single number: "))
    print(f"Value of x: {x}\n")
    # 3. Multiple Inputs
    print("--- Multiple Inputs ---")
    print("Enter two numbers separated by a space:")
    a, b = map(int, input().split())
    print(f"Value of a: {a} and b: {b}\n")

if __name__ == "__main__":
    main()
 