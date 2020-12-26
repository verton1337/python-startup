"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
 Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
 Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
 Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). 
 Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""

class TrafficLight():
    red_light = 7
    yelow_light = 2
    green_light = 30
    color_dict = {"Red":red_light,"Yellow":yelow_light,"Green":green_light}
    def __init__(self, color):
        self.__color = color
        
    def running(self):
        for k,v in self.color_dict.items():
            self.__color = k
            for i in range(v):
                print(f"Сейчас горит {self.__color}")
                
    
        
        
sw1 = TrafficLight("Green")
sw1.running()
