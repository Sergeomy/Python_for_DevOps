"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на
нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем
 нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не
завершиться с ошибкой.
"""


class DivZero(Exception):
    def __init__(self, txt):
        self.txt = txt


def div():
    try:
        nmb_1 = int(input("Что делить: "))
        nmb_2 = int(input("На что делить: "))
        if nmb_2 == 0:
            raise DivZero("Вы пытаетесь разделить на ноль.")
        else:
            answ = nmb_1 / nmb_2
            return answ
    except ValueError:
        print("Вы ввели не число")
    except DivZero as err:
        return err


print(div())
