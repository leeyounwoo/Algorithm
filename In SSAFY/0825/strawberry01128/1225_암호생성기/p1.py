import sys
sys.stdin = open('input.txt')

def cycle(num):
    i = 1
    while True:
        if i > 5:
            i = 1
        t = num.pop(0) - i
        if t <= 0:
            num.append(0)
            break
        num.append(t)
        i += 1
    return num

for tc in range(1, 11):
    tcc = int(input())
    number = (list(map(int, input().split())))
    print('#{}'.format(tc),end=" ")
    for i in cycle(number):
        print(i,end=" ")
    print()