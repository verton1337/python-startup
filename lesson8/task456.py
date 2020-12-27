"""
4. Начните работу над проектом «Склад оргтехники». 
Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники 
(принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
 Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.
 
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для указания количества принтеров, 
отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""
from abc import ABC, abstractmethod
import random

class Storage():
    def __init__(self, name):
        self.__assets = {}
        self.name = name
    def move_to_storage(self, item):
        item.position = self.name
        if not item._category in self.__assets.keys():
            self.__assets[item._category] = [item]
        else:
            self.__assets[item._category].append(item)
    def move_from_storage(self, item, position):
        self.__assets[item._category].remove(item)
        item.position = position
        
    def check_count_asset(self, category):
        return len(self.__assets[category])
    @property
    def assets_storage(self):
        return self.__assets
    def __str__(self):
        result = "Оборудование на складе:\n"
        for k,v in self.__assets.items():
            result += f"{k} \n"
            for i in v:
                result += f"\t {i.name} s/n {i._asset_number}\n"
        return result
        
    
    
class Item(ABC):
    @abstractmethod
    def create_asset_number(self):
        pass
        
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        self.position = "undefined"
        
    def __str__(self):
        return self.name
        
        
class Printer(Item):
    @staticmethod
    def create_asset_number():
        return random.randint(2000000, 3000000)
    def __init__(self, name, cost):
        self._category = "Printer"
        self._asset_number = self.create_asset_number()
        super().__init__(name, cost)
        
class Scanner(Item):
    @staticmethod
    def create_asset_number():
        return random.randint(3000000, 4000000)
    def __init__(self, name, cost):
        self._category = "Scanner"
        self._asset_number = self.create_asset_number()
        super().__init__(name, cost)
        
class Laptop(Item):
    @staticmethod
    def create_asset_number():
        return random.randint(4000000, 5000000)
    def __init__(self, name, cost):
        self._category = "Laptop"
        self._asset_number = self.create_asset_number()
        super().__init__(name, cost)
        
        
        
        
# Если закоментировать отсюда и до низу, то программа все будет делать автоматически
assets = {}    
created_storage = False
while True:
    
    print("Для выхода из программы введите e и нажмите Enter")
    print("Введите s для создания нового склада ") 
    if created_storage:
        print("Для перемещения оборудования на склад введите post")
        print("Для перемещения оборудования со склада введите get")
        print("Введите asset для создания новой единицы оборудования")
    user_input = input("\n")
    if user_input == "e":
        break
    if user_input == "s":
        storage = Storage(input("Введите название склада \n"))
        created_storage = True
        while True:
            print("Для выхода из меню добавления введите e и нажмите Enter")
            print("Введите asset для создания новой единицы оборудования ") 
            user_input = input("\n")
            if user_input == "e":
                break
            if user_input == "asset":
                name = input("Введите название оборудования \n")
                cost = 0
                while cost == 0:
                    try:
                        cost = float(input("Введите цену оборудования \n"))
                    except (ValueError, TypeError):
                        cost = 0
                while True:
                    user_input = input("Выберите категорию оборудования: 1-Laptop, 2- Printer, 3- Scanner \n")
                    if user_input == "1":
                        asset = Laptop(name, cost) 
                        assets[asset._asset_number] = asset
                        break
                    elif user_input == "2":
                        asset = Printer(name, cost)
                        assets[asset._asset_number] = asset
                        break
                    elif user_input == "3":
                        asset = Scanner(name, cost)
                        assets[asset._asset_number] = asset
                        break
                    else:
                        print("Неккорректный выбор")
    if user_input == "asset":
                name = input("Введите название оборудования \n")
                cost = 0
                while cost == 0:
                    try:
                        cost = float(input("Введите цену оборудования \n"))
                    except (ValueError, TypeError):
                        cost = 0
                while True:
                    user_input = input("Выберите категорию оборудования: 1-Laptop, 2- Printer, 3- Scanner \n")
                    if user_input == "1":
                        asset = Laptop(name, cost)
                        assets[asset._asset_number] = asset
                        break
                    elif user_input == "2":
                        asset = Printer(name, cost)
                        assets[asset._asset_number] = asset
                        break
                    elif user_input == "3":
                        asset = Scanner(name, cost)
                        assets[asset._asset_number] = asset
                        break
                    else:
                        print("Неккорректный выбор")
                    
    if user_input == "post":
        print("Список оборудования не на складе:")
        for k,v in assets.items():
            if v.position != storage.name:
                print(f"{v} s/n {k} position: {v.position}")
        user_input = input("Введите серийный номер оборудования, которое хотите поместить на склад \n")
        storage.move_to_storage(assets[int(user_input)])
    if user_input == "get":
        print("Список оборудования на складе:")
        for k,v in storage.assets_storage.items():
           print(k)
           for i in v:
               print(f"\t {i} s/n {i._asset_number}")
        
        storage.move_from_storage(assets[int(input("Введите серийный номер оборудования, которое хотите поместить со склада \n"))],input("Куда перемещаем?\n"))
        
print(storage)

# Для автоматической работы закомментировать досюда и раскомментировать кусок кода ниже
        
"""       
assets = {}    
storage = Storage("storage1")
asset = Laptop("Dell 7390", 1200)
assets[asset._asset_number] = asset
asset = Laptop("Dell 7280", 1300)
assets[asset._asset_number] = asset
asset = Laptop("Dell 5490", 1500)
assets[asset._asset_number] = asset

asset = Printer("hp", 1500)
assets[asset._asset_number] = asset
asset = Printer("samsung", 1500)
assets[asset._asset_number] = asset

asset = Scanner("elipson q200", 1500)
assets[asset._asset_number] = asset

asset = Scanner("elipson q300", 1500)
assets[asset._asset_number] = asset

asset = Scanner("elipson q200", 1500)
assets[asset._asset_number] = asset
print("Создали несколько единиц оргтехники и переместили ее на склад")

for k,v in assets.items():
    storage.move_to_storage(v)
print(storage)

for k, v in assets.items():
    if k in range(3000000, 4000000):   
        storage.move_from_storage(v, "office 1")
        
print("Переместили все сканеры в офис 1")       
print(storage)   
print("Вывод списка всего оборудования")
for k, v in assets.items():
    print(f"{k} {v.name} {v.position}")

"""


        
    
