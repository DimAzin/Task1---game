"""The Game - how is the number&
Computer games with themself.
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Rundom find number

    Args:
        number (int, optional): Secret number. Defaults to 1.

    Returns:
        int: Count of attempt 
    """
    count = 0
    min_range = 1 # min range of predict attept
    max_range = 101 # max range of predict attepmt

    while True:
        count += 1
        
        predict_number = np.random.randint(min_range, max_range)  # attempt's number
        if number == predict_number:
            break  # BINGO!
        elif number > predict_number:
            min_range = predict_number
        else:
            max_range = predict_number
        
    return count


def score_game(random_predict) -> int:
    """ЗHow much attempts are? 1000 rounds.

    Args:
        random_predict ([type]): predict function

    Returns:
        int: mean count of attempts
    """
    count_ls = [] #list of attempt's results
    
    random_array = np.random.randint(1, 101, size=(1000))  # list of numbers

    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
