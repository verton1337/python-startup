"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: 
имя, фамилия, год рождения, город проживания, email, телефон. 
Функция должна принимать параметры как именованные аргументы.
 Реализовать вывод данных о пользователе одной строкой.
"""

def user_info(**kwargs):
	current_params = {"name", "surname", "b_date", "country", "email", "phone"}
	inputed_params = set()
	for k,v in kwargs.items():
		if k not in current_params:
			return f"ParamsError: В функцию передан неверный параметр {k}"
		inputed_params.add(k)
	if inputed_params != current_params:
		return f"ParamsError: В функцию переданы не все параметры"
	#return {"name":,"surname":,"b_date":,"country":,"email":,"phone":}
	for v in kwargs.values():
		print(v, end=" ")
	print()
	

	
while True:
	u_name = input("Введите имя или нажмите Enter для выхода: ")
	if u_name == "":
		break
	u_surname = input("Введите фамилию: ")
	u_b_date = input("Введите дату рождения: ")
	u_country = input("Введите город: ")
	u_email = input("Введите email: ")
	u_phone = input("Введите телефон: ")
	#user_info(name="Alex", surname="Turch", b_date="07.08.1997", country="Mos" ,email="asd@asd.ru", phone="89999999999")
	result = user_info(name=u_name, surname=u_surname, b_date=u_b_date, country=u_country ,email=u_email, phone=u_phone)
	if result is not None:
		print(result)