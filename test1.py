import pickle

class Animal:
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

    def list_animals(self):
        print("Список животных в зоопарке:")
        for animal in self.animals:
            print(f"Имя: {animal.name}, возраст: {animal.age}")

    def list_staff(self):
        print("Список сотрудников зоопарка:")
        for staff_member in self.staff:
            print(f"Имя: {staff_member.name}")

    def save_to_file(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)
            print("Состояние зоопарка сохранено в файл.")

    def load_from_file(self, filename):
        with open(filename, 'rb') as f:
            loaded_zoo = pickle.load(f)
            self.animals = loaded_zoo.animals
            self.staff = loaded_zoo.staff
            print("Состояние зоопарка загружено из файла.")

# Пример использования
zoo = Zoo()
zoo.add_staff(ZooKeeper("Настя"))
zoo.add_staff(Veterinarian("Михаил"))

zoo.add_animal(Bird("Кукушка", 3))
zoo.add_animal(Mammal("Кот", 5))
zoo.add_animal(Reptile("Жаба", 2))

# Сохранение состояния зоопарка в файл
zoo.save_to_file('zoo_state.pkl')

# Загрузка состояния зоопарка из файла
new_zoo = Zoo()
new_zoo.load_from_file('zoo_state.pkl')
new_zoo.list_animals()
new_zoo.list_staff()
