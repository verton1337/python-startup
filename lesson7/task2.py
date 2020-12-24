"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды. 
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
 К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
 Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). 
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: 
реализовать абстрактные классы для основных классов проекта,
 проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod

class Order():
	
	def __init__(self, *lst):
		self.__dress_lst = lst
	
	def __add__(self, other):
		self.__dress_lst.append(other)
		return self.__dress_lst
	def __str__(self):
		result = 0
		for i in self.__dress_lst:
			result += i.expense
		return str(result)

class Dress(ABC):
	@abstractmethod
	def expense(self):
		pass
		
class Costume(Dress):
	def __init__(self, height):
		self._height = height
		self.__expense = round(2 * self._height + 0.3, 2)
	@property
	def expense(self):
		return self.__expense
	
class Coat(Dress):
	def __init__(self, value):
		self._value = value
		self.__expense = round(self._value / 6.5 + 0.5, 2)
	@property
	def expense(self):
		return self.__expense
		
		
coat1 = Coat(160)
costume1 = Costume(46)

print(f"Количество материала для пальто {coat1.expense}")
print(f"Количество материала для костюма {costume1.expense}")

o1 = Order(coat1,costume1)
print(f"Общее количество материала {o1}")