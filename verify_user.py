import json

def get_stored_user():
    """Check to see if there is a stored username."""
    filename = 'username.json'
    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username

def greet_user():
    """Greet the user."""
    username = get_stored_user()
    if username:
        confirmed = input("Is this " + username + "? Enter 'y' for yes or 'n' for no.")
        if confirmed == 'y':
            print('Hello, ' + username + '!')
        if confirmed == 'n':
            username = get_new_user()
            print('Welcome to our site, ' + username + '!')
    else:
        username = get_new_user()
        print('Welcome to our site, ' + username + '!')

def get_new_user():
    """Prompt user for their name."""
    username = input('What is your name?')
    filename = 'username.json'
    with open(filename, 'w') as file_object:
        json.dump(username, file_object)
    return username

def confirm_user():
    username = input("Is this " + username + "? Enter 'y' for yes or 'n' for no.")
    if confirmed == 'y':
        print('Hello, ' + username + '!')
    if confirmed == 'n':
        username = get_new_user()
        print('Welcome to our site, ' + username + '!')

greet_user()