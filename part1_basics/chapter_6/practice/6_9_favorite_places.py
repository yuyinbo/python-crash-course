favorite_places = {
    'alice': ['paris', 'kyoto', 'santorini'],
    'ben': ['new york city', 'roma'],
    'catherine': ['london'],
}

for name, places in favorite_places.items():
    if len(places) >= 2:
        print(name.title() + "'s favorite places are: ")
        for place in places:
            print("\t" + place.title())
    else:
        print(name.title() + "'s favorite place is: " + places[0].title())
