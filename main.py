#1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`)
# и методы (`make_sound()`, `eat()`) для всех животных.

#2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`.
# Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).

#3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных
# и вызывает метод `make_sound()` для каждого животного.

#4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.

#5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы
# (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).


class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass

class Bird(Animal):
    def make_sound(self):
        print("Ку-ку")

class Mammal(Animal):
    def make_sound(self):
        print("Мяу-мяу")

class Reptile(Animal):
    def make_sound(self):
        print("Ква-ква")

animals = [Bird("Кукушка", 5), Mammal("Кот", 2), Reptile("Жаба", 1)]

print(f"Животные: {[animal.name for animal in animals]}, возраст: {[animal.age for animal in animals]}")
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

animal_sound(animals)


class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_employee(self, employee):
        self.employees.append(employee)

    def feed_animal(self):
        pass

    def heal_animal(self):
        pass


class ZooKeeper(Zoo):
    def feed_animal(self):
        pass

class Veterinarian(Zoo):
    def heal_animal(self):
        pass

