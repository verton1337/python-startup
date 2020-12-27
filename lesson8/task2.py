"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. 
Проверьте его работу на данных, вводимых пользователем. 
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""
import random
class MyZeroDivError(Exception): pass



def my_mul(a,b):
    if b ==0 : raise MyZeroDivError
    try:
        return round(a/b, 2)
    except (ValueError, TypeError):
        return None

lst = [0,0,0,0,1,23,12,32423,23423,12,"word","word","word"]

for i in range(30):

    a = lst[random.randint(0, len(lst)-1)]
    b = lst[random.randint(0, len(lst)-1)]
    try:
        print(f"Значаение А - {a} Значение Б - {b}")
        result = my_mul(a,b)
        print(result)
    except MyZeroDivError:
        print("Делить на ноль нельзя")

