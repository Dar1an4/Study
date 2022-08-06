name = input('Enter your name, please \n'
             'or if u wanna stop this - input "Exit" : ')
name = name.title().strip()

text_counter = 0
counter = 1 if name == 'Exit' else 0

vowels_en = ['A', 'E', 'U', 'I', 'O', 'Y']
vowels_ru = ['А', 'У', 'О', 'Ы', 'И', 'Э', 'Я', 'Ю', 'Ё', 'Е']

while counter == 0:
    if text_counter == 0:
        print(f' Hello, dear {name}\n'
              f" Let's do some magic \n"
              f' You just need enter any what you want \n'
              f' im not kidding. Just punch the keyboard by your head\n')
    else:
        print("\n\nOkey, Let's do it again. Just hit the keyboard by your head! ")

    value_input = input("Let's do it! : ")

    if value_input.capitalize().strip() == 'Exit':
        print('Ok, see u later')
        break

    space_counter = 0
    space_indexes = []

    vowels_en_input = []
    vowels_en_uniq = []

    vowels_ru_input = []
    vowels_ru_uniq = []

    for i in range(len(value_input)):
        if value_input[i] == " ":
            space_counter += 1
            space_indexes.append(str(i))

        if value_input[i].upper() in vowels_ru:
            vowels_ru_input.append(value_input[i])
            vowels_ru_uniq.append(value_input[i].upper())
        if value_input[i].upper() in vowels_en:
            vowels_en_input.append(value_input[i])
            vowels_en_uniq.append(value_input[i].upper())

        i -= 1  # fix problem without of len
        if (value_input[i-1] + value_input[i] + value_input[i+1]).isdigit():
            print("something wrong. "
                  "Maybe you input three digits one by one?")
            counter += 1
            break

    if counter == 0:
        print(f' Your input Value is "{value_input}". \n(nice punch, LOL)\n'
              f' if we make up register, it will looks like: \n {value_input.upper()} \n'
              f' there are {space_counter} spaces on your text ')
        if space_counter > 0:
            print(f" indexes of spaces in your string - {', '.join(space_indexes)}")
        print(f' There are {len(vowels_ru_input)} RU vowels and {len(vowels_en_input)} EN vowels')
        if len(vowels_ru_input) > 0:
            print(f" Input RU vowels is '{''.join(vowels_ru_input) }' \n"
                  f" There are {len(set(vowels_ru_uniq))}  unique RU voweles")
        if len(vowels_en_input) > 0:
            print(f" Input EN vowels is '{''.join(vowels_en_input) }' \n"
                  f" There are {len(set(vowels_en_uniq))}  unique EN voweles")
        text_counter += 1