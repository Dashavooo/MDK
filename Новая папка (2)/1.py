# Дан класс Car.
# 
# Вам необходимо:
# 1 - Добавить атрибут fuel
# 2 - Добавить метод refuel
# 3 - Сделать метод drive, чтобы тратил топливо

class Car:
    def __init__(self, model, speed, fuel=0):
        self.model = model
        self.speed = speed
        self.fuel = fuel
        print(f'Создан автомобиль {self.model} со скоростью {self.speed}. Топливо: {self.fuel}')

    def drive(self):
        fuel_consumption = 10  # Расход топлива за одну поездку
        if self.fuel >= fuel_consumption:
            self.fuel -= fuel_consumption
            print(f'{self.model} едет со скоростью {self.speed}. Остаток топлива: {self.fuel}')
        else:
            print(f'Недостаточно топлива для поездки. В {self.model} осталось {self.fuel} единиц.')

    def refuel(self, amount):
        self.fuel += amount
        print(f'Машина {self.model} заправлена на {amount} единиц. Текущий уровень топлива: {self.fuel}')

# Создаем экземпляр класса Car
my_car = Car("Aurus", 90)

print("\n Пример #1")
my_car.drive()

# Заправляем машину
print("\nЗаправка")
my_car.refuel(25)
# Едем, пока не кончится топливо
print("\nПример #2")
my_car.drive()
my_car.drive()
my_car.drive() # На эту поездку топлива уже не хватит

