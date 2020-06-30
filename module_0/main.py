import numpy as np


def score_game(game_core_name, game_core_func):
    """Запускаем игру 1000 раз, чтоб узнать как быстро игра угадывает число"""

    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(100, size=(1000))

    count_ls = [game_core_func(x) for x in random_array]
    score = int(np.mean(count_ls))

    print(f"Алгоритм {game_core_name} угадывает число в среднем за {score} попыток")

    return score


def game_core_v1(number):
    """Просто угадываем перебором никак не используя информацию о больше или меньше.
       Функция Принимает загаданное число и возвращает число попыток"""
    count = 0
    while number != count:
        count += 1

    return count  # выход из цикла, если угадали


def game_core_v2(number):
    """Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток"""
    count = 0
    predict = 50
    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return count  # выход из цикла, если угадали


def game_core_v3(number):
    """Выполняем бинарный поиск"""

    count = 0
    step = predict = 50

    while number != predict:
        count += 1
        step = max(step // 2, 1)

        if number > predict:
            predict = predict + step
        else:
            predict = predict - step

    return count  # выход из цикла, если угадали


score_game("game_core_v1", game_core_v1)
score_game("game_core_v2", game_core_v2)
score_game("game_core_v3", game_core_v3)
