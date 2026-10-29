# -*- coding: utf-8 -*-
"""
Задание 1 (урок 12. ООП, классы и объекты).
Создать 2 класса (Маг и Воин), которые будут содержать характеристики персонажа в РПГ игре
(Ник, раса, пол, цвет волос, тип внешности).
Методы Воин:
1) удар мечом - наносит 2 урона
2) удар щитом - наносит 1 урон
3) исцеление - восстанавливает 5 здоровья
Методы Маг:
1) огненный шар - наносит 5 урона и произносится 5 секунд
2) заморозка - наносит 1 урона
3) исцеление - восстанавливает 5 здоровья
Пользователь вводит все с клавиатуры и заполняет атрибуты будущего объекта.
Пользователь выбирает класс и в зависимости от этого создается объект.
"""


class Mag:
    # конструктор принимает все характеристики и раскладывает их по атрибутам объекта
    def __init__(self, nikname, rasa, gender, collorh, tip):
        self.nik = nikname
        self.rasa = rasa
        self.gender = gender
        self.collorh = collorh
        self.tip = tip

    def firebol(self):
        print('Огненный шар - 5 урона, произнесение 5 секунд')

    def freez(self):
        print('Заморозка - 1 урона')

    def hills(self):
        print('Восстановление 5 единиц здоровья')

    # метод info выводит всю информацию о персонаже
    def info(self):
        print(f'Класс МАГ')
        print(f'Ник: {self.nik}')
        print(f'Раса: {self.rasa}')
        print(f'Пол: {self.gender}')
        print(f'Цвет волос: {self.collorh}')
        print(f'Тип внешности: {self.tip}')
        print(f'Доступно:\nfirebol - огненный шар\nfreez - заморозка\nhills - исцеление')


class Warr:
    # у воина те же характеристики, но свои методы атак
    def __init__(self, nikname, rasa, gender, collorh, tip):
        self.nik = nikname
        self.rasa = rasa
        self.gender = gender
        self.collorh = collorh
        self.tip = tip

    def sword(self):
        print('Удар мечом - 2 урона')

    def shild(self):
        print('Удар щитом - 1 урона')

    def hills(self):
        print('Восстановление 5 единиц здоровья')

    def info(self):
        print(f'Класс ВОИН')
        print(f'Ник: {self.nik}')
        print(f'Раса: {self.rasa}')
        print(f'Пол: {self.gender}')
        print(f'Цвет волос: {self.collorh}')
        print(f'Тип внешности: {self.tip}')
        print(f'Доступно:\nsword - удар мечом\nshild - удар щитом\nhills - исцеление')


# спрашиваем пользователя, какого класса персонажа он хочет создать
pers = (input('Персонажа какого класса хотите создать? \n 1 - Маг\n 2 - Воин\n'))
if pers:  # если что-то ввели
    # все характеристики персонажа заполняются с клавиатуры
    nik = input('Введите ник: ')
    rasa = input('Введите расу: ')
    gender = input('Введите пол: ')
    collorh = input('Введите цвет волос: ')
    tip = input('Введите тип внешности: ')

    # в зависимости от выбора создаем объект нужного класса
    if pers == '1':
        persona = Mag(nik, rasa, gender, collorh, tip)
    elif pers == '2':
        persona = Warr(nik, rasa, gender, collorh, tip)

persona.info()  # выводим информацию о созданном персонаже
