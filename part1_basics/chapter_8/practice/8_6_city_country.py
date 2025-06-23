def city_country(city, country):
    city_info = {'name': city.title(), 'loc': country.title()}
    city_info_str = '"' + city_info['name'] + ', ' + city_info['loc'] + '"'
    return city_info_str


print(city_country('wuhan', 'china'))
print(city_country('tokyo', 'japan'))
print(city_country('new york', 'USA'))
