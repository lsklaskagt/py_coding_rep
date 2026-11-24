# Day 6/30
# L.1

new_tuple = ()
brothers = ('Vlad', 'Dima', 'Antoshka', 'Matvey')
sisters = ('Masha', 'Lera')
siblings = brothers + sisters
print(siblings)
print(len(siblings))
new_list = list(siblings)
new_list.append('Nadya')
new_list.append('Aleks')
print(tuple(new_list))

# L.2

s1, s2, s3, s4, s5, s6, s7, s8 = new_list
print(s1, s2, s3, s4, s5, s6, s7, s8)
fruit = ('apple', 'banana', 'orange')
vegetables = ('cucumber', 'tomato')
animal_product = ('milk', 'beef')
food_stuff_tp = fruit + vegetables + animal_product
print(food_stuff_tp)
food_stuff_list = list(food_stuff_tp)
print(len(food_stuff_list))
del food_stuff_list[(len(food_stuff_list) - 1) // 2]
print(food_stuff_list)
del food_stuff_list[0:3]
del food_stuff_list[0:3]
print(food_stuff_list)
del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
does_exist = 'Estonia' in nordic_countries
print(does_exist)
does_exist = 'Finland' in nordic_countries
print(does_exist)