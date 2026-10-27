# Day 11/30
# L.1
pi = 3.14159

def add_two_numbers(first_number, second_number):
    return first_number + second_number

def area_of_circle(radius):
    return pi * radius ** 2

def add_all_nums(*args):
    sum = 0

    for num in args:
        if type(num) in (int, float):
            sum += num
    return sum

def convert_celsius_to_fahrenheit(temp):
    return temp * 1.8 + 32

def check_season(month):
    if month == 'April' or month == 'March' or month == 'May':
        return 'Spring'
    elif month == 'June' or month == 'July' or month == 'August':
        return 'Summer'
    elif month == 'September' or month == 'October' or month == 'November':
        return 'Fall'
    elif month == 'December' or month == 'January' or month == 'February':
        return 'Winter'
    else:
        print("ERROR")

def solve_quadratic_eqn(a, b, c):
    if b ** 2 - 4 * a * c >= 0:
        first_root = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
        second_root = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
        if first_root == second_root:
            return first_root
        else:
            return first_root, second_root
    else:
        return 'No real solution'

def print_list(list):
    for item in list:
        print(item)

def reverse_list(list):
    new_list = []
    for item in list:
        new_list.insert(0, item)
    print(new_list)

def capitalize_list_items(list):
    new_list = []
    for item in list:
        new_list.append(item.capitalize())
    print(new_list)

def add_item(list, item):
    list.append(item)
    print(list)

def remove_item(list, item):
    list.remove(item)
    print(list)

def sum_of_numbers(number):
    sum = 0
    for num in range(0, number + 1):
        sum += num
    print(sum)

def sum_of_odds(number):
    sum = 0
    for num in range(0, number + 1):
        if num % 2 != 0:
            sum += num
    print(sum)

def sum_of_evens(number):
    sum = 0
    for num in range(0, number + 1, 2):
        sum += num
    print(sum)

print(add_two_numbers(100, -100))
print(area_of_circle(10))
print(add_all_nums(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(f"{convert_celsius_to_fahrenheit(12.1):.5f}")
print(check_season('August'))
print(solve_quadratic_eqn(1, -6, 9))
print_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
reverse_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
capitalize_list_items(['aboba', 'amogus'])
add_item([], 'abob')
remove_item([1, 2, 3], 3)
sum_of_numbers(10)
sum_of_odds(100)
sum_of_evens(100)

# L.2

def evens_and_odds(number):
    if number <= 0:
        return
    else:
        odd_sum = 0
        even_sum = 0
        for num in range(1, number + 1):
            if num % 2 == 0:
                even_sum += 1
            else:
                odd_sum += 1
    print('Odd: ', odd_sum, 'Even: ', even_sum)

def factorial(number):
    sum = 1

    for num in range(1, number + 1):
        sum *= num
    print(sum)

def is_empty(parameter = 0):
    if parameter == 0:
        print('Empty')
    else:
        print(parameter)

def calculate_mean(list):
    sum = 0
    count = 0

    for num in list:
        sum += num
        count += 1
    print(sum / count)

def calculate_median(list):
    new_list = []

    for num in list:
        new_list.append(num)
    new_list.sort()

    if len(new_list) % 2 == 0:
        first_num = new_list[len(new_list) // 2]
        second_num = new_list[len(new_list) // 2 - 1]
        print((first_num + second_num) / 2)
    else:
        print(new_list[len(new_list) // 2])

def calculate_mode(list):
    new_set = set(list)
    new_dict = {}
    new_list = []

    for num in new_set:
        cnt = list.count(num)
        new_dict[num] = cnt
        list.remove(num)
    max_value = max(new_dict.values())

    for key, value in new_dict.items():
        if value == max_value:
            new_list.append(key)
    print(new_list)

def calculate_range(list):
    max_value = list[0]
    min_value = list[0]

    for num in list:
        if num > max_value:
            max_value = num

    for num in list:
        if num < min_value:
            min_value = num

    print(max_value - min_value)

def calculate_variance(list):
    sum = 0
    cnt = 0
    new_list = []

    for num in list:
        sum += num
        cnt += 1

    avg = sum / cnt

    for num in list:
        disp = (num - avg) ** 2
        new_list.append(disp)

    new_sum = 0
    new_count = 0

    for num in new_list:
        new_sum += num
        new_count += 1

    res = new_sum / new_count
    return res

def calculate_std(list):
    variance = calculate_variance(list)
    print(variance ** 0.5)

def greet(name = "Hello, guest!"):
    print("Hello, " + name)

def show_args(**args):
    print("Received: ")
    for key, value in args.items():
        print(key + ": " + str(value))

evens_and_odds(12301)
factorial(10)
is_empty()
calculate_mean([1, 2, 3])
calculate_median([1, 2, 3, 4])
calculate_mode([1, 1, 2, 2, 3, -1])
calculate_range([-10, 2, 3, 4, 5, 6, 7, 8, 9, 1000])
print(calculate_variance([1, 2, 4]))
calculate_std([1, 2, 3])
greet("Alice")
show_args(name="Alice", age=30, city="New York")

# L.3

def is_prime(number):
    cnt = 0

    if number < 2:
        return
    else:
        for i in range(1, number + 1):
            if number % i == 0:
                cnt += 1
        if cnt == 2:
            print("This number is a prime number")
        else:
            print("This number is not a prime number")

def is_unique(list):
    new_set = set(list)

    if len(new_set) == len(list):
        print("Uniqueness is true")
    else:
        print("Uniqueness is false")

def data_type(list):
    list2 = []

    for item in list:
        list2.append(type(item))

    new_set = set(list2)

    if len(new_set) > 1:
        print("NO")
    else:
        print("YES")

def is_identity(str):
    if(str.isidentifier()):
        print("Correct")
    else:
        print("Incorrect")

is_prime(7)
is_unique([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
data_type(['abb', 'asdasd'])
is_identity('123aboba')