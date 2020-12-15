"""
4. Программа принимает действительное положительное число x и целое отрицательное число y.
 Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). 
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
"""
def my_func(x,y):

	try:
		y = int(y)
	except ValueError:
		return "Введено некорректное число Y"
	try:
		x = float(x)
	except ValueError:
		return "Введено некорректное число X"
	if x <=0:
		return "Число X должно быть положительным"
	if y>=0:
		return "Число Y должно быть отрицательное"
	result = 1
	i = 1
	while i<= y*(-1):
		result/=x
		i+=1
	return result
x = input("Введите положительное число X: ")
y = input("Введите отрицательное число Y: ")
print(my_func(x,y))