import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, time, make = map(int, input().split())
    peoples = list(map(int, input().split()))

    fish_bread = [0] * (max(peoples)+1)
    for i in range(time, len(fish_bread), time):
        fish_bread[i] = make

    result = 'Possible'
    for people in peoples:
        for i in range(people, -1, -1):
            if fish_bread[i]:
                fish_bread[i] -= 1
                break
        else:
            result = 'Impossible'

    print('#{} {}'.format(tc, result))