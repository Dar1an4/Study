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
        print("\n\nOkey, Let's do it again. Just hit the keyboard by yoar head! ")

    value_input = input("Let's do it! : ")

    if value_input.capitalize().strip() == 'Exit':
        print('Ok, see u later')
        break

    space_counter = 0
    space_indexes = []

    vowels_en_counter = 0
    vowels_en_input = []

    vowels_ru_counter = 0
    vowels_ru_input = []

    for i in range(len(value_input)):
        if value_input[i] == " ":
            space_counter += 1
            space_indexes.append(i)

        if value_input[i].upper() in vowels_ru:
            vowels_ru_counter += 1
            vowels_ru_input.append(value_input[i].upper())
        if value_input[i].upper() in vowels_en:
            vowels_en_counter += 1
            vowels_en_input.append(value_input[i].upper())
        i -= 1
        if (value_input[i-1] + value_input[i] +value_input[i+1]).isdigit():
            print("something wrong. "
                  "Maybe you input three digits one by one?")
            counter += 1
            break

    if counter == 0:
        print(f' Your input Value is {value_input}. \n(nice punch, LOL)\n'
              f' if we up register, it will looks like: \n {value_input.upper()} \n'
              f' there are {space_counter} spaces on your text ')
        if space_counter > 0:
            print(f' indexes of spaces in your string - {space_indexes}')
        print(f' There are {vowels_ru_counter} RU vowels and {vowels_en_counter} EN vowels' )
        if vowels_ru_counter > 0:
            print(f' Input RU vowels is {vowels_ru_input}')
        if vowels_en_counter > 0:
            print(f' Input EN vowels is {vowels_en_input}')
        text_counter += 1

