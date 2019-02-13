available_cars = ['honda', 'nissan', 'volkswagen', 'bmw', 'subaru']
requested = ['nissan', 'audi', 'lexus', 'volkswagen']

for car in requested:
    print("Do you have any cars made by " + car.title() + "?")
    if car in available_cars:
        print("Yes! We have some in stock.\n")
    else:
        print("I'm sorry, but we do not at this time.\n")