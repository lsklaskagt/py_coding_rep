# Списки

names = ["Tom", "John", "Bob", "Jane"]
print(names[0], names[2], names[-1])

nums = [10, 20, 30]
nums[1] = 25
nums.append(40)
nums.insert(0, 5)
print(nums)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
list1 = letters[:3]
list2 = letters[2:5]
list3 = letters[::-1]
print(list1)
print(list2)
print(list3)

items = [1, 2, 3, 2, 4, 2, 5]
cnt = items.count(2)
items.remove(2)
per = items.pop(-1)
print(items)
print(cnt)
print(per)

a = [1, 2]
b = [3, 4]
a.extend(b)
c = a.copy()
c.append(99)
print(a)
print(c)

words = ['яблоко', 'кот', 'апельсин', 'дом', 'банан']
words.sort(key = len)
print(words)

data = [4, 1, 4, 2, 4, 3, 4]
while 4 in data:
    data.remove(4)
print(data)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
summa = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end = ' ')
        if i == j:
            summa += matrix[i][j]
print(f"\n{summa}")

# Кортежи

single = (42,)
print(type(single))

cities = ["Москва", "Казань", "Сочи"]
new_tuple = tuple(cities)
print(len(new_tuple))
print(new_tuple[-1])

user = ("Alex", 28, "Google")
name, age, company = user
print(f"Имя: {name}, Возраст: {age}, Компания: {company}")

nums = (10, 20, 30, 40, 50, 60)
print(nums[0::2])

def get_min_max(nums):
    max = nums[0]
    min = nums[0]
    for num in nums:
        if num > max:
            max = num

        if num < min:
            min = num
    new_tuple = (min, max)
    return new_tuple

print(get_min_max([4, 1, 9, -2, 5]))

langs = ("Python", "C++", "Java", "C++", "Go")
if "C++" in langs:
    print(langs.index("C++"))
    print(langs.count("C++"))

tpl = ("Tom", 22, "Student")
new_list = list(tpl)
new_list[1] = 23
tpl = tuple(new_list)
print(tpl)

students = (("Анна", [5, 4, 5]), ("Борис", [3, 4, 3]), ("Виктор", [5, 5, 5]))
for name, grades in students:
    avg = sum(grades) / len(grades)
    if avg > 4.5:
        print(name)

# Диапазоны range

lst = [i for i in range(0, 6)]
print(lst)

lst = [i for i in range (5, 13)]
print(lst)

print([i for i in range(2, 21, 2)])

lst = [i for i in range(10, 0, -1)]
print(lst)

summa = [i for i in range(1, 101) if i % 5 == 0]
print(sum(summa))

nums = [1, 2, 3, 4, 5]
nums = [i * i for i in range(len(nums))]
print(nums)

r = range(10, 100, 7)
print(len(r))
print(r[0])
print(r[-1])
print(52 in r)

for i in range(1, 5):
    for j in range(1, 5):
        print(i * j, end="\t")
    print()

# Словари

person = {'name': 'Alice', 'age': 25}
print(person['name'])
person['age'] = 26
person['city'] = 'Moscow'
print(person)

prices = {'apple': 100, 'banana': 80}
print(prices.get('apple'))
print(prices.get('orange'), 0)

codes = {'ru': 7, 'us': 1, 'uk': 44}
deleted = codes.pop('us')
deleted2 = codes.pop('aboba', 0)
print(codes)

grades = {'Math': 5, "Physics": 4, 'History': 5}
for subj, grade in grades.items():
    print(f"{subj}: {grade}")

d1 = {'a': 1, 'b': 2}
d2 = {'b': 20, "c": 30}

d3 = d1.copy()
d3.update(d2)
print(d3)

text = 'abracadabra'
dicti = {}
for char in text:
    dicti[char] = text.count(char)
print(dicti)

capitals = {"Russia": 'Moscow', 'France': 'Paris', "italy": "Rome"}
new_dict = {}
for key, value in capitals.items():
    new_dict[value] = key
print(new_dict)

new_dict = {'u1': {'name': 'Tom', 'salary': 80000}, 'u2': {'name': 'Bob', 'salary': 120000}, 'u3': {'name': 'Alice', 'salary': 95000}}
for key, value in new_dict.items():
    for subkey, subvalue in value.items():
        if subkey == 'salary' and subvalue < 100000:
            res = subvalue + 0.1 * subvalue
            value[subkey] = int(res)
print(new_dict)

# Множества

nums = [1, 2, 2, 3, 4, 4, 4, 5]
print(set(nums))

tools = {'hammer', 'wrench'}
tools.add('saw')
tools.remove('hammer')
tools.discard('aboba')
print(tools)

