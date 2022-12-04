with open('input.txt', 'r') as f:
    temp = []
    for line in f:
        temp.append(line)

temp = [l.strip('\n') for l in temp]

choice_score = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

result_score = {
    'A X': 3,
    'B Y': 3,
    'C Z': 3,
    'A Y': 6,
    'A Z': 0,
    'B X': 0,
    'B Z': 6,
    'C X': 6,
    'C Y': 0

}


def my_func(x: list, y: dict) -> int:

    score = 0

    for _ in x:
        for i in range(len(y)):
            if _[2] == list(y.keys())[i]:
                score += y[list(y.keys())[i]]

    return score


def your_func(x: list, y: dict) -> int:

    score = 0

    for _ in x:
        for i in range(len(y)):
            if _ == list(y.keys())[i]:
                score += y[list(y.keys())[i]]

    return score


matching = {
    'A X': 'A Z',
    'A Y': 'A X',
    'A Z': 'A Y',
    'B X': 'B X',
    'B Y': 'B Y',
    'B Z': 'B Z',
    'C X': 'C Y',
    'C Y': 'C Z',
    'C Z': 'C X'
}


def new_mapping(x: list) -> list:
    new_list = [matching[k] for k in x]
    return new_list


print(
    f'The result of the first part is: {my_func(temp, choice_score) + your_func(temp, result_score)}')

print(
    f'The result of the first part is: {my_func(new_mapping(temp), choice_score) + your_func(new_mapping(temp), result_score)}')
