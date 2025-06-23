def make_sandwich(*fillings):
    print("\nMaking a sandwich which following filling")
    for filling in fillings:
        print("- " + filling)


make_sandwich('Ham', 'Cheddar cheese', 'Lettuce')
make_sandwich('Turkey', 'Swiss cheese', 'Cucumber', 'Egg salad')
make_sandwich('Mayonnaise', 'Pickles', 'Tuna salad',
              'Tomato', 'Avocado')

