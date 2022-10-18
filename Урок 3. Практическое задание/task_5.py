"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При
 нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить
 ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных
 чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа
 вводится специальный символ, выполнение программы завершается.
 Если специальный символ введен после нескольких чисел, то вначале нужно
 добавить сумму этих чисел к полученной ранее сумме и после этого завершить
 программу.
"""


# Функция подсчёта суммы введённых чисел, до тех пор пока на будет введён
# символ.
def adder(*nums):
    # Начальные условия
    num_sum = 0
    stp_f = False
    # Перебор введённых чисел для подсчёта суммы
    for i in nums:
        # Проверка на ввод символов
        try:
            if i:
                num_sum += int(i)
        except ValueError:
            print(f"Выход.")
            stp_f = True
    return num_sum, stp_f


# Приглашение для ввода чисел и подсчёта общего результата через функцию
# adder(*nums)
tot = 0
while True:
    num_str = input("Введите числа через пробел или ! для выхода: ").split()
    sums, stp = adder(*num_str)
    tot += sums
    print(f"Общая сумма: {tot}")

    if stp:
        break
