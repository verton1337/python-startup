"""
2. Представлен список чисел.
Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

"""
"""
def upper_el(lst):
	result = []
	for i in range(len(lst)):
		try:
			if lst[i+1]>lst[i]:
				result.append(lst[i+1])
		except IndexError:
			continue
	return result
	
result = upper_el([300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55])
print (result)
"""
lst = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [el for el in lst if lst[lst.index(el)-1]<el and lst.index(el)>0]
print(result)