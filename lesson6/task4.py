"""
4. Реализуйте базовый класс Car.
 У данного класса должны быть следующие атрибуты:
 speed, color, name, is_police (булево).
 А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). 
 Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
 Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""

class Car():
    
    _speed_coef = 1.3
    _speed_limit = 180
    def __init__(self, name, color):
        self._speed = 0
        self.color = color
        self.name = name
        
    def go(self, turn_time):
        if self._speed == 0:
            print(f"Машина {self.name} поехала")
        for i in range(turn_time):
            self._speed += int(self._speed_coef**4 * turn_time)
            if self._speed >= self._speed_limit:
                self._speed = self._speed_limit
                print(f"Машина {self.name} достигла лимита скорости {self._speed}")
                break
            else:
                print(f"Скорость {self.name} составляет {self._speed}")
        
        
    def stop(self):
        self._speed = 0
        print(f"Машина {self.name} остановилась")
        
    def turn(self, direction):
        if self._speed != 0:
            derect_dict = {"left":"налево", "right":"направо"}
            print(f"Машина {self.name} повернула {derect_dict[direction]}")
        else:
            print("Машина не может поворачивать, когда стоит на месте")
    def show_speed(self):
        print(f"Текущая скорость {self._speed}")


class TownCar(Car):
    _speed_limit = 60

class WorkCar(Car):
    _speed_limit = 40
    
class SportCar(Car):
        _speed_coef = 1.8
        _speed_limit = 300
            
class PoliceCar(Car):
    def __init__(self, name, color):
            self._is_police = True
            super().__init__(name,color)
            
c1 = TownCar("KIA","red")
c1.go(10)
c1.show_speed()
c1.stop()
c1.turn("left")
c1.go(10)
c1.turn("left")


sc1 = SportCar("Bugatti", "black")
sc1.go(10)
sc1.show_speed()
sc1.stop()
sc1.turn("left")
sc1.go(10)
sc1.turn("right")




