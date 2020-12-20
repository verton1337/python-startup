"""
5. Реализовать класс Stationery (канцелярская принадлежность). 
Определить в нем атрибут title (название) и метод draw (отрисовка). 
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
 Для каждого из классов методы должен выводить уникальное сообщение.
 Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""

class Stationery(): 
    def __init__(self, title):
        self.title = title
    def draw(self):
        print("Запуск отрисовки")
        
class Pen(Stationery):

    def draw(self):
        print("Рисование ручкой")
        
class Pencil(Stationery):

    def draw(self):
        print("Рисование карандашом")
        
class Handle(Stationery):

    def draw(self):
        print("Рисование маркером")
    
stat1 = Stationery("Pencil")  
pen1 = Pen("Pen")
pencil1 = Pencil("Pencil")
handle1 = Handle("Handle")


stat1.draw()
pen1.draw()
pencil1.draw()
handle1.draw()


