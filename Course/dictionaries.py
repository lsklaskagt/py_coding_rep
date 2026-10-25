# Day 8/30

dog = {}
dog['name'] = 'Hell'
dog['color'] = 'blue'
dog['age'] = 10
dog['legs'] = True
print(dog)

student = {'first_name' : 'Marcus', 'last_name' : 'Cloverty', 'gender' : 'Male', 'age' : 19, 'Marital status' : 'Not married', 'skills' : ['Python, SQL'], 'country' : 'USA', 'city' : 'Washington', 'address' : 'Downing street, 51'}
print(student)
print(len(student))
print(student['skills'])
print(type(student['skills']))
student['skills'].append('Java')
print(student)
print(student.keys())
print(student.values())

print(student.items())
del student['age']
print(student)

del student