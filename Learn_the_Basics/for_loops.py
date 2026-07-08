def basic_for_loop():
    print("--- Basic For Loop ---")
    # range(1, 11) generates numbers from 1 up to 10.
    for i in range(1, 11):
        print(f"Hey, Striver, this is the {i}'th iteration")
    print()


def nested_for_loops():
    print("--- Nested For Loops ---")
    # range(3) is a shortcut for range(0, 3) -> generates 0, 1, 2
    for i in range(3):
        for j in range(3):
            print(f"i = {i}, j = {j}")
    print()


def conditional_for_loop():
    print("--- Conditionals Inside For Loops ---")
    # Loop from 1 to 5
    for i in range(1, 6):
        if i % 2 == 0:
            print(f"{i} is an EVEN number")
        else:
            print(f"{i} is an ODD number")
    print()


def custom_step_loop():
    print("--- Customizing For Loops (Step) ---")
    # range(start=1, stop=26, step=5)
    for i in range(1, 26, 5):
        print(f"i = {i}")
    print()


def main():
    basic_for_loop()
    nested_for_loops()
    conditional_for_loop()
    custom_step_loop()

if __name__ == "__main__":
    main()