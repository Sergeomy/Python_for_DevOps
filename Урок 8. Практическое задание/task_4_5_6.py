"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий
 склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа
оргтехники.

5. Продолжить работу над четвертым заданием.
Разработать методы, отвечающие за приём оргтехники на
склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и
количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над пятым заданием. Реализуйте механизм валидации вводимых
 пользователем данных.
Например, для указания количества принтеров,
отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте
«Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""


class Storage:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.whouse_full = []
        self.whouse = []
        self.unit = {"Модель устройства": self.name,
                     "Цена за ед": self.price,
                     "Количество": self.quantity}

    def income(self):
        try:
            unit = input(f"Введите наименование: ")
            unit_p = int(input(f"Введите цену за ед: "))
            unit_q = int(input(f"Введите количество: "))
            units = {"Модель устройства": unit,
                     "Цена за ед": unit_p,
                     "Количество": unit_q}
            self.unit.update(units)
            self.whouse.append(self.unit)
            print(f"Текущий список -\n {self.whouse}")
        except ValueError:
            return f"Ошибка ввода данных. Текущий список -\n {self.whouse}"

        print(f'Для выхода - Q, продолжение - Enter')
        q = input("")
        if q == 'Q' or q == 'q':
            self.whouse_full.append(self.whouse)
            print(f'Весь склад -\n {self.whouse_full}')
            return f'Выход'
        else:
            return Storage.income(self)


class Printer(Storage):
    def to_print(self):
        return self.unit


class Scanner(Storage):
    def to_scan(self):
        return self.unit


class Copier(Storage):
    def to_copier(self):
        return self.unit


unit_1 = Printer('hp', 2000, 5)
print(unit_1.income())
print(unit_1.to_print())
