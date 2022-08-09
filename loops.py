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
        print("\n\nOkay, Let's do it again. Just hit the keyboard by your head! ")

    value_input = input("Let's do it! : ")

    if value_input.capitalize().strip() == 'Exit':
        print(f'Ok, see u later. We done {text_counter} iterations')
        break

    space_indexes = []  # put here spaces indexes for their counting and output

    letters_isup = []

    vowels_en_input = []  # for saving original input register
    vowels_en_uniq = []  # for counting and listing unique vowels

    vowels_ru_input = []
    vowels_ru_uniq = []

    for i in range(len(value_input)):
        if value_input[i] == " ":
            space_indexes.append(str(i))
        if (value_input[i]).isupper():
            letters_isup.append(value_input[i])

        if value_input[i].upper() in vowels_ru:
            vowels_ru_input.append(value_input[i])
            vowels_ru_uniq.append(value_input[i].upper())
        if value_input[i].upper() in vowels_en:
            vowels_en_input.append(value_input[i])
            vowels_en_uniq.append(value_input[i].upper())
        try:
            if (value_input[i] + value_input[i + 1] + value_input[i + 2]).isdigit() or \
                    (value_input[i - 1] + value_input[i - 2] + value_input[i - 3]).isdigit():
                print("something wrong. "
                      "Maybe you input three digits one by one?")
                counter += 1
                break
        except:
            pass
    if counter == 0:
        print(f' Your input Value is "{value_input}". \n(nice punch, LOL)\n'
              f' if we make up register, it will looks like: \n {value_input.upper()} \n'
              f' There are {len(letters_isup)} is upper')
        if len(letters_isup) > 0:
            print(f" Up register letters in your string is: {', '.join(letters_isup)} ")
        print(f' there are {len(space_indexes)} spaces in your text ')
        if len(space_indexes) > 0:
            print(f" indexes of spaces in your string: {', '.join(space_indexes)}")
        print(f' There are {len(vowels_ru_input)} RU vowels and {len(vowels_en_input)} EN vowels')
        if len(vowels_ru_input) > 0:
            print(f" Input RU vowels is: '{''.join(vowels_ru_input) }' \n"
                  f" There are {len(set(vowels_ru_uniq))}  unique RU vowels")
        if len(vowels_en_input) > 0:
            print(f" Input EN vowels is: {''.join(vowels_en_input) } \n"
                  f" There are {len(set(vowels_en_uniq))}  unique EN vowels")
        text_counter += 1
