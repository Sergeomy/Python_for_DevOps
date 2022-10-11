"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
n = int(input("Введите целое число: "))
nn = str(n) + str(n)
nnn = str(n) + str(n) + str(n)
s = n + int(nn) + int(nnn)
print(f"n + nn + nnn = {s}")
