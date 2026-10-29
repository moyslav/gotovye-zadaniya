# -*- coding: utf-8 -*-
"""
Задание 2 (урок 15. API, JSON).
Дан код, который делает GET-запрос к сайту с фактами о числах
(numbersapi.com) и печатает ответ.

Что нужно переделать:
1. Месяц и день вводит пользователь.
2. Таких запросов должно быть 10.
3. Все ответы от сервиса нужно записать в файл в формате json.

Перед запуском нужно установить библиотеку requests:  pip install requests
"""

import json      # для записи ответов в json-файл
import requests  # для HTTP-запросов к сайту

sl = {}  # словарь, куда сложим все ответы: ключ — номер запроса, значение — факт
head = {'Content-Type': 'application/json'}  # заголовок: ждем ответ в формате json

for i in range(10):  # всего 10 запросов
    m = int(input('Введите месяц: '))  # месяц, например 9
    d = int(input('Введите число: '))  # день, например 2
    # Подставляем месяц и день прямо в адрес запроса через f-строку.
    # Роут /месяц/день/date выдает факт о том, что произошло в этот день.
    response = requests.get(f'http://numbersapi.com/{m}/{d}/date', headers=head)
    sl[i] = response.json()  # переводим ответ сервиса из json в объект Python

# Сохраняем все собранные факты в файл.
# encoding='utf-8' и ensure_ascii=False — чтобы русские символы писались нормально.
with open('facts.json', 'w', encoding='utf-8') as fl:
    json.dump(sl, fl, indent=4, ensure_ascii=False)

print('Готово, факты сохранены в файл facts.json')
