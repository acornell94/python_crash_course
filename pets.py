pets = []

pet = {
    'name': 'spike',
    'animal_type': 'dog',
    'owner': 'megan',
    }
pets.append(pet)

pet = {
    'name': 'fluffy',
    'animal_type': 'cat',
    'owner': 'susan',
    }
pets.append(pet)

pet = {
    'name': 'al',
    'animal_type': 'bird',
    'owner': 'sam',
    }
pets.append(pet)

for pet in pets:
    print(pet['owner'].title() + "'s " + pet['animal_type'] + " is named " + 
    pet['name'].title() + ".")	