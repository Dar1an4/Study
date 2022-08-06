name = input('Enter your name, please \n'
             'or if u wanna stop this - input "Exit" : ')
name = name.title().strip()
to_dos = ['+', '-', '/', '*', '**']

text_counter = 0
counter = 1 if name == 'Exit' else 0
while counter == 0:
    if text_counter == 0:
        print(f' Hello, dear {name}\n'
              f" Let's try to show you Pythoculator \n"
              f' You just need enter any Value one by one below, and finally, \n'
              f' what whe need to do ? {to_dos}\n'
              f' and if you want to exit - just input "Exit" instead any value or operation')
    else:
        print("Let's go again.\n"
              'if you want to exit - just input "Exit".\n'
              'For continue, just input some values and what we need to do: \n')
    while counter == 0:
        value_input_first = input('Enter first value: ')
        if value_input_first.title().strip() == 'Exit':
            counter += 1
            break
        value_input_second = input('Enter second value: ')
        if value_input_second.title().strip() == 'Exit':
            counter += 1
            break
        try:
            values = [value_input_first, value_input_second]
            values.sort()  # sort for comparison
            comparison = '<' if float(values[0]) < float(values[1]) else '='  # Use float, because comparison didnt work if values ==
            value_first = float(value_input_first) if '.' in value_input_first else int(value_input_first)
            value_second = float(value_input_second) if '.' in value_input_second else int(value_input_second)
            break
        except ValueError:
          print('Hey Bro, wtf, what has been entered? we need only digits')

    while counter == 0:
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
                    print(f'{name}, bro, wtf again? We already had a deal! you need use only {to_dos}'
                          f'Dont forget! your values is {value_first} and {value_second}!\n'
                          f'Just put between them something what we talking about!')
        except Exception as error:
            print(f"You make dirty... :{ error }")
    try:
        print(f'\nYour an arithmetical example is {value_first} {to_do} {value_second}\n'
              f'and the answer is..... : {result} (how unexpected) \n'
              f'And just for reference: \n'
              f'Type of your answer is {type(result)} \n'
              f'And {values[0]} {comparison} {values[1]} \n'
              f'Type of your entered first value is {type(value_first)}, and type of second is {type(value_second)}\n'
              f'the order of answer is {len(str(int(result))) - 1} \n')  # How many orders does the operand have?(скільки порядків)
        text_counter += 1
    except:
        print('Ok, if u decide it.... So, by, see you later!')
        break
