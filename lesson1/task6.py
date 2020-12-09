first_day = float(input("Введите результат в первый день"))
need_result = float(input("Введите какого результата хотите достичь"))
need_time = 1
while (first_day < need_result):
	need_time +=1
	first_day = first_day*1.1
print(f"на {need_time}-й день спортсмен достиг результата — не менее {need_result} км.")