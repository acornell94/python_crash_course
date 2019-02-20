capitals = {
    'thailand': 'bangkok',
    'china': 'beijing',
    'jordan': 'amman',
    'egypt': 'cairo',
    'italy': 'rome',
    'ireland': 'dublin',
    'kyrgyzstan': 'bishkek',
    }

for country, city in capitals.items():
    print(city.title() + " is the capital of " + country.title() + ".")

print(" ")
for city in capitals.values():
    print(city.title())

print(" ")
for country in capitals.keys():
    print(country.title())