"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами. 
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
 Если в слово длинное, выводить только первые 10 букв в слове.
"""

user_input = input("Введите слова через пробел: ").split()

for i in range(len(user_input)):

    if len(user_input[i]) <= 10: #Если длина слова меньше 10 символов то просто печатаем его
        print(i+1, user_input[i])
        
    else: #В противном случае выводим на печать первые 10 символов
        print(i+1, user_input[i][:10])