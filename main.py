import datetime
class Taxi:
    def __init__(self):
        self.base_rate: float = 4.00
        self.distance_rate: float = 0.25 / 140

    def time(func):
        def wrapper(*args, **kwargs):
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            result = func(*args, **kwargs)
            print(f'{timestamp} Запуск функции {func.__name__} с аргументами: {args}, {kwargs}')
            return result
        return wrapper

    @time
    def travel_distance(self, distance_meters):
        distance: int = distance_meters
        fare: float = self.base_rate + distance * self.distance_rate
        return round(fare, 2)

taxi = Taxi()
distance = 3500
fare = taxi.travel_distance(distance)
print(f" За растояние {distance} метров - стоимость поездки составляет ${fare}")



