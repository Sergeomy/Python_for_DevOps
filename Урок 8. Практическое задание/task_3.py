"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у
пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class ValError(Exception):
    def __init__(self):
        pass


# noinspection PyGlobalUndefined
class TypeCheck:
    def __init__(self):
        self.lst = []

    def check_val(self):
        global in_val
        while True:
            try:
                try:
                    in_val = int(input("Введите число: "))
                    ex = input(f"Всё отлично, добавляем '{in_val}' в список."
                               f"(q - выход, Enter - продолжить): ").lower()
                    self.lst.append(in_val)
                    if ex == "q":
                        print(self.lst)
                        break
                except ValueError:
                    raise ValError
            except ValError:
                ex = input(f"Введите число! (q - выход, Enter - продолжить):"
                           f" ").lower()
                if ex == "q":
                    print(self.lst)
                    break
                else:
                    self.check_val()


a = TypeCheck()
a.check_val()
