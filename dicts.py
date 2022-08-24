ascii = {key: chr(key) for key in range(0, 128)}
print(ascii)

string = input('Enter your string for coding: ')
password = int(input('Enter your code: '))
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

alphabet_key = {
    key: alphabet[key] for key in range(26)
}

inv_keys_alphabet = {}
for key, value in alphabet_key.items():
    inv_keys_alphabet[value] = key

secret_string = []
keys = []

for key in string:
    keys.append(inv_keys_alphabet.get(key.upper()))
for key in keys:
    secret_string.append(alphabet_key.get(key+password))

print(''.join(secret_string))

string = input('Enter your string for decoding: ')
password = int(input('Enter your code: '))

secret_string2 = []
keys2 = []

for key in string:
    keys2.append(inv_keys_alphabet.get(key.upper()))
for values in keys2:
    secret_string2.append(alphabet_key.get(values-password))

print(''.join(secret_string2).capitalize())
