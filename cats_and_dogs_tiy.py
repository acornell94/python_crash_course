file_names = ['cats.txt', 'birds.txt', 'dogs.txt']

for file_name in file_names:
    print("Contents of " + file_name + ":")
    try:
        with open(file_name) as file_object:
            contents = file_object.read()
            print(contents)
    except FileNotFoundError:
        pass