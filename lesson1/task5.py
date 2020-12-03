user_input_cash_in = float(input("Введите размер выручки"))
user_input_cash_out = float(input("Введите размер издержек"))
if user_input_cash_in - user_input_cash_out >0:
	print("Предприятие получает прибыль больше чем убытки")
	cash_rent = (user_input_cash_in/user_input_cash_out - 1)*100
	print(f"Рентабельность выручки состовляет {cash_rent}%")
	employee_count = int(input("Введите количество сотрудников "))
	cash_in_one_employee = (user_input_cash_in - user_input_cash_out)/employee_count
	print(f"Прибыль в расчете на одного сотрудника состовляет {cash_in_one_employee}")
else:
	print("Предприятие работает в убыток")
	