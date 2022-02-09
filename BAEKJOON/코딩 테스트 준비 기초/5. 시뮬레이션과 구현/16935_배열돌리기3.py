import sys

def input():
    return sys.stdin.readline().rstrip()


def function1():
    for i in range(len(array)//2):
        array[i], array[len(array)-i-1] = array[len(array)-i-1], array[i]


def function2():
    for i in range(len(array)):
        array[i].reverse()


def function3():
    global n, m
    new_array = [[] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            new_array[i].append(array[n-1-j][i])
    n, m = m, n
    return new_array

def function4():
    global n, m
    new_array = [[] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            new_array[i].append(array[j][m-1-i])
    n, m = m, n
    return new_array


def function5(n, m):
    group1 = [[] for _ in range(n//2)]
    group2 = [[] for _ in range(n//2)]
    group3 = [[] for _ in range(n//2)]
    group4 = [[] for _ in range(n//2)]
    for i in range(n):
        for j in range(m):
            if i < n//2 and j < m//2:
                group1[i].append(array[i][j])
            if i < n // 2 and j >= m // 2:
                group2[i].append(array[i][j])
            if i >= n // 2 and j < m // 2:
                group4[i-n//2].append(array[i][j])
            if i >= n // 2 and j >= m // 2:
                group3[i-n//2].append(array[i][j])

    new_array = [[] for _ in range(n)]
    for i in range(n):
        if i < n//2:
            group4[i].extend(group1[i])
            new_array[i] = group4[i]
        else:
            group3[i-n//2].extend(group2[i-n//2])
            new_array[i] = group3[i-n//2]

    return new_array



def function6(n, m):
    group1 = [[] for _ in range(n // 2)]
    group2 = [[] for _ in range(n // 2)]
    group3 = [[] for _ in range(n // 2)]
    group4 = [[] for _ in range(n // 2)]
    for i in range(n):
        for j in range(m):
            if i < n // 2 and j < m // 2:
                group1[i].append(array[i][j])
            if i < n // 2 and j >= m // 2:
                group2[i].append(array[i][j])
            if i >= n // 2 and j < m // 2:
                group4[i - n // 2].append(array[i][j])
            if i >= n // 2 and j >= m // 2:
                group3[i - n // 2].append(array[i][j])

    new_array = [[] for _ in range(n)]
    for i in range(n):
        if i < n // 2:
            group2[i].extend(group3[i])
            new_array[i] = group2[i]
        else:
            group1[i - n // 2].extend(group4[i - n // 2])
            new_array[i] = group1[i - n // 2]
    return new_array


sys.stdin = open('input.txt')
n, m, r = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()))
for i in range(len(commands)):
    command = commands[i]
    if command == 1:
        function1()
    elif command == 2:
        function2()
    elif command == 3:
        array = function3()
    elif command == 4:
        array = function4()
    elif command == 5:
        array = function5(n, m)
    elif command == 6:
        array = function6(n, m)



for i in range(len(array)):
    for j in range(len(array[i])):
        print(array[i][j], end=' ')
    print()
