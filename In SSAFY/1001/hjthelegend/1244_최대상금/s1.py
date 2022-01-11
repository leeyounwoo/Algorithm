import sys
sys.stdin = open('input.txt')

# 32888 교환횟수 2회
# -> 82838
# -> 88832
# 최대 값을 가져와야하는데
# 교환 횟수만큼 반드시 교환해야함.

def swapper(number):
    for i in range(len(number)):
        if number[i] != max(number): # 가장 앞부터 최대 숫자가 아니라면
            number[i], number[number.index(max(number))] = number[number.index(max(number))], number[i]
            print(number[i])
            print(number[number.index(max(number))])
            return number

t = int(input())
for tc in range(1, t+1):
    number, n = input().split()
    number = list(map(int, number))
    n = int(n)
    for _ in range(n):
        number = swapper(number)

    print(number)


def dfs(count):
    global answer
    if not count:
        temp = int(''.join(values))
        if answer < temp:
            answer = temp
        return
    for i in range(length):
        for j in range(i + 1, length):
            values[i], values[j] = values[j], values[i]
            temp_key = ''.join(values)
            if visited.get((temp_key, count - 1), 1):
                visited[(temp_key, count - 1)] = 0
                dfs(count - 1)
            values[i], values[j] = values[j], values[i]


for t in range(int(input())):
    answer = -1
    value, change = input().split()
    values = list(value)
    change = int(change)
    length = len(values)
    visited = {}
    dfs(change)
    print('#{} {}'.format(t + 1, answer))