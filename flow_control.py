name = input('Enter your name, please: ')
name = name.title()
name = name.strip()
print(f'Hello, dear {name}\n'
      f" Let's try to show you Pythoculator \n"
      f' You just need enter any Value one by one below, and finally, '
      f' what whe need to do ? ("+","-","/","*", "n ** n1")')
values = []         #  use in later, put here aur values for sorting for comparison
counter = 0
while counter == 0:
    value_input_first = input('Enter first value: ')
    value_input_second = input('Enter second value: ')
    try:
        if '.' in value_input_first or '.' in value_input_second:
            value_first = float(value_input_first)
            value_second = float(value_input_second)
            counter += 1
        else:
            value_first = int(value_input_first)
            value_second = int(value_input_second)
            counter += 1
    except:
        print('Hey Bro, wtf, what has been entered? we need only digits')

value_input_first_type = 'float' if '.' in value_input_first else 'int'
value_input_second_type = 'float' if '.' in value_input_second else 'int'

values.append(value_input_first)
values.append(value_input_second)
values.sort()       #  sort for comparison

comparison = '<' if values[0] < values[1] else '='      # use it in answer for comparison between values

counter = 0     #  refresh our iteration counter
while counter == 0:
    to_do = input('finally, what whe need to do with them: ')
    if to_do == '+':
          result = value_first + value_second
          print(f'\n \nand the answer is..... : {result} (how unexpected) \n'
                f'And just for reference: \n'
                f'Type of your answer is {type(result)} \n'
                f'And {values[0]} {comparison} {values[1]} \n'
                f'Type of your first value is {value_input_first_type}, and type of second is {value_input_second_type}')
          counter += 1
    elif to_do == '-':
          result = value_first - value_second
          print(f'\n \nand the answer is..... : {result} (how unexpected) \n'
                f'And just for reference: \n'
                f'Type of your answer is {type(result)} \n'
                f'And {values[0]} {comparison} {values[1]} \n'
                f'Type of your first value is {value_input_first_type}, and type of second is {value_input_second_type}')
          counter += 1
    elif to_do == '/':
          result = value_first / value_second
          print(f'\n \nand the answer is..... : {result} (how unexpected) \n'
                f'And just for reference: \n'
                f'Type of your answer is {type(result)} \n'
                f'And {values[0]} {comparison} {values[1]} \n'
                f'Type of your first value is {value_input_first_type}, and type of second is {value_input_second_type}')
          counter += 1
    elif to_do == '*':
          result = value_first * value_second
          print(f'\n \nand the answer is..... : {result} (how unexpected) \n'
                f'And just for reference: \n'
                f'Type of your answer is {type(result)} \n'
                f'And {values[0]} {comparison} {values[1]} \n'
                f'Type of your first value is {value_input_first_type}, and type of second is {value_input_second_type}')
          counter += 1
    elif to_do == '**':
          result = value_first ** value_second
          print(f'\n \nand the answer is..... : {result} (how unexpected) \n'
                f'And just for reference: \n'
                f'Type of your answer is {type(result)} \n'
                f'And {values[0]} {comparison} {values[1]} \n'
                f'Type of your first value is {value_input_first_type}, and type of second is {value_input_second_type}')
          counter += 1
    else:
        print(f'{name}, bro, wtf again? We already had a deal! you need use only +, -, /, *, ** "\n'
              f'Dont forget! your values is {value_first} and {value_second}!\n'
              f'Just put between them something what we talking about!')

print(f'\n\n Thx for using that! waiting for you again!')
