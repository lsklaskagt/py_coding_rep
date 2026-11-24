# Day 12/30
# L.1

import math
import string
import random

def random_user_id():
    res = string.ascii_letters + string.digits
    str = ''

    for num in range(6):
        str += random.choice(res)
    print(str)

def user_id_gen_by_user():
    len = int(input("Введите длину: "))
    cnt = int(input("Введите количество: "))
    for count in range(cnt):
        res = string.ascii_letters + string.digits
        str = ''

        for num in range(len):
            str += random.choice(res)
        print(str)

def rgb_colour_gen():
    new_tuple = ()
    for num in range(3):
        number = random.randint(0, 255)
        new_tuple += (number,)
    print('rgb',new_tuple)

def list_of_hexa_colours(number):
    for num in range(number):
        res = 'ABCDEF' + string.digits
        str = ''

        for num in range(6):
            str += random.choice(res)
        print('#' + str)

def list_of_rgb_colours(number):
    new_list = []
    for num in range(number):
        new_tuple = ()
        for num in range(3):
            number = random.randint(0, 255)
            new_tuple += (number,)
        new_list.append(f'rgb{new_tuple}')
    print(new_list)

def generate_colours(parameter_type, count):
    if parameter_type == 'hexa':
        list_of_hexa_colours(count)
    elif parameter_type == 'rgb':
        list_of_rgb_colours(count)

def shuffle_list(list):
    new_list = []

    for num in range(len(list)):
        a = random.choice(list)
        new_list.append(a)
        list.remove(a)
    print(new_list)

def random_numbers():
    new_set = {}
    res = string.digits
    num = random.choice(res)
    new_set = {f"{num}"}

    while len(new_set) < 7:
        choice = random.choice(res)
        new_set.update({f"{choice}"})
    print(new_set)

random_user_id()
user_id_gen_by_user()
rgb_colour_gen()
list_of_hexa_colours(5)
list_of_rgb_colours(4)
generate_colours('rgb', 2)
shuffle_list(['a', 'b', 'c', 1, 2, 3, 4])
random_numbers()