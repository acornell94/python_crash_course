people = ['adam', 'blake', 'charlie', 'dillon']

def show_people(people):
    for person in people:
        print(person.title())

def make_great(people):
    great_people = []

    while people:
        person = people.pop()
        great_person = person + " the Great"
        great_people.append(great_person)

    for great_person in great_people:
        people.append(great_person)

show_people(people)
print(" ")
make_great(people)
show_people(people)