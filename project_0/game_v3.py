import numpy as np

def cycle_predict(number:int=1) -> int:
    """Угадываем число с помощью цикла while

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0
    min_number = 0 # Минимальное значение рассматриваемого интервала
    max_number = 100 # Максимальное значение рассматриваемого интервала

    while min_number <= max_number:
        count += 1
        predict_number = (max_number + min_number) // 2  # предполагаемое число
        if predict_number > number: # если предполагаемое число больше
            max_number = predict_number - 1
        elif predict_number < number: # если предполагаемое число меньше
            min_number = predict_number + 1
        else:
            return count
    return -1

def score_game(cycle_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        cycle_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(cycle_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(cycle_predict)
