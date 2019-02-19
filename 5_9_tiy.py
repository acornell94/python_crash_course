current_users = ['andy', 'brian', 'chad', 'david', 'eli']
new_users = ['frank', 'gary', 'henry', 'DAVID', 'isaac', 'jack']

current_users_case = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users:
	    print("I'm sorry, " + new_user + " is unavailable. Please choose something else.")
    else:
        print("Yes, " + new_user + " is available.")