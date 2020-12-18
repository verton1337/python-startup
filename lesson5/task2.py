"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.
"""
dict_lines = {}
i = 0
with open("task2_file.txt","r") as f:
    for line in f:
        i+=1
        dict_lines[i]= len(line.split())
        
print(f"Всего строк - {i}")
for k, v in dict_lines.items():
    print(f"В {k} строке {v} слов")