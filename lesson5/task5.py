"""
5. Создать (программно) текстовый файл, 
записать в него программно набор чисел, разделенных пробелами.
 Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import random

def sum(lst):
    result = 0
    for i in lst:
        result += float(i)
    return result
    
    
    
with open("task5_file.txt","w") as f:
    for i in range(1,random.randint(1,100)):
        f.write(f"{random.randint(1,100)} ")

with open("task5_file.txt","r") as f:
    lst = f.readline().split()
print(f"Сумма чисел в файле равна {sum(lst)}")
