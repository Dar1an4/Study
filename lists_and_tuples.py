any_string = input('Enter a string: ')
some_list = any_string.split(' ')
print(','.join(some_list[2::3]))  # printing every third word

input_list = [1, 2.1, "f", "2", 3, "1", 18, "df"]
output_list = [1, 2.1, -1, '6', 9, '3', 18, -1]

gen_list = [el if type(el) == float else
             el if (type(el) == int and el % 2 == 0) else
             el**2 if (type(el) == int and el % 2 != 0) else
             (str(int(el)*3)) if (type(el) == str and el.isdigit()) else -1 for el in input_list]

print(gen_list)