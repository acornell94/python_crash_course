import json

# Load favorite number if it has been given previously.
# Prompt the user for favorite number if not. 

filename = 'favorite_number.json'

try:
    with open(filename) as file_object:
        number = json.load(file_object)
except FileNotFoundError:
    number = input('What is your favorite number?')
    with open (filename, 'w') as file_object:
        json.dump(number, file_object)
    print("I'll keep that in mind!")
else:
    print("Your favorite number is " + number + ".")