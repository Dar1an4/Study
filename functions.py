import time

"""FIRST EXERCISE"""
start = int(input('enter the start of calculation: '))
finish = int(input('enter the start of calculation: '))

def counter(start: int, finish: int) -> int:
    list = [start, finish]
    list = sorted(list)
    result = sum(range(list[0], list[1] + 1))
    return result

print(f'{counter(start, finish) = }')

"""SECOND EXERCISE"""

def time_convert(sec: int) -> str:
    if sec < 86400:
        res = time.gmtime(sec)
        result = str(time.strftime("%H:%M:%S", res))
        return result
    else:
        days = sec // 86400
        left_seconds = sec - (days * 86400)
        res = time.gmtime(left_seconds)
        result = f'{str(days)}:{str(time.strftime("%H:%M:%S", res))}'
        return f'days:hours:minutes:seconds {result}'

print(f'{time_convert(86401) = }')

"""THIRD EXERCISE"""

list_inc = [1, 3, 4, 6, 7, 8, 12, 2]

def for_counter(incoming_list: list) -> int or float:
    sum = 0
    for i in incoming_list:
        sum += i
    return sum

print(f'{for_counter(list_inc) = }')

list_inc = [1, 3, 4, 6, 7, 8, 12, 2]

def while_counter(incoming_list: list) -> int or float:
    output_list = incoming_list.copy()
    sum = 0
    while len(output_list) != 0:
        sum += output_list.pop()
    return sum

print(f'{while_counter(list_inc) = }')

list_inc = [1, 3, 4, 6, 7, 8, 12, 2]

def recurs_counter(incoming_list: list) -> int or float:
    if incoming_list == []:
        return 0
    else:
        sum = recurs_counter(incoming_list[1:])
        sum = sum + incoming_list[0]
        return sum

print(f'{recurs_counter(list_inc) = }')


"""FOURTH EXERCISE"""

