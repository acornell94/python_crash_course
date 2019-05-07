print("Input 2 numbers, and I will add them for you. Enter 'quit' to quit.")
while True:
    try:
        first_number = input("Please tell me your first number.")
        if first_number == 'quit':
            break
        first_number = int(first_number)
        second_number = input("Please tell me a second number.")
        if second_number == 'quit':
            break
        second_number = int(second_number)
    except ValueError:
        print("\nPlease enter your number in a numeric format.\n")
    else:
        added = first_number + second_number
        print("\nThe sum is " + str(added) + ".\n")