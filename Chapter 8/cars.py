def make_car(make, model, **car_info):
    car_info['make'] = make
    car_info['model'] = model
    return car_info

car = make_car('Honda', 'Civic', year=2016, color='silver')
print(car)