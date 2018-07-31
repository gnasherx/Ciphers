import numpy as np


def add_padding(input_string, matrix_size):
    garbage = matrix_size - len(input_string) % matrix_size
    input_string = input_string + '$' * garbage
    print(input_string)
    return input_string


def blockcipher(input_string):
    k = int(input("Enter key size: "))
    matrix_size = k ** 2

    input_string = add_padding(input_string, matrix_size)
    matrix = []
    start = 0

    for i in range(start, len(input_string), matrix_size):
        temp = []
        for n in range(k):
            temp.append(list(input_string[start:start + k]))
            start = start + k
        matrix.append(temp)

    test = []

    for i in range(len(matrix)):
        test.append(np.transpose(matrix[i]))
    outputtext = ""
    for j in range(len(matrix)):
        for i in test[j]:
            outputtext = outputtext + "".join(list(i))

    return outputtext


select_type = input("Press e for Encryption and d for Decryption: ")

if select_type is "e":

    text = input("Enter text to Encrypt: ")

    outputtext = blockcipher(text)
    print("Before Encryption: " + text + "\nAfter Encryption: " + outputtext)

elif select_type is "d":

    text = input("Enter text to Decrypt: ")

    outputtext = blockcipher(text).replace('$', '')
    print("Before Decryption: " + text + "\nAfter Decryption: " + outputtext)

else:

    print("Select valid type")
