# Day 4/30

print('Coding ' + 'For ' + 'All')

a = 'Thirty '
b = 'Days '
c = 'Of '
d = 'Python'

print(a + b + c + d)

name = 'Coding For All'
print(name, len(name))
print(name.upper())
name2 = name.lower()
print(name2.capitalize())
print(name2.title())
print(name2.swapcase())

print(name[6:])
print(name.index('Coding'))
print(name.replace('Coding', 'Python'))
print(name.replace('Coding For All', 'Python For All'))
print(name.split())

name3 = "Facebook Google Microsoft Apple IBM Oracle Amazon"
print(name3.split())

print(name[0])
print(name[-1])
print(name[10])
print(name[0], name[7], name[11])

print(name.index('C'))
print(name.index('F'))
print(name.rfind('l'))

name4 = 'You cannot end a sentence with because because because is a conjunction'
print(name4.index('because'))
print(name4.rfind('because'))
print(name4.rindex('because'))
print(name4[31:54])

name5 = 'aboba aboba aboba'
print(name5.rindex('aboba'))

print(name.startswith('Coding'))
print(name.endswith('coding'))

name6 = '   Coding For All      '
print(name6.strip(' '))

name7 = "30DaysOfPython"
name8 = "thirty_days_of_python"
print(name7.isidentifier(), name8.isidentifier())

name9 = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
res = ' '.join(name9)
print(res)

print("I am enjoying this challenge.\nI just wonder what is next.")

print("Name\tAge\tCountry\tCity\tAsabeneh\t250\tFinland\tHelsinki")

radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle with radius {radius} is {int(area)} meteres square.')

first_num = 8
second_num = 6

print(f"{first_num} + {second_num} = {first_num + second_num}")
print(f"{first_num} - {second_num} = {first_num - second_num}")
print(f"{first_num} * {second_num} = {first_num * second_num}")
print(f"{first_num} / {second_num} = {(first_num / second_num):.33f}")
print(f"{first_num} // {second_num} = {first_num // second_num}")
print(f"{first_num} % {second_num} = {first_num % second_num}")
print(f"{first_num} ** {second_num} = {first_num ** second_num}")