favorite_places = {
    'john': ['florida', 'alaska'],
    'bill': ['oregon'],
    'sarah': ['cambodia', 'singapore'],
    }

for name, places in favorite_places.items():
    if len(places) < 2:
        print("\n" + name.title() + "'s favorite place is as follows:")
        for place in places:
            print("\t" + place.title())
    else:
        print("\n" + name.title() + "'s favorite places are as follows:")
        for place in places:
            print("\t" + place.title())