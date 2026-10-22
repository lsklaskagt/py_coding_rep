# Day 2/30
# L.1

first_name = "Antoshka"
last_name = "Gricenko"
full_name = first_name + " " + last_name
country = "Russia"
city = "Tambov"
age = 19
year = 2007
is_married = False
is_light_on = True
is_hungry, weight, phone_colour = False, 80, "White"

print(first_name, last_name, full_name, country, city, age, year, is_married, is_light_on, is_hungry, weight, phone_colour)

#L.2

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_light_on))
print(max(len(first_name), len(last_name)))

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

radius = 30
pi = 3.14

area_of_circle = pi * radius
circum_of_circle = 2 * pi * radius
print(radius, area_of_circle, circum_of_circle)

person_first_name = str(input())
person_last_name = str(input())
person_country = str(input())
person_age = int(input())

print(help('keywords'))