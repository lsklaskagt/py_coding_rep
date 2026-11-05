# Определение и подключение модулей
import string

from greetings import say_hello
from geometry import pi, circle_area as c_area
from converter import celsius_to_fahrenheit as c_t_f
from tax_ru import calc as c_ru
from tax_us import calc as c_us
import stats
import random
import secrets
import math

data = [10, -5, 20, 0, 30]

say_hello('aboba')
print(c_area(5))
print(c_t_f(100))
print(c_ru(100000))
print(c_us(100000))
print(stats.average_positive(data))

# Генерация байткода модулей

# Двухэтапное выполнение: При запуске программы Python сначала компилирует исходный код (.py) в промежуточный байткод, который затем интерпретируется виртуальной машиной Python.
# Каталог __pycache__: При импорте модуля интерпретатор автоматически создает папку __pycache__ и сохраняет туда скомпилированный файл .pyc (например, module.cpython-312.pyc), что ускоряет последующие запуски.
# Ручная компиляция одного файла: Встроенный модуль py_compile позволяет скомпилировать файл без его запуска вызовом py_ compile.compile("user.py").
# Массовая компиляция проекта: Модуль compileall и его функция compileall.compile_dir("путь_к_папке") рекурсивно компилируют все .py-файлы в указанном каталоге.

# Модуль random

rand_num = random.randint(1, 6)
print(rand_num)

rand_float_num = random.random() # от 0 до 1 рандомное (random.random() * 50 - от 0 до 50)
print(rand_float_num)

rand_even_num = random.randrange(10, 98, 2)
print(rand_even_num)

cards = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
random.shuffle(cards)
print(random.choice(cards))

lst = ['Орел', "Решка"]
def coin_stats(n):
    new_dict = {}
    orel = 0
    reshka = 0
    for i in range(n):
        res = random.choice(lst)
        if res == 'Орел':
            orel += 1
        elif res == 'Решка':
            reshka += 1

    new_dict["Орел"] = orel
    new_dict["Решка"] = reshka
    return new_dict

print(coin_stats(22))

def generate_ticket():
    lst = list(range(1, 50))
    random.shuffle(lst)
    return lst[:6]

print(generate_ticket())

# Модуль secrets

num = secrets.randbelow(100)
print(num)
num = secrets.randbits(16)
print(num)

tok = secrets.token_hex(16)
stroka = secrets.token_urlsafe(16)
print(stroka)
print(tok)

passw = string.ascii_letters + string.digits
stroka = ''
for i in range(0, 10):
    stroka += random.choice(passw)

print(stroka)

def check_pin(user_pin, secret_pin):
    return secrets.compare_digest(user_pin, secret_pin)

print(check_pin('123456', '12345226'))

def password_generation():
    example1 = string.digits
    example2 = string.ascii_lowercase
    example3 = string.ascii_uppercase
    res = []
    for i in range(1):
        res.append(secrets.choice(example2))
        res.append(secrets.choice(example3))
    for i in range(3):
        res.append(secrets.choice(example1))

    random.shuffle(res)
    final_res = ''.join(res)
    return final_res

print(password_generation())

# Математические функции и модуль math

print(math.sqrt(17.4))
print(math.ceil(17.4))
print(math.floor(17.4))

def cylinder_volume(r, h):
    V = math.pi * h * math.pow(r, 2)
    return V

print(cylinder_volume(5, 5))
print(cylinder_volume(5, 10))

a, b = 3, 4
hypo = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
print(hypo)
print(math.degrees(math.asin(a / hypo)))

def simplify(a, b):
    new_drob = math.gcd(a, b)
    return a / new_drob, b / new_drob

def combinations(n, k):
    if n > k:
        return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))



print(simplify(48, 180))
print(combinations(10, 5))

lst = [10.0, 100.0, math.nan, 1000.0, math.inf]
new_lst = [val for val in lst if val is not math.nan and val is not math.inf]
sum = 0
for num in new_lst:
    sum += math.log10(num)

print(sum)