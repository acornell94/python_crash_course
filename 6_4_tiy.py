produce_colors = {
    'banana': 'yellow',
    'carrot': 'orange',
    'lime': 'green',
    'lemon': 'yellow',
    'broccoli': 'green',
    'beet': 'purple',
    'apple': 'red',
    'blueberry': 'blue',
    }

print("The following produce have been mentioned:")
for produce in produce_colors.keys():
    print(produce.title())

print("\nProduce can be many different colors. For example: ")
for colors in set(produce_colors.values()):
    print(colors.title())