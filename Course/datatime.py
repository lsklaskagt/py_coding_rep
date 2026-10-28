# Day 16/30

from datetime import datetime, date

now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
timestamp = now.timestamp()
date_string = '5 December, 2019'
time_object = datetime.strptime(date_string, "%d %B, %Y")
today = date(year = 2026, month = 10, day = 28)
new_year = date(year = 2027, month = 1, day = 1)
diff = new_year - today
time_stamp_era = date(year = 1970, month = 1, day = 1)
new_today = date.today()
diff2 = new_today - time_stamp_era

print(day, month, year, hour, minute, second, timestamp)
print(f"{month}/{day}/{year}, {hour}:{minute}:{second}")
print(time_object)
print(diff)
print(diff2)