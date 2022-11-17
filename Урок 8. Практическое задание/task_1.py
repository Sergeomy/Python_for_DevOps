"""
Задание 1.

Реализовать класс «Дата», на уровне класса определить атрибут day_month_year,
присвоить ему значение

В рамках класса реализовать два метода.

Первый, с декоратором @classmethod, должен извлекать число, месяц,
год, преобразовывать их тип к типу «Число» и делать атрибутами класса.

Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
 реальных данных.
"""


class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extraction(cls, day_month_year):
        my_date = []

        for i in day_month_year.split("/"): my_date.append(i)
        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def validation(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2200 >= year >= 0:
                    return f"Всё корректно"
                else:
                    return f"Год должен быть с 1900 по 2200"
            else:
                return f"Введён некорректный месяц (1-12)"
        else:
            return f"Введён некоректный день месяца (1-31)"

    def __str__(self):
        return f"Введённая дата: {Data.extraction(self.day_month_year)}"


today = Data("13/11/2022")
print(today)
print(Data.validation(11, 11, 2222))
print(today.validation(13, 13, 2022))
print(Data.extraction("13/11/2022"))
print(today.extraction("13/11/2222"))
print(Data.validation(1, 11, 2000))
