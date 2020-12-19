"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, 
что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
 Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""
from itertools import count, cycle

def int_num(num, end = 1000):
	result = []
	for el in count(num):
		if el<=end:
			result.append(el)
		else:
			return result
			

def circle_el(lst, end=1000):
	i = 0
	result = []
	for el in cycle(lst):
		if i<end:
			result.append(el)
			i+=1
		else:
			return result
	
	
	
	
int_el = int_num(3,100)
print(int_el)

cycle_el_result = circle_el([1,"e", True],12)
print(cycle_el_result)


