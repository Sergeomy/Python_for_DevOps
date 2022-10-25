"""
4)	Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую
построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
# Задаём начальные параметры
i = 0
words = 0
lines = 0

# Открываем и читаем исходный файл построчно
with open("file_3.txt", "r", encoding="utf-8") as file:
    for line in file:
        i += 1
        lines += 1
        print(line)

# Меняем английские числительные на русские
with open("file_3.txt", "r", encoding="utf-8") as file:
    data = file.read()
    data = data.replace("One", "Один").replace("Two", "Два")\
        .replace("Three", "Три").replace("Four", "Четыре")

# Записываем данные в новый файл
with open("file_3_ru.txt", "w", encoding="utf-8") as file:
    file.write(data)

# Проверяем, что записали в новый файл
with open("file_3_ru.txt", "r", encoding="utf-8") as file_new:
    new_data = file_new.read()
    print(new_data)
