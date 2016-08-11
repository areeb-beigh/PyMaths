def take_input(options_list, max_value, min_value=1):
    """
    Prints the given options and takes the user input (int) and checks
    if it is in the given range
    """

    indent = "    "
    print()
    for serial, option in enumerate(options_list, start=min_value):
        print(indent, str(serial) + ".", option)
    print()
    choice = int(input("Enter your choice: "))
    valid_options = range(min_value, max_value + 1)
    if choice in valid_options:
        return choice
    else:
        print("Invalid input, try again")
        take_input(options_list, max_value, min_value)
