import sys
sys.stdin = open('input.txt')

def movement(cycle,number):
    for _ in range(cycle):
        t = number.pop(0)
        number.append(t)
    return number[0]


T = int(input())
for tc in range(1,T+1):
    numbers, cycle = map(int,input().split())
    number = list(map(int, input().split()))
    print('#{} {}'.format(tc,movement(cycle,number)))