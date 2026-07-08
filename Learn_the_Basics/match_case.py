def day_of_week(day_number: int):
    print(f"--- Match Statement: Day {day_number} ---")
    
    # The modern Python 'switch' equivalent (Python 3.10+)
    match day_number:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
        case _:
            # The underscore acts as the default/catch-all case
            print("Invalid Day")
    print()


def grade_evaluation(grade: str):
    print(f"--- Match Statement: Grade '{grade}' ---")
    
    # Python easily handles strings in match statements
    match grade.upper():  # .upper() ensures 'a' matches 'A'
        case 'A':
            print("Excellent!")
        case 'B':
            print("Good!")
        case 'C':
            print("Average.")
        case _:
            print("Not specified.")
    print()


def day_of_week_dictionary(day_number: int):
    print(f"--- Dictionary Mapping: Day {day_number} ---")
    
    # The classic, highly-optimized Pythonic approach using a dictionary
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    
    # .get() looks up the key, and returns the second argument if the key is missing
    result = days.get(day_number, "Invalid Day")
    print(result)
    print()


def main():
    # 1. Testing the Match-Case statement
    day_of_week(4)
    day_of_week(9)
    
    # 2. Testing String matching
    grade_evaluation('B')
    
    # 3. Testing the Dictionary mapping (Data Engineering style)
    day_of_week_dictionary(5)
    day_of_week_dictionary(10)

if __name__ == "__main__":
    main()