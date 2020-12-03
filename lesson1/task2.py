# -*- coding: utf-8 -*-
user_input = int(input ("Введите время в секундах "))
hours = user_input // 3600
result = user_input % 3600
minutes = result // 60
secs = result % 60
print(f"Время: {hours}:{minutes}:{secs}")