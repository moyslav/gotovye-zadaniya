# -*- coding: utf-8 -*-
"""
Задание 1 (урок 13. ООП, классы и объекты. Продолжение).
Расширить программу следующим образом:
Добавить еще характеристики персонажам, такие как Здоровье и Базовый урон.
Т.е. у классов есть три общие характеристики: Здоровье, Базовый урон и способность исцеления.
Создать общий класс, который будет являться родительским, вынести его в отдельный файл
и подключать в виде модуля к основному файлу.
В основном файле происходит так же создание объекта класса.
Все характеристики персонажа вводятся с клавиатуры (часть с прошлого задания плюс новые Здоровье и Базовый урон).
Методы классов изменятся следующим образом: к урону метода добавляется базовый урон.
Т.е. если удар мечом наносил 2 урона, то теперь он наносит 2+базовый урон (по аналогии все атакующие методы).
"""

# подключаем родительский класс из отдельного файла char_pers.py
from char_pers import Base


class Mag(Base):
    # маг наследуется от Base, поэтому в конструкторе сначала вызываем super().__init__
    # чтобы заполнить общие характеристики, а потом уже свои
    def __init__(self, nikname, rasa, gender, collorh, tip, base_damag, base_hp):
        super().__init__(base_damag, base_hp)
        self.nik = nikname
        self.rasa = rasa
        self.gender = gender
        self.collorh = collorh
        self.tip = tip

    def firebol(self):
        # к урону заклинания добавляется базовый урон персонажа
        print(f'Огненный шар - {5 + self.base_damage} урона, произнесение 5 секунд')

    def freez(self):
        print(f'Заморозка - {1 + self.base_damage} урона')

    def hills(self):
        # исцеление берем из родительского класса
        super().healing()

    def info(self):
        print(f'Класс МАГ')
        print(f'Ник: {self.nik}')
        print(f'Раса: {self.rasa}')
        print(f'Пол: {self.gender}')
        print(f'Цвет волос: {self.collorh}')
        print(f'Тип внешности: {self.tip}')
        print(f'Доступно:\nfirebol - огненный шар\nfreez - заморозка\nhills - исцеление')


class Warr(Base):
    # воин устроен так же, отличается только набор атак
    def __init__(self, nikname, rasa, gender, collorh, tip, base_damag, base_hp):
        super().__init__(base_damag, base_hp)
        self.nik = nikname
        self.rasa = rasa
        self.gender = gender
        self.collorh = collorh
        self.tip = tip

    def sword(self):
        print(f'Удар мечом - {2 + self.base_damage} урона')

    def shild(self):
        print(f'Удар щитом - {1 + self.base_damage} урона')

    def hills(self):
        super().healing()

    def info(self):
        print(f'Класс ВОИН')
        print(f'Ник: {self.nik}')
        print(f'Раса: {self.rasa}')
        print(f'Пол: {self.gender}')
        print(f'Цвет волос: {self.collorh}')
        print(f'Тип внешности: {self.tip}')
        print(f'Доступно:\nsword - удар мечом\nshild - удар щитом\nhills - исцеление')


# выбор класса персонажа
pers = (input('Персонажа какого класса хотите создать? \n 1 - Маг\n 2 - Воин\n'))
if pers:
    # старые характеристики из прошлого задания
    nik = input('Введите ник: ')
    rasa = input('Введите расу: ')
    gender = input('Введите пол: ')
    collorh = input('Введите цвет волос: ')
    tip = input('Введите тип внешности: ')
    # новые общие характеристики — здоровье и базовый урон
    base_d = int(input('Введите базовый урон: '))
    base_hp = int(input('Введите здоровье: '))

    if pers == '1':
        persona = Mag(nik, rasa, gender, collorh, tip, base_d, base_hp)
    elif pers == '2':
        persona = Warr(nik, rasa, gender, collorh, tip, base_d, base_hp)

persona.info()
