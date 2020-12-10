"""
3. Реализовать функцию my_func(), 
которая принимает три позиционных аргумента, 
и возвращает сумму наибольших двух аргументов.
"""
def my_func(*args):
	func_input = []
	try:
		for el in args:
			el = float(el)
			func_input.append(el)
		func_input.sort()
		result = func_input[-1]+func_input[-2]
	except ValueError:
			result = "Введено неверное значение"
	
	return result
		
print(my_func(1,5,23))