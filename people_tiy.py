person_0 = {
    'first_name': 'Jack',
    'last_name': 'Hill',
    'age': 26,
    'city': 'Chicago',
    }

person_1 = {
    'first_name': 'Jill',
    'last_name': 'Hill',
    'age': 24,
    'city': 'Chicago',
    }

person_2 = {
    'first_name': 'Jane',
    'last_name': 'Hill',
    'age': 2,
    'city': 'Chicago',
    }

people = [person_0, person_1, person_2]

for person in people:
    name = person['first_name'].title() + " " + person['last_name'].title()
    age = str(person['age'])
    city = person['city'].title()

    print(name + " of " + city + " is " + age + " years old.")