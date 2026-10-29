# -*- coding: utf-8 -*-
# Задание 1 (урок 6).
# Из введенной строки делаем список и удаляем буквы 'a', 'e', 'u'.

st = list(input("Введите строку: "))  # превращаем строку в список символов

# Метод remove удаляет только первое вхождение,
# поэтому цикл повторяем столько раз, сколько букв осталось в списке.
for i in range(st.count('a')):
    st.remove('a')
for i in range(st.count('e')):
    st.remove('e')
for i in range(st.count('u')):
    st.remove('u')

print(st)

# Другой вариант — через while, пока буква есть в списке:
# q = list(input())
# while 'a' in q: q.remove('a')
# while 'e' in q: q.remove('e')
# while 'u' in q: q.remove('u')
# print(q)
