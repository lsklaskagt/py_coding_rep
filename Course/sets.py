# Day 7/30
# L.1

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add('Twitter')
print(it_companies)
it_companies.update(['Yadro', 'Yandex', 'VK'])
print(it_companies)
it_companies.remove('Yadro') # если нету элемента в списке - ошибка, лучше юзать discard() он не выдает
print(it_companies)

# L.2

set1 = A.union(B)
print(set1)
set2 = A.intersection(B)
print(set2)
print(A.issubset(B))
print(A.isdisjoint(B))
set3 = A.union(B)
set4 = B.union(A)
print(set3 == set4)
print(A.symmetric_difference(B))
del A
del B

# L.3

new_age = set(age)
print(new_age)

str = 'I am a teacher and I love to inspire and teach people.'
print(str.split())
new_list = str.split()
first_len = len(new_list)
print(first_len)
new_set = set(new_list)
diff = len(new_list) - (len(new_list) - len(new_set))
print(diff)
print(new_set)