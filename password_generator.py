import random

alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
sym = '''~!@#$%^&*(_)+-=[]{|};':"<>?,./'''

length = int(input("Length of the password: "))
include_alpha = input("Include Letters(Y/N): ").upper() in ['Y', 'YES', 'TRUE']
include_digits = input("Include Numbers(Y/N): ").upper() in ['Y', 'YES', 'TRUE']
include_sym = input("Include Symbols(Y/N): ").upper() in ['Y', 'YES', 'TRUE']

charset = ''
if include_alpha:
    charset += alpha
if include_digits:
    charset += digits
if include_sym:
    charset += sym

if not charset:
    print("No characters selected. Please include at least one character type.")
else:
    password = ''.join(random.choices(charset, k=length))
    print("Generated password:", password)
