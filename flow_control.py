name = input('Enter your name, please: ')
name = name.title().strip()
print(f'Hello, dear {name}\n'
      f" Let's try to show you Pythoculator \n"
      f' You just need enter any Value one by one below, and finally, '
      f' what whe need to do ? ("+","-","/","*", "n ** n1")')
while 1:
    while 1:
        value_input_first = input('Enter first value: ')
        if value_input_first.title().strip() == 'Exit':
            print('Ok, if u decide it.... So, by, see you later!')
            break
        value_input_second = input('Enter second value: ')
        if value_input_second.title().strip() == 'Exit':
            print('Ok, if u decide it.... So, by, see you later!')
            break
        try:
            value_first = float(value_input_first) if '.' in value_input_first else int(value_input_first)
            value_second = float(value_input_second) if '.' in value_input_second else int(value_input_second)
            break
        except:
            print('Hey Bro, wtf, what has been entered? we need only digits')

    try:
        values = [value_input_first, value_input_second]
        values.sort()       #  sort for comparison
        comparison = '<' if float(values[0]) < float(values[1]) else '='
    except:
        break

    to_dos = ['+', '-', '/', '*', '**']
    while 1:
        try:
            to_do = input('finally, what whe need to do with them: ')
            if to_do == to_dos[0]:
                result = value_first + value_second
                break
            elif to_do == to_dos[1]:
                result = value_first - value_second
                break
            elif to_do == to_dos[2]:
                result = value_first / value_second
                result = int(result) if value_first % value_second == 0 else float(result)
                break
            elif to_do == to_dos[3]:
                result = value_first * value_second
                break
            elif to_do == to_dos[4]:
                result = value_first ** value_second
                break
            elif to_do not in to_dos:
                if to_do.title().strip() == 'Exit':
                    break
                else:
                    print(f'{name}, bro, wtf again? We already had a deal! you need use only +, -, /, *, ** "\n'
                          f'Dont forget! your values is {value_first} and {value_second}!\n'
                          f'Just put between them something what we talking about!')
        except Exception as error:
            print(f"You make dirty... :{ error }")
    try:
        print(f'\n \nand the answer is..... : {result} (how unexpected) \n'
              f'And just for reference: \n'
              f'Type of your answer is {type(result)} \n'
              f'And {values[0]} {comparison} {values[1]} \n'
              f'Type of your entered first value is {type(value_first)}, and type of second is {type(value_second)}\n'
              f'the order of answer is {len(str(int(result))) - 1} \n')  # How many orders does the operand have?(скільки порядків)
    except:
        print('Ok, if u decide it.... So, by, see you later!')
        break