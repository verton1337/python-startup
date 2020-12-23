"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""

user_input=1
lst = []
while user_input:
    user_input = input("Введите текст: ")
    if user_input != "":
        lst.append(f"{user_input}\n")
f = open("task1_file.txt", "wt")
f.writelines(lst)
f.close()
print("Результат выполнения программы в файле task1_file.txt")