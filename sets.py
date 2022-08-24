first_tuple = set(input("Enter values: "))
second_tuple = set(input("Enter values again: "))

letters_from_both_sets = set()
digits_set1 = set()
digits_set2 = set()

for value in first_tuple:
    if value.isalpha():
        letters_from_both_sets.add(value)
    if value.isdigit():
        digits_set1.add(value)

for value in second_tuple:
    if value.isalpha():
        letters_from_both_sets.add(value)
    if value.isdigit():
        digits_set2.add(value)

print(f'{letters_from_both_sets = } ')
print(f'{digits_set1.symmetric_difference(digits_set2) = }')

test_tuple1 = {2, 15, 'al', 32, 5, 3, 2, 1, 0, 'ass', 'arr', 145}
test_tuple2 = {'ass', 15, 1231, 'asaa', 432, 0, 223, 123, 432, 24}
test_tuple3 = {0, 'ass', 2, 4, 'sym', 11, 12, 15, 113, 5, 0, 43}

print(test_tuple1 ^ test_tuple2 ^ test_tuple3)
print(test_tuple1 & test_tuple2 & test_tuple3)
print(test_tuple1 | test_tuple2 | test_tuple3)
print(test_tuple1 - test_tuple2 - test_tuple3)
