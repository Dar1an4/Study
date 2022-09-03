import string


ascii = {key: chr(key) for key in range(0, 128)}
print(ascii)
################################################################

alphabet_key = {
    letter: index
    for index, letter in enumerate(string.ascii_lowercase)}
print(alphabet_key)

user_str = input('Enter your string for coding: ')
password = int(input("Type positive integer value for password: ")) % len(alphabet_key)

alphabet_secure = {
    # ternary operator for make loop inside the alphabet
    index - password + (len(alphabet_key) if password > index else 0): letter
    for letter, index in alphabet_key.items()
    }
print(alphabet_secure)

secret_string = "".join([alphabet_secure[alphabet_key[letter]] for letter in user_str])

print(secret_string)

user_str = input('Enter your string for decoding: ')
password = int(input("Type positive integer value for password decoding: ")) % len(alphabet_key)

alphabet_secure = {
    index + password - (len(alphabet_key) if password > index else 0): letter
    for letter, index in alphabet_key.items()
    }

decoding_string = "".join([alphabet_secure[alphabet_key[letter]] for letter in user_str])
print(decoding_string)
