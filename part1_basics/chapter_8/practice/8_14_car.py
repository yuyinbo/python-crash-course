def make_car(manufacturer, model, **kwargs):
    info = {'manufacturer': manufacturer, 'model': model}
    for key, value in kwargs.items():
        info[key] = value
    return info


car = make_car('Subaru', 'outback', color='blue',
               tow_package=True)
print(car)
