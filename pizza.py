toppings = ['green peppers', 'mushrooms', 'red peppers']

print(toppings)

for topping in toppings:
    if topping == 'mushrooms':
        print("Unfortunately, we do not have any mushrooms right now.")
    else:
        print("Adding " + topping + ".")

if "mushrooms" in toppings:
    print("\nWould you like to add another topping in the place of mushrooms?")
else:
    print("\nYour pizza is finished!")