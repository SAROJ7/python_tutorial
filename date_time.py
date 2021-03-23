import datetime
import pytz



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

dt = datetime.datetime(2021, 2, 23, 10, 38, 43, tzinfo=pytz.UTC)
print(dt)

dt_now = datetime.datetime.now(tz= pytz.UTC)
print(dt_now)

dt_utcnow = datetime.datetime.utcnow().replace(tzinfo= pytz.UTC)
print(dt_utcnow) 
# print(pytz.all_timezones)
dt_mtn = dt_utcnow.astimezone(pytz.timezone('Asia/kathmandu'))
print(dt_mtn)

# for tz in pytz.all_timezones:
#     print(tz)

dt_mmm = datetime.datetime.now()
Kathmandu_time = pytz.timezone('Asia/Kathmandu')

dt_mmm = Kathmandu_time.localize(dt_mmm)

dt_jap = dt_mmm.astimezone(pytz.timezone('Asia/Tokyo'))
dt_malta = dt_mmm.astimezone(pytz.timezone('Europe/Malta'))
dt_crotia = dt_mmm.astimezone(pytz.timezone('CET'))
dt_newz = dt_mmm.astimezone(pytz.timezone('NZ'))
dt_sing = dt_mmm.astimezone(pytz.timezone('Asia/Singapore'))


print(f'Japan time: {dt_jap}')
print(f'Malta time: {dt_malta}')
print(f'Crotia time: {dt_malta}')
print(f'NewZealand time: {dt_malta}')
print(f'Singapore time: {dt_sing}')

dt_mnm = datetime.datetime.now(tz= pytz.timezone('Asia/Kathmandu'))
print(dt_mnm.isoformat())
print(dt_mnm.strftime('%B %d, %Y'))

dt_str = 'March 23, 2021'

dt_t = datetime.datetime.strptime(dt_str,'%B %d, %Y')
print(dt_t)
