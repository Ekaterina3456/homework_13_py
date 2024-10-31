# Один буддист-программист решил создать свой симулятор жизни, в котором
# нужно набрать 500 очков кармы (это константа), чтобы достичь просветления.
# Каждый день вызывается специальная функция one_day(), которая возвращает
# количество кармы от 1 до 7 и может с вероятностью 1 к 10 выкинуть одно из
# исключений:
# ● KillError,
# ● DrunkError,
# ● CarCrashError,
# ● GluttonyError,
# ● DepressionError.
# (Исключения нужно создать самостоятельно, при помощи наследования от
# Exception.)
# Напишите такую программу. Функцию оберните в бесконечный цикл, выход из
# которого возможен только при накоплении кармы до уровня константы.
# Исключения обработайте и запишите в отдельный лог karma.log.
# По итогу у вас может быть примерно такая структура программы:
# открываем файл
# цикл по набору кармы
# try
# карма += one_day()
# except(ы) с указанием классов исключений, которые нужно поймать
# добавляем запись в файл
# закрываем файл

from random import randint, random, choice

MAX_CARMA = 500

class KillError(Exception):
    def __init__(self):
        super().__init__('вы убили муху, получение кармы невозможно')

class DrunkError(Exception):
    def __init__(self):
        super().__init__("вы выпили получение кармы невозможно")

class CarCrushError(Exception):
    def __init__(self):
        super().__init__('вы попали в аварию')

class GluttonyError(Exception):
    def __init__(self):
        super().__init__('вы слишком много сели, получение кармы невозможно')

class DepressionError(Exception):
    def __init__(self):
        super().__init__('вы впали в уныние, получение кармы невозможно')




def one_day():
    carma = 0
    if randint(1, 10) == 1:
        exception = choice([KillError, DrunkError, CarCrushError, GluttonyError, DepressionError])
        raise exception
    else:
        carma += randint(1, 7)
    return carma


if __name__ == '__main__':
    karma = 0

    with open('karma.log', 'a', encoding='utf-8') as f_karma:
        while True:
            try:
                karma += one_day()
            except Exception as e:
                f_karma.write(f'{e}\n')
            if karma >= MAX_CARMA:
                break

    print('вы накопили карму')
