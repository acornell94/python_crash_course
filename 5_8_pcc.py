users = ['admin', 'ann', 'sue', 'barbara', 'beverly']

for user in users:
    if user == 'admin':
        print("Hello, Admin. Would you like to see a status report?")
    else:
    	print("Hello, " + user.title() + ". Thank you for logging in again.")