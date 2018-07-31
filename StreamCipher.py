key = 3

encr_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8,
             'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16,
             'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}

encr_list = sorted(list(encr_dict.keys()))


def encrypt(ch):
    return (encr_dict[ch] + key) % 26


def decrypt(ch):
    return ((encr_dict[ch] + 26) - key) % 26


def make_cipher():
    encrypted_text = ""
    message = input('Enter your message: ')
    message = message.lower()
    print('encrypting...')
    for m in message:
        if m in encr_dict:
            encrypted_text += encr_list[encrypt(m)]
        else:
            encrypted_text += m
    print(encrypted_text)


def decrypt_cipher():
    decrypted_text = ""
    message = input('Enter your cipher text: ')
    message = message.lower()
    print('decrypting...')
    for d in message:
        if d in encr_dict:
            decrypted_text += encr_list[decrypt(d)]
        else:
            decrypted_text += d
    print(decrypted_text)


choice = input("Type e for encryption or d for decryption: ")
if choice is 'e':
    make_cipher()
elif choice is 'd':
    decrypt_cipher()
else:
    print('Check your input!')
