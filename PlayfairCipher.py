from collections import deque
import numpy as np

matrix_size = 5 ** 2
input_string = ''


def find_repeater(string):
    my_list = []
    my_list.append(string[0])
    for i in range(1, len(string)):
        if string[i] in my_list:
            return False
        else:
            my_list.append(string[i])
    return True


input_key = input('Enter mono-alphabetical key:')
isMonoAlphabetical = find_repeater(input_key)
print(isMonoAlphabetical)


def extra_padding(input, m_size):
    garbage = m_size - len(input) % m_size
    input = input + '$' * garbage
    print(input)
    return input


def add_padding(key):
    abcd_list = list(map(chr, range(97, 123)))
    print(abcd_list)
    for a in abcd_list:
        if a in input_key:
            continue
        elif a == 'j':
            continue
        else:
            key += a
    print(key)
    return key


padded_key = add_padding(input_key)

input_string = extra_padding(padded_key, matrix_size)
matrix = []
start = 0

for i in range(start, 5, matrix_size):
    for n in range(5):
        matrix.append(list(input_string[start:start + 5]))
        start = start + 5
    # matrix.append(temp)

print(matrix)


# Finding consective repeting chars


def consective_char(string):
    string_list = deque(list(string))
    for j in range(0, len(string)):
        if j == len(string) - 1:
            break
        elif string_list[j] == string_list[j + 1]:
            # Inserting x
            string_list.insert(j + 1, 'x')
    return string_list


# Swap the values using coordinates/ find intersections


def swap_first_values(first_value, second_value):
    v1 = first_value[0]
    v2 = first_value[1]
    v3 = second_value[0]
    v4 = second_value[1]
    print('v1', v1)
    print('v4', v4)
    first_char = matrix[[4], [4]]
    print('first_char:', first_char)


def swap_second_values(first_value, second_value):
    v1 = first_value[0]
    v2 = first_value[1]
    v3 = second_value[0]
    v4 = second_value[1]
    print('v3', v3)
    print('v2', v2)
    second_char = matrix[[0], [1]]
    print('second_char: ',second_char)


# Find the index of op code
def find_index(first, second):
    first_index = [(index, row.index(first)) for index, row in enumerate(matrix) if first in row]
    second_index = [(index, row.index(second)) for index, row in enumerate(matrix) if second in row]
    print(np.asarray(first_index[0]), np.asarray(second_index[0]))
    swap_first_values(np.asarray(first_index[0]), np.asarray(second_index[0]))
    swap_second_values(np.asarray(first_index[0]), np.asarray(second_index[0]))


def intersection(string):
    string_s = string.replace(' ', '')
    for (op, code) in zip(string_s[0::2], string_s[1::2]):
        print('op: ', op, 'code', code)
        find_index(op, code)


# Taking plain text as input and encryptinh it using table

plain_text = input('Enter your plain text: ')
input_x = consective_char(plain_text)
# Typecasting deque to string
input_x = ''.join(input_x)
print(input_x)
intersection(input_x)
