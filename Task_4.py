# Создайте класс GameScore для отслеживания очков игрока. В этом классе
# должны быть методы для добавления и уменьшения очков. Однако:
# ● Очки не могут быть отрицательными.
# ● Если игрок пытается добавить больше очков, чем 1000, должно быть
# выброшено исключение ScoreLimitExceededError.
# Создайте пользовательское исключение ScoreLimitExceededError.
from random import randint


class ScoreLimitExceededError(Exception):
    def __init__(self):
        super().__init__('вы  не можете набрать больше 1000 очков')

class GameScore:
    def __init__(self):
        self.score = 0

    def add_score(self):
        point = randint(10, 300)
        if self.score + point >= 1000:
            exception = ScoreLimitExceededError
            raise exception
        else:
            self.score += point
        return self.score

    def take_away_score(self):
        point = randint(10, 300)
        if self.score - point < 0:
            self.score = 0
        else:
            self.score -= point
        return self.score

if __name__ == '__main__':
    score = GameScore()
    score.add_score()
    score.take_away_score()
    score.add_score()
    print(score.add_score())





