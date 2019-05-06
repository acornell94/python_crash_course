file_name = 'learning_python.txt'

with open(file_name) as f:
    lines = f.readlines()

for line in lines:
    print(line.strip())

print()

for line in lines:
    line = line.strip()
    print(line.replace('Python', 'C'))