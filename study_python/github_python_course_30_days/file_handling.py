# Day 19/30

from pathlib import Path

file_path = Path.home() / 'Desktop' / 'reading_file_example.txt'
f = open(file_path, 'r')
full_text = f.read()
print(full_text)
f.close()

file_path = Path.home() / 'Desktop' / 'reading_file_example.txt'
f = open(file_path, 'r')
first_line = f.readline()
print(first_line)
f.close()

file_path = Path.home() / 'Desktop' / 'reading_file_example.txt'
f = open(file_path, 'r')
list_of_strings = f.readlines()
print(list_of_strings)
f.close()

file_path = Path.home() / 'Desktop' / 'reading_file_example.txt'
f = open(file_path, 'r')
list_of_strings = f.read().splitlines()
print(list_of_strings)
f.close()

# файл сам закрывается если используем with
with open(file_path, 'r') as f:
    print(f.read())

with open(file_path, 'r') as f:
    print(f.read().splitlines())

with open(file_path, 'a') as f:
    f.write('New line at the end of the file')

with open(file_path, 'r') as f:
    print(f.read())