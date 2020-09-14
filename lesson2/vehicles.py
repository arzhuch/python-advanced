'''
1) Создать класс автомобиля. Описать общие аттрибуты. Создать
классы легкового автомобиля и грузового. Описать в основном
классе базовые аттрибуты для автомобилей. Будет плюсом если в
классах наследниках переопределите методы базового класса.
'''
from time import sleep


class Vehicle:

    purpose = 'transportation'
    number_of_wheels = 4

    def __init__(self, manufacturer, color):

        self.manufacturer = manufacturer
        self.color = color
        self.loaded_with = []
        self.engine_started = False

    def start_engine(self, delay=0):
        self.engine_started = True
        print('Starting engine... brr brr brrrrrr!!!... ')
        sleep(delay)
        print(f'Engine started after {delay} seconds')

    def check_engine(self):
        print('Engine is working') if self.engine_started else print('Engine is silent')

    def load_into(self, stuff, *args):
        for a in args:
            print(f'{a} loaded into {self.color} {self.manufacturer}!')
            self.loaded_with.append(a)


class Truck(Vehicle):

    cargo_capacity_in_kg = 1500

    def change_capacity(self, delta):
        self.cargo_capacity_in_kg += delta
        print('New truck capacity is ', self.cargo_capacity_in_kg)

    def load_into(self, **kwargs):    # designed to take item name and weight
        for item, weight in kwargs.items():
            print(f'Loaded {item}, weight = {weight} kg')
            self.loaded_with.append({item: weight})

    def check_load(self):
        print('Loaded with: ')
        print(self.loaded_with)


class Car(Vehicle):

    passanger_capacity = 4
    music_playing = None
    passangers_inside = ()

    def turn_on_music(self, song):
        self.music_playing = song
        print(song, 'is playing out of the car!')

    def load_into(self, **kwargs):  # designed to take passanger's name and age
        for name, age in kwargs.items():
            print(f'{name}, {age} y.o., is inside the car')
            self.loaded_with.append({name: age})

    def check_load(self):
        print('Loaded with: \n')
        for i in self.loaded_with:
            print(i)



# just leaving it here

my_car = Car('Mustang', 'white')
my_truck = Truck('KAMAZ', 'blue')

my_car.load_into(artem=24, kostya=31, oleh=66)
my_car.check_load()

my_truck.load_into(furniture=50, food=35)
my_truck.check_load()
