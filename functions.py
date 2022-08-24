import datetime

"""FIRST EXERCISE"""
start = int(input('enter the start of calculation: '))
finish = int(input('enter the start of calculation: '))


def counter(start: int, finish: int) -> int:
    list = [start, finish]
    list = sorted(list)
    result = sum(range(list[0], list[1] + 1))
    return result


print(counter(start, finish))

"""SECOND EXERCISE"""


def time_convert(sec: int):
    result = datetime.timedelta(seconds=sec)
    return result


print(time_convert(360000))

"""THIRD EXERCISE"""
list = [1, 3, 4, 6, 7, 8, 12, 2]

def for_counter(list: list) -> int or float:
    sum = 0
    for i in list:
        sum += i
    return sum

print(for_counter(list))

list = [1, 3, 4, 6, 7, 8, 12, 2]

def while_counter(list: list) -> int or float:
    sum = 0
    while len(list) != 0:
        sum += list.pop()
    return sum

print(while_counter(list))

list = [1, 3, 4, 6, 7, 8, 12, 2]

def recurs_counter(list: list) -> int or float:
    if list == []:
        return 0
    else:
        sum = recurs_counter(list[1:])
        sum = sum + list[0]
        return sum

print(recurs_counter(list))


"""FOURTH EXERCISE"""