"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. 
Важно, чтобы для каждого предмета не обязательно были все типы занятий. 
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) 

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

def testdigit(input_str):
    result = ""
    for i in range(len(input_str)):
        try:
            int(input_str[i])
            result += input_str[i]
        except ValueError:
            result += " "
    result = result.split()
    return result
def sum(lst):
    result = 0
    for i in lst:
        result += int(i)
    return result  
    

output_dict = {}

with open("task6_file.txt", encoding = "utf-8") as f:
    lst = f.readlines()
for i in lst:
    output_dict[i.split()[0]] = sum(testdigit(i))
    
print(output_dict)