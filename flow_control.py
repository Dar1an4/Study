name = input('Enter your name, please: ')
name = name.title()
name = name.strip()
print(f'Hello, dear {name}\n'
      f" Let's try to show you Pythoculator \n"
      f' You just need enter any Value one by one below, and finally, '
      f' what whe need to do ? ("+","-","/","*", "n ** n1")')

while 1:
    value_input_first = input('Enter first value: ')
    value_input_second = input('Enter second value: ')
    try:
        if '.' in value_input_first:
            value_first = float(value_input_first)
        else:
            value_first = int(value_input_first)
        if '.' in value_input_second:
            value_second = float(value_input_second)
            break
        else:
            value_second = int(value_input_second)
            break
    except:
        print('Hey Bro, wtf, what has been entered? we need only digits')

values = [value_input_first, value_input_second]
values.sort()       #  sort for comparison
                                                                    # use it in answer for comparison between values
comparison = '<' if float(values[0]) < float(values[1]) else '='    # use float because if type is different - comparison will be
                                                                    # incorrect, when values ==
while 1:
    try:
        to_do = input('finally, what whe need to do with them: ')
        if to_do == '+':
              result = value_first + value_second
              break
        elif to_do == '-':
              result = value_first - value_second
              break
        elif to_do == '/':
              result = value_first / value_second
              result = float(result) if '.' in value_input_first or '.' in value_input_second else int(result)
              break
        elif to_do == '*':
              result = value_first * value_second
              break
        elif to_do == '**':
              result = value_first ** value_second
              break
        else:
            print(f'{name}, bro, wtf again? We already had a deal! you need use only +, -, /, *, ** "\n'
                  f'Dont forget! your values is {value_first} and {value_second}!\n'
                  f'Just put between them something what we talking about!')
    except Exception as error:
        print(f"You make dirty... :{ error }")

print(f'\n \nand the answer is..... : {result} (how unexpected) \n'
      f'And just for reference: \n'
      f'Type of your answer is {type(result)} \n'
      f'And {values[0]} {comparison} {values[1]} \n'
      f'Type of your entered first value is {type(value_first)}, and type of second is {type(value_second)}\n'
      f'the order of answer is {len(str(int(result))) - 1}')  # How many orders does the operand have? (скільки порядків)


print(f'\n\n Thx for using that! waiting for you again!')
