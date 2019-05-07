print("Input 2 numbers, and I will add them for you.")
try:
    first_number = input("Please tell me your first number.")
    first_number = int(first_number)
    second_number = input("Please tell me a second number.")
    second_number = int(second_number)
except ValueError:
    print("Please enter your number in a numeric format.")
else:
    added = first_number + second_number
    print("The sum is " + str(added) + ".")