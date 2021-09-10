import datetime
import time

import pytz

print(f'The epoch on this system starts at: {time.strftime("%c", time.gmtime(0) )}')

print(f'The current timezone is {time.tzname[0]}, {time.tzname[1]} with an offset of {time.timezone} milliseconds, \
    {time.timezone/(60*60)} in hours')

if time.daylight != 0:
    print('\tDay light saving is in effect for this location')
    print('\tThe DST timezone is '+time.tzname[1])
    
print('Local time is ' + time.strftime('%Y-%m-%d %H-%M-%S', time.localtime()))
print('GMT time is ' + time.strftime('%Y-%m-%d %H-%M-%S', time.gmtime()))



print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())

country = "Europe/Moscow"
country = "IST"
tz_to_display = pytz.timezone(country)
print(tz_to_display)
local_time = datetime.datetime.now(tz=tz_to_display)
print(f'The time in {country} is {local_time}')
print(f'UTC is {datetime.datetime.utcnow()}')

# The following piece of code shows the problem pytz can give. I was shocked when I first found it out.
# I.e. the timezone created by pytz is for the true local time, instead of the standard local time people observe.
# Shanghai conforms to +0800, not +0806 as suggested by pytz:

# print((datetime(2017,2,13,14,29,29, tzinfo=pytz.timezone('Asia/Shanghai'))
#      - datetime(2017,2,13,14,29,29, tzinfo=pytz.timezone('UTC')))
#      .total_seconds())
# print((datetime(2017,2,13,14,29,29, tzinfo=dateutil.tz.gettz('Asia/Shanghai'))
#      - datetime(2017,2,13,14,29,29, tzinfo=dateutil.tz.tzutc()))
#      .total_seconds())
#
# -29160.0
# -28800.0

