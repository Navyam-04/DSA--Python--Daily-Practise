def print_time_complexity_o_n_square(n: int):
    print(f"--- O(N^2) Time Complexity (N={n}) ---")
    operations = 0
    
    # Outer loop runs N times
    for i in range(n):
        # Inner loop runs N times for EVERY outer loop
        for j in range(n):
            operations += 1
            
    print(f"Total steps executed: {operations} (Which is exactly N * N)\n")


def print_time_complexity_triangular(n: int):
    print(f"--- Triangular O(N^2) Time Complexity (N={n}) ---")
    operations = 0
    
    # Outer loop runs N times
    for i in range(n):
        # Inner loop runs from 0 up to i (i+1 times)
        for j in range(i + 1):
            operations += 1
            
    # The math here is sum of first N numbers: (N * (N + 1)) / 2
    # In Big O, we drop the constants and lower terms -> O(N^2)
    print(f"Total steps executed: {operations}\n")


def space_complexity_example(a: int, b: int) -> int:
    # a and b are INPUT space.
    
    # c is AUXILIARY space (extra memory used to solve the problem).
    # Space complexity is O(1) constant space because it only creates one new integer,
    # regardless of how big a and b are.
    c = a + b 
    return c


def main():
    # 1. Standard N^2 Loop
    print_time_complexity_o_n_square(5)
    
    # 2. Triangular Loop (Still reduces to O(N^2))
    print_time_complexity_triangular(5)
    
    # 3. Space Complexity
    result = space_complexity_example(10, 20)
    print(f"--- Space Complexity --- \nResult: {result}")

if __name__ == "__main__":
    main()