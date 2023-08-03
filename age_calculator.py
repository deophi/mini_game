import datetime
today = datetime.datetime.now().date()
dob = datetime.date(1998, 9, 4)
age = int((today-dob).days / 365.25)

print(age)