import json

class Animal:
    def __init__(self, type, name, age):
        self.type = type
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        print(f"{self.name} ест.")

class Bird(Animal):
    def __init__(self, name, age):
        super().__init__("Bird", name, age)

    def make_sound(self):
        print(f"{self.name} говорит ку-ку!")

class Mammal(Animal):
    def __init__(self, name, age):
        super().__init__("Mammal", name, age)

    def make_sound(self):
        print(f"{self.name} говорит мяу!")

class Reptile(Animal):
    def __init__(self, name, age):
        super().__init__("Reptile", name, age)

    def make_sound(self):
        print(f"{self.name} говорит ква-ква!")

class ZooKeeper:
    def __init__(self, name):
        self.name = name
        self.role = "ZooKeeper"

class Veterinarian:
    def __init__(self, name):
        self.name = name
        self.role = "Veterinarian"

class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Добавление {animal.name} в животные зоопарка.")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"Добавление {staff_member.name} в сотрудники зоопарка.")

    def list_animals(self):
        print("Список животных в зоопарке:")
        for animal in self.animals:
            print(f"Имя: {animal.name}, возраст: {animal.age}, тип: {animal.type}")

    def list_staff(self):
        print("Список сотрудников зоопарка:")
        for staff_member in self.staff:
            print(f"Имя: {staff_member.name}, роль: {staff_member.role}")

    def save_to_file(self, filename):
        data = {
            "animals": [{"type": a.type, "name": a.name, "age": a.age} for a in self.animals],
            "staff": [{"name": s.name, "role": s.role} for s in self.staff]
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
            print("Состояние зоопарка сохранено в файл.")

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            self.animals = [self.create_animal(a['type'], a['name'], a['age']) for a in data['animals']]
            self.staff = [self.create_staff_member(s['name'], s['role']) for s in data['staff']]
            print("Состояние зоопарка загружено из файла.")

    def create_animal(self, type, name, age):
        if type == "Bird":
            return Bird(name, age)
        elif type == "Mammal":
            return Mammal(name, age)
        elif type == "Reptile":
            return Reptile(name, age)

    def create_staff_member(self, name, role):
        if role == "ZooKeeper":
            return ZooKeeper(name)
        elif role == "Veterinarian":
            return Veterinarian(name)

# Пример использования
zoo = Zoo()
zoo.add_staff(ZooKeeper("Настя"))
zoo.add_staff(Veterinarian("Михаил"))

zoo.add_animal(Bird("Кукушка", 3))
zoo.add_animal(Mammal("Кот", 5))
zoo.add_animal(Reptile("Жаба", 2))

# Сохранение состояния зоопарка в файл
zoo.save_to_file('zoo_state.json')

# Загрузка состояния зоопарка из файла
new_zoo = Zoo()
new_zoo.load_from_file('zoo_state.json')
new_zoo.list_animals()
new_zoo.list_staff()
