def check_adult_status():
    print("--- Age Check ---")
    # Take input and convert it to an integer immediately
    age = int(input("Enter your age: "))
    
    # Python uses a colon (:) to start a conditional block
    if age >= 18:
        # Notice the indentation!
        print("You are an adult.\n")
    else:
        print("You are not an adult.\n")

def unoptimized_grading(marks: int):
    print(f"--- Unoptimized Grading (Marks: {marks}) ---")
    # Using 'and' to check both boundaries explicitly
    if marks < 25:
        print("Grade: F")
    elif marks >= 25 and marks <= 44:
        print("Grade: E")
    elif marks >= 45 and marks <= 49:
        print("Grade: D")
    elif marks >= 50 and marks <= 59:
        print("Grade: C")
    elif marks >= 60 and marks <= 69:
        print("Grade: B")
    elif marks >= 70:
        print("Grade: A")
    else:
        print("Invalid marks entered.")
    print()

def optimized_grading(marks: int):
    print(f"--- Optimized Grading (Marks: {marks}) ---")
    # Because Python checks sequentially top-to-bottom, we can drop the lower bounds.
    # If the code reaches the first 'elif', we ALREADY know marks >= 25.
    
    if marks < 25:
        print("Grade: F")
    elif marks <= 44:  # Implies marks >= 25
        print("Grade: E")
    elif marks <= 49:  # Implies marks > 44
        print("Grade: D")
    elif marks <= 59:  # Implies marks > 49
        print("Grade: C")
    elif marks <= 69:  # Implies marks > 59
        print("Grade: B")
    else:              # Implies marks >= 70
        print("Grade: A")
    print()

def main():
    # Uncomment the line below to test the age checker interactively
    # check_adult_status()
    
    # Testing the grading systems
    test_marks = 54
    unoptimized_grading(test_marks)
    optimized_grading(test_marks)

if __name__ == "__main__":
    main()