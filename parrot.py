promt ="\nTell me something, and I will repeat it back to you."
promt += "\nEnter 'QUIT' to end the program."
message =""
while message != 'QUIT':
    message = input(prompt)
    print(message)