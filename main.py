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
        print(f"{self.name} ест.")

class Bird(Animal):
    def make_sound(self):
        print(f"{self.name} говорит ку-ку!")

class Mammal(Animal):
    def make_sound(self):
        print(f"{self.name} говорит мяу!")

class Reptile(Animal):
    def make_sound(self):
        print(f"{self.name} говорит ква-ква!")

animals = [Bird("Кукушка", 5), Mammal("Кот", 2), Reptile("Жаба", 1)]

print(f"Животные: {[animal.name for animal in animals]}, возраст: {[animal.age for animal in animals]}")
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

animal_sound(animals)


class ZooKeeper:
    def feed_animal(self, animal):
        print(f"{self.name} освобождает {animal.name}.")

    def __init__(self, name):
        self.name = name

class Veterinarian:
    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}.")

    def __init__(self, name):
        self.name = name

# Класс Zoo с использованием композиции
class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Добавление {animal.name} в животные зоопарка.")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"Дабавление {staff_member.name} в сотрудники зоопарка.")

# Создание объектов и тестирование функционала
zoo = Zoo()
zoo.add_staff(ZooKeeper("Настя"))
zoo.add_staff(Veterinarian("Михаил"))

zoo.add_animal(Bird("Кушка", 3))
zoo.add_animal(Mammal("Кот", 5))
zoo.add_animal(Reptile("Жаба", 2))
print(f"Животные: {[animal.name for animal in animals]}, возраст: {[animal.age for animal in animals]}")
animal_sound(zoo.animals)
