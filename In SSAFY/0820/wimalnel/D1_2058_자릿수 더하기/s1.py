N = int(input())

a = N // 1000 % 10
b = (N // 100) % 10
c = (N // 10) % 10
d = (N // 1) % 10

print(a+b+c+d)
