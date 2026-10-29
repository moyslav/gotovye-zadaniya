# -*- coding: utf-8 -*-
# Задание 5 (урок 8).
# Функция возвращает список только из уникальных элементов.

import random  # модуль случайных чисел


def my_f(sp):
    # Превращаем список в множество (дубликаты исчезают),
    # потом обратно в список.
    new_sp = list(set(sp))
    return new_sp


old_sp = []  # исходный список
for i in range(20):                       # 20 повторений
    old_sp.append(random.randint(1, 30))  # заполняем случайными числами

print(old_sp)
print(my_f(old_sp))
