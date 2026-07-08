def modify_immutable(a: int):
    print(f"Inside function (Start): a = {a}")
    # Because 'a' is an integer (immutable), this creates a NEW object in memory
    a = a + 10
    print(f"Inside function (End): a = {a} (Points to new memory)\n")

def modify_mutable(lst: list):
    print(f"Inside function (Start): lst = {lst}")
    # Because 'lst' is a list (mutable), .append() modifies the original object directly
    lst.append(10)
    print(f"Inside function (End): lst = {lst} (Modifies original memory)\n")

def the_reassignment_trap(lst: list):
    print(f"Inside function (Start): lst = {lst}")
    # TRAP: By using '=' to assign a brand new list, we break the link to the original!
    # It no longer modifies the passed list; it creates a new local one.
    lst = [99, 100]
    print(f"Inside function (End): lst = {lst} (Link broken, points to new memory)\n")

def main():
    print("--- 1. Immutable Types (Integers/Strings) ---")
    x = 5
    print(f"Before function: x = {x}")
    modify_immutable(x)
    print(f"After function: x = {x} (Original is safe!)\n")
    
    print("--- 2. Mutable Types (Lists/Dictionaries) ---")
    my_nums = [5]
    print(f"Before function: my_nums = {my_nums}")
    modify_mutable(my_nums)
    print(f"After function: my_nums = {my_nums} (Original was changed!)\n")
    
    print("--- 3. The Reassignment Trap ---")
    my_other_nums = [5]
    print(f"Before function: my_other_nums = {my_other_nums}")
    the_reassignment_trap(my_other_nums)
    print(f"After function: my_other_nums = {my_other_nums} (Original is safe!)\n")

if __name__ == "__main__":
    main()