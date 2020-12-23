"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, 
открывающую файл на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""

keywords_dict = {"One":"Один","Two":"Два","Three":"Три","Four":"Четыре"}


with open("task4_file.txt", encoding='utf-8') as f:
    lst = f.readlines()
lst = [i.split() for i in lst]


for i in lst:
    if i[0] in keywords_dict.keys():
        i[0] = keywords_dict[i[0]]
   

lst = [f"{i[0]} {i[1]} {i[2]} \n" for i in lst]  
 
 
with open("task4_file_write.txt", "w", encoding='utf-8') as f:
    f.writelines(lst)

    