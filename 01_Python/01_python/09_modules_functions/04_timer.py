# from time import time as my_timer
import random
import time
from time import monotonic
from time import perf_counter
from time import process_time  # this is basically used to measure CPU time

# Measuring using the time.time
# This displays the actual local time
input('Press enter to start')
wait_time = random.randint(1, 5)
time.sleep(wait_time)
start_time = time.time()
input('Press enter to measure your response time: ')
end_time = time.time()

print(f"""Started at {time.strftime("%X", time.localtime(start_time))} 
and ended at {time.strftime("%X", time.localtime(end_time))}. 
Total reaction time is {end_time-start_time}
""")

# Measuring using the perf_counter - this is more efficient
# Doesn't display the local time
time.sleep(random.randint(1, 3))
start_time = perf_counter()
input('Performance measured based on the Performance counter, click enter: ')
end_time = perf_counter()
print(f"""Started at {time.strftime("%X", time.localtime(start_time))}, 
ended at {time.strftime("%X", time.localtime(end_time))},
Response time is: {end_time - start_time}
""")

# Measuring the time using the monotonic - This shall ensure time will always go forward
# even if there is a daylight saving time adjustments on the system clock
# Doesn't display the local time
time.sleep(random.randint(1, 3))
start_time = monotonic()
input("Press enter to measure your response time using monotonic: ")
end_time = monotonic()
print(f"""Start time is {time.strftime("%X", time.localtime(start_time))},
End time is {time.strftime('%X', time.localtime(end_time))},
Response time is {end_time - start_time}
""")

# Measuring the CPU time
# Doesn't display the local time
time.sleep(random.randint(a=1, b=3))
start_time = process_time()
input("Press enter to record your response time using process time: ")
end_time = process_time()
print(f"""Start time is {time.strftime('%X', time.localtime(start_time))},
end time is {time.strftime('%X', time.localtime(end_time))}, 
Response time is {end_time - start_time}
""")

# Challenge to get information about clock functions using get_clock_info()
list_clocks = ['time', 'perf_counter', 'monotonic', 'process_time']
for element in list_clocks:
    print(time.get_clock_info(element))


