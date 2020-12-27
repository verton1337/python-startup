"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
 В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». 
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""
class CreateClassError(Exception): pass

class MyDate():	
    
    @classmethod
    def validate_data(cls, input_date):
        input_date = input_date.split("-")
        input_date = [int(input_date[i]) for i in range(len(input_date))]
            
        if input_date[0] in range(1,31) and input_date[1] in range(1,13) and input_date[2] > 1900 :
            return input_date
        else:
            raise ValueError
    @staticmethod
    def check_date(input_date):
        try:
            input_date = MyDate.validate_data(input_date)
            return True
        except ValueError:
            return False
        
        
        
    def __init__(self, input_date):
        try:
            self._date = MyDate.validate_data(input_date)  
        except ValueError:
            raise CreateClassError
        #self._date = input_date.split("-")    
    def __str__(self):
        result = f"День - {self._date[0]} \nМесяц - {self._date[1]} \nГод - {self._date[2]}"
        return result
	
date_list = ["34-10-2020","12-10-12","12-100-2020","12-10-2020","28-10-2003"]  

for date in date_list:
    try:
        d1 = MyDate(date)
        print(d1)
    except CreateClassError:
        print("Произошла ошибка при создании класса")
        
        
d2 = MyDate.validate_data("12-12-2020")
print(f"Результат работы функции извлечения   {d2}")

d3 = MyDate.check_date("32-23-2333")
print(f"Результат валидации даты {d3}")