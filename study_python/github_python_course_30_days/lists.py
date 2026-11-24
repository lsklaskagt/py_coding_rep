# Day 5/30
# L.1

lst1 = []
lst2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(len(lst2))
print(lst2[0], lst2[(len(lst2) - 1) // 2], lst2[-1])

mixed_data_types = ['Dima', 23, 173, 'Married', 'Moscow']
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print(mixed_data_types)
print(len(it_companies))
print(it_companies[0], it_companies[-1], it_companies[(len(it_companies) - 1) // 2])
it_companies.append('Yadro')
print(it_companies)
it_companies.insert((len(it_companies) - 1) // 2, 'Yandex')
print(it_companies)
it_companies[1] = it_companies[1].upper()
print(it_companies)
it_companies.append('#; ')
print(it_companies)
company_exist = 'Facebook' in it_companies
print(company_exist)
it_companies.sort()
print(it_companies)
it_companies.reverse()
print(it_companies)
del it_companies[0:3]
print(it_companies)
del it_companies[-3:]
print(it_companies)
it_companies.remove(it_companies[(len(it_companies) - 1) // 2])
print(it_companies)
it_companies.remove(it_companies[0])
print(it_companies)
it_companies.clear()
print(it_companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)
print(front_end)

full_stack = front_end.copy()
dop = full_stack.index('Redux')
full_stack.insert(dop + 1, 'Python')
full_stack.insert(dop + 2, 'SQL')
print(full_stack)

# L.2

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min_elem = ages[0]
max_elem = ages[-1]
print(ages, "\n", min_elem, max_elem)
ages.append(min_elem)
ages.append(max_elem)
print(ages)
dop1 = ages[(len(ages) - 1) // 2]
dop2 = ages[(len(ages) - 1 ) // 2  + 1]
med_elem = (dop1 + dop2) // 2
print(med_elem)
ages_len = len(ages)
sum = ages[0] + ages[1] + ages[2] + ages[3] + ages[4] + ages[5] + ages[6] + ages[7] + ages[8] + ages[9] + ages[10] + ages[11]
avg = sum / ages_len
range = max_elem - min_elem
print(avg)
print(range)
print(abs(min_elem - avg) > abs(max_elem - avg))

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]

print(countries[(len(countries) - 1) // 2])

countries.insert(0, 'Sahara')
print(len(countries))
dop1 = countries.copy()
del dop1[0:(len(countries) - 1) // 2 + 1]
first_part = dop1
dop2 = countries.copy()
dop3 = (len(countries) - 1) // 2
del dop2[dop3:(len(countries) - 1)]
second_part = dop2
print(first_part)
print(second_part)

new_list = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

a, b, c, d, e, f, g = new_list
print(a.upper(), b.lower(), c, d, e, f, g)
print(c.endswith('SA'))