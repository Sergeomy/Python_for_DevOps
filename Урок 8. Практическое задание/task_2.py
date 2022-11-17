"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на
нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем
 нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не
завершиться с ошибкой.
"""


class ZeroDiv:
    def __init__(self, number, denominator):
        self.number = number
        self.denominator = denominator

    @staticmethod
    def div_by_zero(number, denominator):
        try:
            return number / denominator
        except ZeroDivisionError:
            return f"Деление на ноль."


div = ZeroDiv(10, 100)
print(div.div_by_zero(10, 1))
print(div.div_by_zero(100, 0))
