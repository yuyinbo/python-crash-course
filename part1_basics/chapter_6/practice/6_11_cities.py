cities = {
    'tokyo': {
        'country': 'japan',
        'population': '37 million',
        'fact': "It is the largest metropolitan area in the world "
                "by population."
    },
    'cairo': {
        'country': 'egypt',
        'population': '20 million',
        'fact': "It is home to the famous Giza Pyramids and "
                "the Great Sphinx."

    },
    'rio de janeiro': {
        'country': 'brazil',
        'population': '6.7 million',
        'fact': "It is known for its annual Carnival festival and "
                "the iconic Christ the Redeemer statue. "
    },
}

for city_name, city_info in cities.items():
    print(city_name.title() + " is in " + city_info['country'] +
          ", with a population of " + city_info['population'] + " people. " +
          city_info['fact'])

for city_name, city_info in cities.items():
    print(city_name.title())
    for key, value in city_info.items():
        if key != 'fact':  # 避免fact的句子也.title()
            print("\t" + key.title() + ": " + value.title())
        else:
            print("\t" + key.title() + ": " + value)

