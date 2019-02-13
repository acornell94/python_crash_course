for value in range (0,11):
    print(value)

squares = []
for value in range (1,11):
    square = value**2
    squares.append(square)
print(squares)

cubes = [value**3 for value in range(1,11)]
print(cubes)

print(sum(cubes)-sum(squares))
print(min(cubes))
print(max(cubes))