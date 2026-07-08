def calculate_factorial(n: int):
    print(f"--- Calculating Factorial of {n} ---")
    
    factorial = 1
    current_n = n
    
    # The loop continues as long as current_n is strictly greater than 0
    while current_n > 0:
        factorial *= current_n  # Multiply the running total by current_n
        current_n -= 1          # Decrement current_n by 1 (Equivalent to n--)
        
    print(f"Factorial of {n} is: {factorial}\n")


def data_validation_example():
    print("--- While Loop for Data Validation ---")
    # This loop will run infinitely until the user provides valid data
    # (Uncomment the lines below to test it interactively)
    
    # valid_input = False
    # while not valid_input:
    #     user_input = input("Enter a positive number: ")
    #     
    #     # .isdigit() checks if the string contains only numbers
    #     if user_input.isdigit() and int(user_input) > 0:
    #         print(f"Valid data accepted: {user_input}")
    #         valid_input = True  # This breaks the loop condition
    #     else:
    #         print("Invalid input. Please try again.")
    print("Validation logic is ready to be uncommented and tested.\n")


def main():
    calculate_factorial(5)
    calculate_factorial(3)
    
    data_validation_example()

if __name__ == "__main__":
    main()