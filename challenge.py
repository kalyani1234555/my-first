# write a small program to display information on the
# four clocks whose functions we have just looked at:
#i.e time(), perf_counter, monotonic() and process_time().

# use the documentation for the get_clock_info() function

import time

print("time():\t\t\t", time.get_clock_info('time'))
print("perf_counter():\t", time.get_clock_info('perf_counter'))
print("monotonic():\t", time.get_clock_info('monotonic'))
print("process_time():\t", time.get_clock_info('process_time'))
