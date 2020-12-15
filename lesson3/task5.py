"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
 При нажатии Enter должна выводиться сумма чисел.
 Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. 
 Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. 
 Но если вместо числа вводится специальный символ, выполнение программы завершается.
 Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме 
 и после этого завершить программу.

"""
def sum(lst):
	result = 0
	for el in lst:
		result+=el
	return result

lst = []
result = 0
exitcode = 0
while exitcode == 0:
	user_input = input("Введите числа разделенные пробелом").split()
	try:
		for el in user_input:
			lst.append(float(el))
	except ValueError:
		exitcode = 1
	finally:
		result =sum(lst)
	print(result)