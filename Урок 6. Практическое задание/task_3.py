"""
Задание 3.

Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например,
{"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии
(get_total_income).

Проверить работу примера на реальных данных (создать экземпляры класса
Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).

П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку
 __str__
__str__(self) - вызывается функциями str, print и format.
Возвращает строковое представление объекта.
"""


# Определяем класс
class Worker:

    # Задаём атрибуты
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}


# Создаём класс на бвзе Worker
class Position(Worker):

    # Метод получения полного имени
    def get_full_name(self):
        return self.name + ' ' + self.surname

    # Метод получения полного дохода
    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

# Передаём значения
pos = Position("Руслан", "Новиков", "Дизайнер", "150000", "30000")

print(pos.name)
print(pos.surname)
print(pos.position)
print(pos.get_full_name(), pos.get_total_income())
