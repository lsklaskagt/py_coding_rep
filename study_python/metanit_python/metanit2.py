# Оператор return и возвращение результата функции
from http.cookiejar import request_path
from math import factorial
import time

def sum_of_two_numbers(a, b):
    return a + b

def number_of_symbols_in_string(str):
    return len(str)

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

def max_in_list(nums):
    max = nums[0]
    for num in nums:
        if num > max:
            max = num
    return max

def a_divided_by_b(num1, num2):
    quotient = num1 / num2
    remainder = num2 % num1
    return quotient, remainder

def new_str_list(list):
    new_str = ''
    for item in list:
        if item != "":
            item = item + ", "
            new_str += item
    return new_str[0:len(new_str) - 2]

def new_dict(dict):
    new_dict = {}
    sum = 0
    cnt = 0
    for key, value in dict.items():
        sum += value
        cnt += 1
    avg = sum / cnt

    for key, value in dict.items():
        if value > avg:
            new_dict[key] = value
    return new_dict

# Функция как тип, параметр и результат другой функции

get_length = len(str(input()))

def square(num):
    return num ** 2

def cube(num):
    return num ** 3

def apply_operation(num, func):
    res = func(num)
    return res

def check(num):
    if num > 0 and num < 100 and num % 2 == 0:
        return True
    else:
        return False

def filter_data(nums, func):
    new_list = []
    for num in nums:
        if func(num):
            new_list.append(num)
    return new_list

def get_multiplier_function(n):
    def multiplier(num):
        return num * n
    return multiplier

def map_custom(nums, func_list):
    new_list = []
    for num in nums:
        for func in func_list:
            new_list.append(func(num))
    return new_list

def build_query(base_url):
    def add_params(params_dict):
        pairs = [f'{key}={value}' for key, value in params_dict.items()]
        str = '&'.join(pairs)
        return f'{base_url}?{str}'
    return add_params

def compose(f, g):
    def inner(x):
        return f(g(x))
    return inner

# Лямбда-выражения

res = lambda x: x ** 3

res = lambda x, y: x * y

nums = [-1, 2, 3, -5]
res = list(filter(lambda x: x > 0, nums))

words = ['aob', 'bs', 'sdasd']
res = list(map(lambda word: word[0], words))

list_of_tuples = [(1, 'c'), (3, 'a'), (2, 'b')]
list_of_tuples.sort(key = lambda x: x[1]) # сортировка по второму элементу key = lambda x: x[1]

datasets = [{"name": "users", "rows": 1010}, {"name": "logs", "rows": 500}, {"name": "transactions", "rows": 2250}]
datasets.sort(key = lambda x: x["rows"], reverse = True)

# Преобразование типов

num = 42
string = ' - ответ на главный вопрос'
new_str = str(num) + string
print(new_str)

string = '145.78'
float_number = float(string)
int_number = int(float_number)
print(int_number)

list_of_symbols = ['d', 'a', 't', 'a']
a, b, c, d = list_of_symbols
new_list = a + b + c + d
print(new_list)

base_string = '10;20;30'
numbers = []
text = base_string.replace(';', ' ')
for word in text.split():
    if word != ' ':
        numbers.append(int(word))

print(numbers)

tuple_list = [('id', 1), ('value', 100)]
new_dict = dict(tuple_list)
print(new_dict)

base_list = [1, 2, 3, 'aboba', 'hio', [-10, 'aboba']]
new_list = []
for item in base_list:
    new_list.append(str(item))

print(new_list)

string_list = ['True', 'False', 'true', '1', '0', '', 'false', '10']
print(string_list)
new_list = []
for item in string_list:
    if item == 'True':
        new_list.append(True)
    elif item == 'False':
        new_list.append(False)
    elif item == 'true':
        new_list.append(True)
    elif item == 'false':
        new_list.append(False)
    elif item == '0':
        new_list.append(False)
    elif item.isdecimal() and int(item) != 0:
        new_list.append(True)
    elif item == '':
        new_list.append(False)

print(new_list)

# Область видимости переменных

pi = 3.14

def area_of_circle(radius):
    area = pi * radius * radius
    return area

res = area_of_circle(3)
print(f"{res:.02f}")

counter = 0

def do_something():
    counter = 5
    return counter

res = do_something()
print(res)
print(counter)

def plus_one():
    global counter
    counter += 1
    return counter

plus_one()
plus_one()
plus_one()
print(counter)

def first_func():
    local_counter = 0
    print(local_counter)

def second_func():
    new_counter = local_counter + 1
    print(new_counter)

try:
    second_func()
except:
    print("Локальная переменная использована вне своего контекста")

def first_func():
    local_counter = 0
    def second_func():
        nonlocal local_counter
        local_counter += 1
        print(local_counter)
    second_func()
    print(local_counter)

