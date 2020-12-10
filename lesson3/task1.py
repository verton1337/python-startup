"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
 Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

def devision(a,b):
	try:
		return float(a)/float(b)
	except (ValueError, ZeroDivisionError):
		return "error"

ui_a = input("Введите делимое: ")
ui_b = input("Введите делитель: ")	
result = devision(ui_a,ui_b)
if result == "error":
	print("Введены некорректные данные")
else:
	print(f"Результат деления: {result}")
		
		
		