set_a = {1, 2, 3}
set_b = {3, 4, 5}
set_c = set_a.union(set_b)
print(set_c)

math_club = ['Tom', 'Bob', 'Alice']
code_club = ['Alice', 'Sam', 'Tom']
new_set = set(math_club) & set(code_club)
print(new_set)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c = a.difference(b)
d = a.symmetric_difference(b)
print(c)
print(d)

required = {"Python", "SQL"}
candidate_skills = {"Python", "SQL", "Git", "Docker"}
print(required.issubset(candidate_skills))

s1 = 'python is easy and python is powerful'
s2 = 'python and c++ are powerful'
set_s1 = set(s1.split())
set_s2 = set(s2.split())
set_s3 = set_s1.difference(set_s2)
print(set_s3)

# List comprehension

new_list = [i * i for i in range(1, 8)]
print(new_list)

nums = [-5, 3, -1, 0, 8, -2, 4]
new_nums = [i for i in nums if i > 0]
print(new_nums)

names = [' alice ', 'BOB', ' charlie']
new_list = [name.strip().capitalize() for name in names]
print(new_list)

nums = [-3, -2, 0, 1, 4]
new_list = [i * 2 if i > 0 else 0 for i in nums]
print(new_list)

products = {'Хлеб': 50, "Молоко": 90, "Сыр": 350, "Масло": 220}
new_list = [f"{key}: {value}" for key, value in products.items() if value > 100]
print(new_list)

text = 'Заказ №405 от 12 мая: 3 позиции'
new_list = [int(char) for char in text if char.isdigit()]
print(new_list)

matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
new_list = [item for row in matrix for item in row]
print(new_list)

new_list = [i for i in range(1, 51) if (i % 3 == 0 or i % 5 == 0 and i % 15 != 0)]
print(new_list)

# Упаковка и распаковка

coords = [10, 20, 30]
x, y, z = coords
print(x + y + z)

data = ("Ivan", "secret_hash", "ivan@mail.ru", 2026)
name, _, email, _ = data
print(name, email)

scores = [100, 95, 80, 75, 60]
first, second, *others = scores
print(first, second, others)

start, *middle, end = range(1, 8)
print(start, middle, end)

fruits = ['Яблоко', "Груша", "Слива"]
for index, name in enumerate(fruits):
    print(f"{index}. {name}")

a = [1, 2]
b = (3, 4)
str = '56'
new_coll = [*a, *b, *str]
print(new_coll)

defaults = {'theme': 'light', 'lang': 'ru', 'notifications': True}
custom = {'theme': 'dark'}
new_dict = {**defaults, **custom}
print(new_dict)

record = ("Отдел разработки", ['Анна', "Борис", "Влад"], (101, 102))
dept, (lead, *team), (main_room, _) = record
print(f"dept={dept!r}, lead={lead!r}, team={team}, main_room={main_room}")

# Упаковка и распаковка в параметрах функций

def sum_all(*args):
    sum = 0
    for num in args:
        sum += num
    return sum

print(sum_all(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

def print_info(**kwargs):
    print(kwargs)

print_info(name = 'Tom', age = 24)

def multiply_by(factor, *nums):
    return [num * factor for num in nums]

print(multiply_by(2, 1, 2))

def calc_volume(a, b, c):
    return a * b * c

sides = [2, 5, 10]
print(calc_volume(*sides))

# Функция zip

names = ['Tom', 'Bob', 'Alice']
ages = [25, 30, 22]
for name, age in zip(names, ages):
    print(f"{name}: {age}")

keys = ['id', 'login', 'status']
vals = [101, 'admin', 'active']
new_dict = dict(zip(keys, vals))
print(new_dict)

products = ["Телефон", "Ноутбук", "Планшет", "Часы"]
prices = [50000, 90000]
new_list = list(zip(products, prices))
print(new_list)

names = ["Аня", "Боря"]
scores = [95, 88]
cities = ["Мск", "СПб"]
for name, score, city in zip(names, scores, cities):
    print(f"{name}: {score} ({city})")

prices = [100, 250, 50]
counts = [2, 1, 4]
print(sum([price * count for price, count in zip(prices, counts)]))

def safe_pair(list1, list2):
    try:
        return list(zip(list1, list2, strict = True))
    except ValueError:
        return "Ошибка"

print(safe_pair([1, 2], ['a', 'b']))

points = [(1, 10), (2, 20), (3, 30)]
x_coords, y_coords = zip(*points)
print(x_coords, y_coords)

matrix = [[1, 2, 3], [4, 5, 6]]
print([list(col) for col in zip(*matrix)])