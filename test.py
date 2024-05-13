# Базовый класс
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("This method should be overridden by subclasses.")

    def eat(self):
        print(f"{self.name} ест.")

# Подклассы
class Bird(Animal):
    def make_sound(self):
        print(f"{self.name} говорит чирик!")

class Mammal(Animal):
    def make_sound(self):
        print(f"{self.name} говорит ррр!")

class Reptile(Animal):
    def make_sound(self):
        print(f"{self.name} произносит шипение!")

# Функция для демонстрации полиморфизма
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

# Классы для сотрудников
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
zoo.add_staff(ZooKeeper("Alice"))
zoo.add_staff(Veterinarian("Bob"))

zoo.add_animal(Bird("Tweety", 3))
zoo.add_animal(Mammal("Simba", 5))
zoo.add_animal(Reptile("Slither", 2))

animal_sound(zoo.animals)