first_func()

def third_func():
    for i in range(5):
        pass
    print(i)

third_func()

x = 10
def fourth_func():
    x = 12
    def fifth_func():
        x = 15
        print(x)
    fifth_func()
    print(x)

fourth_func()
print(x)

# Замыкание
# замыкание включает три компонента:
# внешняя функция, которая определяет некоторую область видимости и в которой определены некоторые переменные и параметры - лексическое окружение
# переменные и параметры (лексическое окружение), которые определены во внешней функции
# вложенная функция, которая использует переменные и параметры внешней функции

def outer():  # внешняя функция
    n = 5  # лексическое окружение - локальная переменная
    def inner():  # локальная функция
        nonlocal n
        n += 1  # операции с лексическим окружением
        print(n)
    return inner

f = outer() # f = функция inner, т.к функция outer() возвращает функцию inner()
f()
f()

def outer(name):
    def inner():
        print(f"Привет {name}")
    return inner

f = outer("Amogus")
f()
f = outer("Avtobus")
f()

def outer():
    base_number = 100
    def inner(x):
        print(base_number + x)
    return inner

f = outer()
f(10)
f(200)

def outer():
    counter = 0
    def inner():
        nonlocal counter
        counter += 1
        print(counter)
    return inner

f = outer()
f()
f()
f()

def make_divider(d):
    def inner(x):
        print(x / d)
    return inner

f = make_divider(11.21)
f(5.21)

def make_html_tag(div):
    def inner(text):
        print(f"<{div}>{text}</{div}>")
    return inner

f = make_html_tag("p")
f("something")

def moving_average():
    numbers = []
    def inner(x):
        numbers.append(x)
        print(sum(numbers) / len(numbers))
    return inner

f = moving_average()
f(1)
f(10)

def moving_average():
    sum = 0
    count = 0
    def inner(x):
        nonlocal sum, count
        sum += x
        count += 1
        print(sum / count)
    return inner

f = moving_average()
f(10)
f(20)
f(30)

def outer():
    cache = {}
    def inner(n):
        for n in cache:
            print(f"Нашлось мгновенно для {n}")
            return cache[n]

        res = factorial(n)
        cache[n] = res
        return res
    return inner

f = outer()
print(f(4))
print(f(4))

# Декораторы
# Декораторы в Python представляют функцию, которая в качестве параметра получает функцию и в качестве результата также возвращает функцию.
# Декораторы позволяют модифицировать выполняемую функцию, значения ее параметров и ее результат без изменения исходного кода этой функции.

# определение функции декоратора
def select(input_func):
    def output_func():  # определяем функцию, которая будет выполняться вместо оригинальной
        print("*****************")  # перед выводом оригинальной функции выводим всякую звездочки
        input_func()  # вызов оригинальной функции
        print("*****************")  # после вывода оригинальной функции выводим всякую звездочки

    return output_func  # возвращаем новую функцию


# определение оригинальной функции
@select  # применение декоратора select
def hello():
    print("Hello METANIT.COM")

# вызов оригинальной функции
hello()

def log_call(input_func):
    def output_func():
        print("Начало работы функции")
        input_func()
        print("Конец выполнения функции")
    return output_func

@log_call
def hello():
    print("Hello world!")

hello()

def timeit(input_func):
    def output_func():
        start_time = time.time()
        input_func()
        end_time = time.time()
        print(end_time - start_time)
    return output_func

@timeit
def hello():
    print("Hello world!")

hello()

def select(input_func):
    def output_func(*args, **kwargs):
        print(*args, **kwargs)
        input_func(*args, **kwargs)
    return output_func

@select
def print_person(name, age):
    print(f"Name: {name}, Age: {age}")

print_person("Matthew", 23)

def double_result(input_func):
    def output_func(*args):
        res = args[0] * 2
        input_func(res)
    return output_func

@double_result
def func(num):
    print(num)

func(10)
func(20)

def ignore_exceptions(input_func):
    def output_func(*args):
        try:
            input_func(*args)
        except:
            print("Error")
    return output_func

@ignore_exceptions
def div(a, b):
    print(a / b)

div(10, 10)
div(10, 0)

def repeat(n):
    def decorator(input_func):
        def output_func(*args):
            for i in range(n):
                res = input_func(*args)
            return res
        return output_func
    return decorator

@repeat(4)
def func(name):
    print(f"Hello {name}")

func("Matthew")

def type_check(*expected_arguments):
    def decorator(input_func):
        def output_func(*args):
            for arg, expect in zip(args, expected_arguments):
                if not isinstance(arg, expect):
                    raise TypeError
            return input_func(*args)
        return output_func
    return decorator

@type_check(int, int)
def multiply(a, b):
    print(a * b)

multiply(10, 10)
multiply(10, 10.2)