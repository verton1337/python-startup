"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
 Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""

class ComplexNum():
    def __init__(self,a,ki):
        self._a = a
        self._ki = ki
    #z=z1⋅z2=(a1a2−b1b2)+(a1b2+b1a2)i
    def __mul__(self, other):
        a1 = self._a
        b1 = self._ki
        a2 = other._a
        b2 = other._ki
        a = a1*a2 - b1 * b2
        ki = a1 * b2 + b1 * a2
        return ComplexNum(a,ki)
    def __add__(self, other):
        a = self._a + other._a
        ki = self._ki + other._ki
        return ComplexNum(a,ki)
    def __str__(self):
        return f"{self._a} + {self._ki}i"
    
    
    
print("Входные данные: a = 3 + 5i, b = 2 + 6i")

    
a = ComplexNum(3,5)
b = ComplexNum(2, 6)

print("Пробуем со своим классом")
print(a+b)
print(a*b)


print("Пробуем со встроенным классом")

a1 = 3+5j
b1 = 2 + 6j
print(a1+b1)
print(a1*b1)
