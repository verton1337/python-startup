"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.


Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json
success_count = 0
result = 0
output_dict = {}

with open("task7_file.txt", encoding = "utf-8") as f:
    lst = f.readlines()
lst = [i.split(",") for i in lst]

for i in lst:
    cost = float(i[2])-float(i[3])
    i.append(cost)
    if cost>0:
        result += cost
        success_count+=1
        print(f"Выручка {i[1]} {i[0]} составила {cost}")
    else:
        print(f"Убыток {i[1]} {i[0]} составил {cost}")
    output_dict[f"{i[1]} {i[0]}"] = i[4]
    
    
average_profit =    result/success_count
output_list = [output_dict, {"average_profit":average_profit }]    
    

print(f"Средняя выручка по фирмам, вышедшим в плюс составляет {average_profit}")
print("Основная информация по компаниям занасена в файл JSON")


with open("task7_file_write.json", "w", encoding = "utf-8") as write_f:
    json.dump(output_list, write_f, ensure_ascii=False, indent = 1)
