file_name = 'guest_book.txt'

print('Enter "stop" to end.')
active = True
while active:
    name = input("Please tell me your name.")
    if name == 'stop':
        active = False
    else:
        print("Hello, " + name + "!\n")
        with open(file_name, 'a') as file_object:
            file_object.write(name + "\n")