def city_country(city, country):
    return(city.title() + ", " + country.title())

city = city_country('quebec', 'canada')
print(city)

city = city_country('reykjavik', 'iceland')
print(city)

city = city_country('dublin', 'ireland')
print(city)