"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
 Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
 Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. 
 Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""
class Road():
    weight_sm = 25 #Вес одного квадратного метра асфальта толщиной 1 см
    def __init__(self,length,width):
        try:
            self._length = int(length)
            self._width = int(width)
        except (ValueError):
            print("Ошибка в веденный данных")
        
    def mass(self, height = 5):
        try:
            result = self._length * self._width * self.weight_sm * height / 1000
        except AttributeError:
            return "Введены некорректные данные в тело класса"
        return result
        
r1 = Road(5000,"20rt")

print(f"Масса асфальта составит {r1.mass()}")