"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12. 
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
 Напишите решения через list и через dict.
"""
seasons_dict = {(1,2,12):"Зима",(3,4,5):"Весна",(6,7,8):"Лето",(9,10,11):"Осень"}
user_input = int(input("Введите номер месяца: "))
#С помощью dict
for key, val in seasons_dict.items():
    if user_input in key:
        season = val
        print(season)
        break
#С помощью list
w = "Зима" #Зима
o = "Осень" #Осень
su = "Лето" #Лето
sp = "Весна" #Весна
seasons_list = [w,w,sp,sp,sp,su,su,su,o,o,o,w]
print(seasons_list[user_input-1])
