# Day 3/40

age : int
height : float
complex_number : complex

side = float(input("Введите основание: "))
h = float(input("Введите высоту: "))
print("Площадь треугольника равна: ", side * h)

a = float(input("Введите первую сторону: "))
b = float(input("Введите вторую сторону: "))
c = float(input("Введите третью сторону: "))
print("Периметр треугольника равен: ", a + b + c)

length = float(input("Введите длину прямоугольника: "))
width = float(input("Введите ширину треугольника: "))
print("Площадь прямоугольника равна: ", length * width)
print("Периметр прямоугольника равен: ", 2 * (length + width))

radius = float(input("Введите радиус круга: "))
pi = 3.14159
circle_area = pi * (radius ** 2)
circle_length = 2 * pi * radius
print(circle_area, circle_length)

slope = 2
y_intercept = -2
x_intercept = 1

x1 = 2
x2 = 6
y1 = 2
y2 = 10
new_slope = (y2 - y1) / (x2 - x1)
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(new_slope, distance)
print(slope == new_slope)

x = -3
print((x ** 2 + 6 * x + 9) == 0)

len1 = len('python')
len2 = len('dragon')
print(len1 is not len2)

print('on' in 'python', 'on' in 'dragon')
print('jargon' in 'I hope this course is not full of jargon')

print(str(float(len('python'))))

number = int(input("Введите число для проверки четно ли оно: "))
print(number % 2 == 0)

print(7 // 3 == int(2.7))

print(type('10') == type(10))

print(int(9.8) == 10)

hours = int(input("Введите часы: "))
income_per_hour = int(input("Введите ставку за час: "))
print(hours * income_per_hour)

person_age = int(input("Введите количество лет: "))
print("Человек прожил приблизительно: ", person_age * 12 * 31 * 24 * 60 * 60, " секунд")

n = 1
print(n, n ** 0, n ** 1, n ** 2, n ** 3)
n += 1
print(n, n ** 0, n ** 1, n ** 2, n ** 3)
n += 1
print(n, n ** 0, n ** 1, n ** 2, n ** 3)
n += 1
print(n, n ** 0, n ** 1, n ** 2, n ** 3)
n += 1
print(n, n ** 0, n ** 1, n ** 2, n ** 3)
