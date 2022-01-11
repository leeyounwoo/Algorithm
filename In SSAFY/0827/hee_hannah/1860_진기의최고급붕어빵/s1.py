import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc), end=" ")
    quality, time, num_fish = map(int, input().split()) # 2명 살수잇고 2초마다 2개만들수잇
    people = list(map(int, input().split()))  # 3초 4초에 옴
    # 가장 먼저 사람이 첫번째 붕어빵 만들기 전에 오면 오류
    people.sort()
    if quality < len(people):
        print('impossible')
    else:
        # 붕어빵이 나오는 구간 안의 사람이 만들어진 붕어빵보다 많으면 틀림
        # 붕어빵 처음 만들어진 이후 등장
        # 한 구간안의 사람이 누적된 붕어빵보다 많거나 누적된게없어서 한 타임에 만들어지는 붕어빵보다 사람이 많을떼...
        n = 0
        acc = 0
        while len(people) != 0:
            n += 1
            if n % time == 0:
                acc += num_fish

            if n in people:
                people.pop(0)
                acc -= 1
                if len(people) != 0 and acc < 0:
                    print('impossible')
                    break
                elif len(people) == 0 and acc < 0:
                    print('impossible')
                    break
                elif len(people) == 0 and acc >= 0:
                    print('possible')
                    break



