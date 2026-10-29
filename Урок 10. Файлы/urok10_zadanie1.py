# -*- coding: utf-8 -*-
# Задание 1.
# Написать программу, которая в текущем каталоге создает текстовый файл stichi.txt
# Записывает в него следующий стих (используя print или write)

# Открываем файл stichi.txt на запись в текстовом режиме.
# encoding='utf-8' нужен, чтобы не было проблем с кириллицей и спецсимволами.
fl = open("stichi.txt", "wt", encoding='utf-8')

# Сам стих храним в одной многострочной переменной, так удобнее записать его целиком.
poem = """We walk through the years like steps.
No need to whine that our ascent is hard.
If we suddenly don't find a new step —
The way back is always a moment."""

# Записываем стих в файл методом write
fl.write(poem)

# Не забываем закрыть файл, чтобы данные точно сохранились на диск
fl.close()
