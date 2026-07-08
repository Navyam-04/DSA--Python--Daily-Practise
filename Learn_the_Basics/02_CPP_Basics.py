def list_basics():
    print("--- Python Lists (Arrays) ---")
    
    # 1. Creating a list (No size declaration needed)
    numbers = [10, 20, 30, 40, 50]
    
    print(f"Full List: {numbers}")
    
    # 2. Accessing elements via 0-based indexing (O(1) time complexity)
    print(f"First element (Index 0): {numbers[0]}")
    print(f"Third element (Index 2): {numbers[2]}")
    
    # 3. Finding the length of the list
    print(f"Total number of elements: {len(numbers)}\n")


def string_basics(word: str):
    print("--- Python Strings ---")
    
    # 1. Finding length
    length = len(word)
    print(f"The word '{word}' has {length} characters.")
    
    # 2. Accessing individual characters
    print("Iterating through characters by index:")
    for i in range(length):
        print(f"Index {i} -> {word[i]}")
    print()


def string_immutability(original_text: str) -> str:
    print("--- String Immutability ---")
    print(f"Original: {original_text}")
    
    # Strings CANNOT be changed in place. 
    # original_text[0] = 'H'  <-- This will cause a TypeError!
    
    # To "modify" a string, we create a new one using Slicing
    # Take 'H' and concatenate it with the rest of the string (from index 1 onwards)
    modified_text = 'H' + original_text[1:]
    
    print(f"Modified: {modified_text}\n")
    return modified_text


def string_comparison(str1: str, str2: str):
    print("--- String Comparison ---")
    
    # Deep value comparison
    if str1 == str2:
        print(f"'{str1}' and '{str2}' are EXACTLY equal.")
    else:
        print(f"'{str1}' and '{str2}' are NOT equal.")
    print()


def main():
    list_basics()
    
    string_basics("striver")
    
    string_immutability("hello")
    
    # Case-sensitive comparisons
    string_comparison("data", "data")
    string_comparison("data", "Data")

if __name__ == "__main__":
    main()