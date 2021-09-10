import time

print(time.gmtime(0))

print(time.localtime())

print(time.time())

curr_time = time.localtime()

print('Year:', curr_time[0], curr_time.tm_year)

print('Month:', curr_time[1], curr_time.tm_mon)

print('day:', curr_time[2], curr_time.tm_mday)

for i in curr_time:
    print(i)

for i in range(len(curr_time)):
    print(curr_time[i])