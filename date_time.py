import datetime


# date(year/month/day)
d = datetime.date(2016, 7, 12)
print(d)
tday = datetime.date.today()
print(tday)
print(tday.year)
print(tday.month)
print(tday.day)
print(tday.weekday())
print(tday.isoweekday())

tdelta = datetime.timedelta(days=7)
print(tday + tdelta)
print(tday - tdelta)

bday = datetime.date(2021, 12, 13)

till_bday = bday - tday
print(till_bday)
print(till_bday.days)
print(till_bday.total_seconds())

# time (hours/ minutes / seconds)
t = datetime.time(2, 31, 48, 100000)
print(t)

t1 = datetime.datetime(1996, 12, 13, 6, 30 , 16, 100000)
print(t1.date())
print(t1.time())
t2 = datetime.datetime.today()
t_now = datetime.datetime.now()
t_utc = datetime.datetime.utcnow()
print(t2 - t1)
print(t1 + tdelta)

print(t2)
print(t_now)
print(t_utc)