import string

ascii_lowstring = string.ascii_lowercase
# keys = {key: ascii_lowstring[key] for key in range(0, 26)}
string = 'hello'
password = 4


dict = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n',
        14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}

print(f"{dict = }")

alphabet2 = {}
for key, value in dict.items():
    alphabet2[key+password] = value
print(f"{alphabet2 = }")

inv_keys_alphabet = {}
for key, value in alphabet2.items():
    inv_keys_alphabet[value] = key
print(f"{inv_keys_alphabet= }")

keys = list(inv_keys_alphabet.keys())
values = list(inv_keys_alphabet.values())
# print(keys)
# print(values)

secret_string = []
keys = []

for keys in string:
    secret_string.append(alphabet2.get(inv_keys_alphabet.get(keys)+password))
    print(f"{keys = }")
    print(f"{alphabet2.get(inv_keys_alphabet.get(keys)+password) = }")
    print(f"{inv_keys_alphabet.get(keys)+password = }")
print(secret_string)