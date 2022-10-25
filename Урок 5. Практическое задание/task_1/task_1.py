"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

fl = open("file_1.txt", "w", encoding="utf-8")
data = input("Введите данные (пустая строка - выход): ")

while True:
    fl.writelines(data + "\n")
    data = input("Введите данные (пустая строка - выход): ")
    if data == '':
        break

fl.close()
fl = open("file_1.txt", "r")
body = fl.readlines()
print(body)
fl.close()
