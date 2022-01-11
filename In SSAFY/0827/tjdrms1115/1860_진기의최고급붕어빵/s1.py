import sys
sys.stdin = open('input.txt')

# 테스트 케이스의 개수를 입력받습니다.
T = int(input())

# 테스트 케이스만큼 코드를 실행하고 결과를 저장합니다.
answer = []
for tc in range(1, T+1):

    # 입력값을 입력받습니다.
    N, M, K = map(int, input().split())
    people = list(map(int, input().split()))

    # 사람들을 오는 순서대로 처리하기 위해 정렬을 한 번 해줍니다.
    people.sort()

    # 일단 가능하다고 가정하고 시작합니다.
    result = 'Possible'
    # 붕어빵이 저장될 큐입니다.
    breadfish = []
    # 시간을 저장할 변수입니다.
    time = 0
    # break를 두번 쓰기 싫어서 try-except구문으로 처리했습니다.
    try:
        # 올 사람이 남아있는 동안 반복합니다.
        while people:

            # 현재 시간에 올 사람이 있다면
            while len(people) > 0 and people[0] == time:
                # 붕어빵하나를 주고 사람 한명을 보냅니다.
                # 붕어빵이 없으면 IndexError가 나고,
                # except 구문에서 처리합니다.
                breadfish.pop(0)
                people.pop(0)

            # 시간이 지납니다.
            time += 1
            # 붕어빵이 나올 시간이 되면 붕어빵을 큐에 추가합니다.
            if time % M == 0:
                for _ in range(K):
                    breadfish.append(1)
    # 위에서 붕어빵이 없을 때 사람이 왔기 때문에
    # 결과에 불가능하다고 저장합니다.
    except IndexError:
        result = 'Impossible'

    # 결과를 출력합니다.
    answer.append(result)

for tc in range(1, T+1):
    print('#{} {}'.format(tc, answer[tc-1]))
