from timeit import default_timer as timer
from datetime import timedelta

start = timer()
total = 0
for i in range(100):
    for j in range(1000):
        for k in range(10000):
            total += 1

end = timer()
print('ASC', timedelta(seconds=end-start))


start = timer()
total2 = 0
for z in range(10000):
    for x in range(1000):
        for c in range(100):
            total2 += 1
end = timer()
print('ASC', timedelta(seconds=end-start))