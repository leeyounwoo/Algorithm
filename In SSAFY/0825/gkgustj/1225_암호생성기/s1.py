import sys
sys.stdin = open('input.txt')

def mkpassword(numbers):
    while True:
        for i in range(1, 6):
            temp = numbers.pop(0) - i

            if temp <= 0:
                numbers.append(0)
                return numbers

            numbers.append(temp)


for _ in range(10):
    t = int(input())
    numbers = list(map(int, input().split()))

    password = mkpassword(numbers)

    print('#{}'.format(t), end=' ')
    print(*password)