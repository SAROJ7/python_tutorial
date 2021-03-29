import datetime
import pytz


a = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)

b = str(a)

print (str(a))
print (repr(a))

print (str(b))
print (repr(b))