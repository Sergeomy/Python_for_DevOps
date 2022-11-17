"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс
«Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение
созданных экземпляров.
Проверьте корректность полученного результата.
"""


class ComplexNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f"Сумма комплексных чисел равна: {self.a + other.a} + " \
               f"{self.b + other.b} * i"

    def __mul__(self, other):
        return f"Произведение комплексных чисел равно: " \
               f"{self.a * other.a - (self.b * other.b)}" \
               f" + {self.b * other.a} * i"

    def __str__(self):
        return f"c = {self.a} + {self.b} * i"


c_1 = ComplexNum(1, -3)
c_2 = ComplexNum(2, 4)
print(c_1)
print(c_2)
print(c_1 + c_2)
print(c_1 * c_2)
