# Day 9/30
# L.1

age = int(input('Enter your age: '))

if (age > 18) :
    print("You are old enough to learn to drive.")
else:
    print(f"You need {18 - age} more years to learn to drive.")

my_age = 21
your_age = int(input('Enter your age: '))

if (my_age > your_age) :
    print(f"I'm {my_age - your_age} years older than you.")
else:
    print(f"You are {your_age - my_age} years older than me.")

first_number = int(input('Enter your first number: '))
second_number = int(input('Enter your second number: '))

if (first_number > second_number) :
    print(f"{first_number} is greater than {second_number}.")
elif (first_number < second_number) :
    print(f"{first_number} is less than {second_number}.")
else :
    print(f"{first_number} is equal to {second_number}.")

# L.2

score = int(input('Enter your score: '))

if (score >= 90 and score <= 100) :
    print("Your mark is A")
elif (score >= 80 and score <= 89) :
    print("Your mark is B")
elif (score >= 70 and score <= 79) :
    print("Your mark is C")
elif (score >= 60 and score <= 69):
    print("Your mark is D")
elif (score >= 0 and score <= 59):
    print("Your mark is F")

month = str(input('Enter your month: '))

if (month == 'September' or month == 'October' or month == 'November'):
    print("Autumn")
elif (month == "December" or month == "January" or month == "February"):
    print("Winter")
elif (month == 'March' or month == 'May' or month == 'April'):
    print("Spring")
elif (month == 'June' or month == 'July' or month == 'August'):
    print("Summer")
else:
    print("Enter a valid month!")

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = str(input('Enter your fruit name: '))
if (fruit in fruits):
    print(f"Fruit {fruit} is already in fruits")
else:
    fruits.append(fruit)
    print(f"Fruit {fruit} is now in fruits")
    print(fruits)

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if ('skills' in person):
    skills = person['skills']
    length = len(skills)
    print(person['skills'][length // 2])

if ('skills' in person):
    if ('Python' in person['skills']):
        print("Yes")

if ('skills' in person):
    if ('JavaScript' in person['skills'] and 'React' in person['skills']):
        print('He is a front end developer')
    elif ('Python' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']):
        print('He is a back end developer')
    elif ('React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']):
        print('He is a full stack developer')
    else:
        print("Unknown")