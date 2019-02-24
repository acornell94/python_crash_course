def greet_users(names):
    for name in names:
    	print("Hello, " + name.title() + "!")

users = ['ann', 'todd', 'chad']
greet_users(users)