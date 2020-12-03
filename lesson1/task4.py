user_input = input ("Введите целое положительное число ")
#print(max(user_input))
i=0
max_number = 0
while i < len(user_input):
	if int(user_input[i])>max_number:
		max_number = int(user_input[i])
	i+=1
print(f"Самая большая цифра в числе - {max_number}")