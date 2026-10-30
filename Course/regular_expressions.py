# Day 18/30

import re
from traceback import print_tb

txt = 'I love to teach python and javaScript'
match = re.match('I love to teach python', txt, re.IGNORECASE)
span = match.span()
start, end = span
print(match)
print(span)
print(start, end)

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
search = re.search('a', txt, re.IGNORECASE)
print(search)

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
search_all = re.findall('python', txt, re.IGNORECASE)
print(search_all)

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
search_all = re.findall('Python|python', txt)
print(search_all)

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
search_all = re.findall('[Pp]ython', txt, re.IGNORECASE)
print(search_all)

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
match_replace = re.sub('Python|python', 'Java', txt)
print(match_replace)


txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing.
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs.
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

res = re.sub('%', '', txt)
print(res)

txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
print(re.split('\n', txt))

txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
regex_pattern = r'apple'
match = re.findall(regex_pattern, txt, re.IGNORECASE)
print(match)

txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
regex_pattern = r'[Aa]pple'
match = re.findall(regex_pattern, txt)
print(match)

# L.1

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

words = re.findall('[a-zA-Z]+', paragraph)

new_set = set(words)
new_dict = {}

for word in new_set:
    cnt = words.count(word)
    new_dict[word] = cnt

max_value = -1
max_key = None

for key, count in new_dict.items():
    if count > max_value:
        max_value = count
        max_key = key
print(f"Самое встречающее слово:  {max_key}, {max_value} раз")

text = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction."
points = re.findall('[-]\d+|\d+', text)
res = int(points[-1]) - int(points[0])
print(res)