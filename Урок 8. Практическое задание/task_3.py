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
        self.lst = []

    def check_val(self):
        while True:
            try:
                try:
                    in_val = int(input("Введите число: "))
                    ex = input(f"Всё отлично, добавляем '{in_val}' в список."
                               f"(q - выход): ").lower()
                    self.lst.append(in_val)
                    print(self.lst)
                    if ex == "q":
                        print(self.lst)
                        break
                except ValueError:
                    raise ValError
            except ValError:
                ex = input(f"Необходимо ввести число. "
                           f"(q - выход): ").lower()
                if ex == "q":
                    print(self.lst)
                    break
                else:
                    print(self.lst)


a = ValError()
a.check_val()
