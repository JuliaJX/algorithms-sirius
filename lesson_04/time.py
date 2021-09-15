import time


time_start = time.time()
i=0

while i < 10000:
    i += 1

time_middle = time.time()
i=0

while i < 10000000:
    i += 1


time_finish = time.time()

time_span = time_finish - time_start

time_span1 = time_middle - time_start

time_span2 = time_finish - time_middle

print('Total time:', time_span)
print('Part 1', time_span1)
print('Part 2', time_span2)