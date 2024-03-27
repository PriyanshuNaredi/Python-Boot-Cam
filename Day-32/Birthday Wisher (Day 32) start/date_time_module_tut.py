import datetime as dt

now = dt.datetime.now()
year = now.year
day_of_week = now.weekday()


print(f"{now} Type Of {type(now)}")
print(f"{year} Type Of {type(year)}")
print(day_of_week)

dob = dt.datetime(year=2001, month=7, day=29)
print(dob)
