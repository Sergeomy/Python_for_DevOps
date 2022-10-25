"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

i = 0
words = 0
lines = 0

with open("file_2.txt", "r", encoding="utf-8") as file:
    for line in file:
        i += 1
        lines += 1
        words = len(line.split())
        print(f"Количество слов в строке {i} : {words}")

print(f"Количество строк в файле: {lines}")
