import sys
n = int(input())
list_n = []
for _ in range(n):
    temp = []
    age, name = map(str, sys.stdin.readline().split())
    age = int(age)
    list_n.append([age, name])
list_n.sort(key=lambda X: X[0])
for i in range(n):
    print('{} {}'.format(list_n[i][0], list_n[i][1]))