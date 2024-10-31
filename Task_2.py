# Реализуйте программу - чат, в котором могут участвовать сразу несколько человек, то
# есть программа может работать одновременно для нескольких пользователей. При
# запуске запрашивается имя пользователя. После этого он выбирает одно из действий:
# 1. Посмотреть текущий текст чата
# 2. Отправить сообщение (затем вводит сообщение) Действия запрашиваются
# бесконечно.
from pathlib import Path


class Chat:
    def __init__(self, filename = 'chat.txt'):
        self.filename = filename

    def look_chat(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as read:
                massage = read.readline()
                print(massage)
        except FileNotFoundError as e:
            print('пока что данный чат пуст')

    def add_massage(self, name, massage):
        with open(self.filename, 'a', encoding='utf-8') as add:
            add.write(f'{name}: {massage}\n')

    def start(self):
        name = input('введите ваше имя ')
        while True:
            choice = int(input('выбирите действие:\n 1)просмотреть чат\n 2)написать сообщение\n 3)выйти '))
            match choice:
                case 1:
                    self.look_chat()
                case 2:
                    text = input('введите сообщение ')
                    self.add_massage(name, text)
                case 3:
                    break

if __name__ == '__main__':
    chat = Chat()
    chat.start()


