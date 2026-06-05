# Дан класс Animal.
# 
# Сделать классы:
# 1 - Dog (выводит "гав-гав")
# 2 - Cat ("Мяяяяу")
# 3 - Cow ("бжбж")

class Animal:
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        print("гав-гав")
class Cat(Animal):
    def speak(self):
        print("Мяяяяу")
class Cow(Animal):
    def speak(self):
        print("бжбж")

