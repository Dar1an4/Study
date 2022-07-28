name = input('Enter your name, please: ')
number = float(input(f'Hello dear {name.title()}, enter any float value, please: '))
print(f'Your number is {number}',
      f'\nAnd integer value of yor number is {int(number)}',
      f'\nThe fourth power of yor number is {int(number)**4}',
      f'\nThe second root of your number is {int(number)**0.5}',
      f'\nRemainder of division by two of your number is {int(number)%2}')