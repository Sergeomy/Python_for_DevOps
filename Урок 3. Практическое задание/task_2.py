"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания,
 email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


# Функция заполнения кортежа данными пользователя
def pers_data(name, familyname, birth_ye, city, email, phone):
    return print(f'Имя: {name} Фамилия: {familyname} Год рождения: {birth_ye}'
                 f'Город проживания: {city} Email: {email} Телефон: {phone}')


# Приглашение для ввода данных
pers_data(
    name=input('Имя: '),
    familyname=input('Фамилия: '),
    birth_ye=input('Год Рождения: '),
    city=input('Город проживания: '),
    email=input('email: '),
    phone=input('phone: '),
)
