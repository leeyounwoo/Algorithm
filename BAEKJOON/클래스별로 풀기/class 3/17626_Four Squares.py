import math

n = int(input())
d = [0] * (n+1)
d[1] = 1
for i in range(2, n+1):
    if i == int(math.sqrt(i)) ** 2:
        d[i] = 1
    else:
        d[i] = i

for i in range(2, n+1):
    for j in range(1, int(math.sqrt(i)) + 1):
        d[i] = min(d[i], d[j*j] + d[i - j * j])
print(d[n])