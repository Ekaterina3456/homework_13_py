# Напишите программу, которая запрашивает у пользователя число до тех пор, пока
# сумма этих чисел не станет больше либо равна 777. Каждое введенное число при этом
# дозаписывается в файл. Сделайте так, чтобы перед дозаписью программа с
# вероятностью 1 к 13 выбрасывала пользователю случайное исключение и
# завершалась.
import os
from random import randint

NUMBER = 777

class BadLuck(Exception):
    def __init__(self):
        super().__init__('Неудача!')

class CountNum:
    def __init__(self, number, filename = 'numbers.txt'):
        self.number = number
        self.filename = filename

    def write_num(self):
        with open(self.filename, 'a', encoding='utf-8') as f_num:
            f_num.write(f'{self.number}\n')


    def input_num(self):
        self.number = input('введите число ')
        if randint(1, 13) == 3:
            exception = BadLuck
            raise exception
        return self.number


    def find_summa(self) -> int:
        summa = 0
        while summa < NUMBER:
            summa += int(self.input_num())
            self.write_num()

        return summa


if __name__ == '__main__':
     num = CountNum(0)
     num.find_summa()