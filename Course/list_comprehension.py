# Day 13/20

#lst = [i for i in range(10) if i % 2 == 0]
#print(lst)

#add_two_numbers = lambda x, y: x + y - 2
#print(add_two_numbers(1, 2))
#print((lambda x,y: x + y)(2,1))

#def aboba(x):
    #return lambda y: x ** y

#print(aboba(11)(2))

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered_numbers = [i for i in numbers if i <= 0]
print(filtered_numbers)

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
full_list = [number for row in list_of_lists for number in row]
print(full_list)

new_list = [(i, i ** 0, i ** 1, i ** 2, i ** 3, i ** 4, i ** 5) for i in range(11)]
print(new_list)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
new_countries_list = [(country.upper(), country[0:3], city.upper()) for part in countries for country, city in part]
print(new_countries_list)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
new_dict = {}
new_dict.update({country: country.upper(), city: city.upper()} for part in countries for country, city in part)
print(new_dict)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
new_conc_List = [(first_name + ' ' + last_name) for part in names for first_name, last_name in part]
print(new_conc_List)

print((lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1))(1, 1, 3, 2))