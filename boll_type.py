# 3 ! 5

print(3 != 5)

# 5 _ 5

first_answer, second_answer, third_answer = 5 == 5, 5 <= 5, 5 >= 5
fourth_answer, fifth_answer, sixth_answer = 5 and 5, 5 or 5, 5 is 5
nineth_answer = not 5 != 5
print(f'{first_answer = }, {second_answer = }, {third_answer = }, '
      f'{fourth_answer = }, {fifth_answer = }, {sixth_answer = }'
      f'{nineth_answer = })

# True _ True _ False and or/and/not

answer_first = (True and True) or False
print(f'{answer_first = }')

answer_sec = (not True and not True) or not False
print(f'{answer_sec = }')

answer_third = not True or (True and not False)
print(f'{answer_third = }')

answer_fourth = True or (True and not False)
print(f'{answer_fourth = }')

answer_fifth = True or True or False
print(f'{answer_fifth = }')

answer_sixth = not True or not True or not False
print(f'{answer_sixth = }')

answer_seventh = True or not True or False
print(f'{answer_seventh = }')

answer_eight = True and True and not False
print(f'{answer_eight = }')

# logic None and 7

num_not = None
num = 7

print(num == num_not)
print(num != num_not)

print(num is num_not)
print(num is not num_not)

# logic None and 10 - 1

num_not = ''
some_num = 10 - 1

print(num_not == some_num)
print(num_not != some_num)

print(num_not is some_num)
print(num_not is not some_num)