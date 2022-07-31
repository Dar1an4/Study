# Practice advanced
name = input('Enter your name, please: ')
name = name.title()
name = name.strip()
print(f'Hello, dear {name}\n'
      f'Length of your name is {len(name)} letters \n'
      f'Reversed version of your name looks like {name[::-1]}')
