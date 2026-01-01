def check_odd_even(number):
    """
    Determine if a number is odd or even.
    
    Args:
        number: An integer to check
        
    Returns:
        A string indicating if the number is odd or even
    """
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


# Test cases
if __name__ == "__main__":
    test_numbers = [10, 7, 24, 33, 0, -5, -12]
    
    for num in test_numbers:
        result = check_odd_even(num)
        print(f"{num} is {result}")
