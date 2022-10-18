"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


# Функция сложения двух наибольших чисел из трёх введённых (без sort())
def my_func_1(a, b, c):
    arg = [a, b, c]
    arg.remove(min(a, b, c))
    return sum(arg)


# Приглашение для пользователя для ввода данных
print(my_func_1(int(input("Введите первое число: ")),
                int(input("Введите второе число: ")),
                int(input("Введите третье число: "))))


# Функция сложения двух наибольших чисел из трёх введённых (с sort())
def my_func_2(a, b, c):
    arg = [a, b, c]
    arg.sort()
    del arg[0]
    return sum(arg)


# Приглашение для пользователя для ввода
print(my_func_2(int(input("Введите первое число: ")),
                int(input("Введите второе число: ")),
                int(input("Введите третье число: "))))
