import sys
sys.stdin = open('input.txt')


def babygin(arr):
    for i in range(len(arr) - 2):
        if arr[i] > 0:
            if arr[i] >= 3:
                return True
            elif arr[i + 1] > 0 and arr[i + 2] > 0:
                return True
    if arr[-2] >= 3:
        return True
    if arr[-1] >= 3:
        return True

    return False


T = int(input())

answer = []
for tc in range(1, T + 1):

    input_card = list(map(int, input().split()))

    person1 = [0] * 10
    person2 = [0] * 10
    people = [person1, person2]

    result = 0
    for i in range(len(input_card)):
        target = people[i % 2]
        target[input_card[i]] += 1
        if babygin(target):
            result = (i % 2) + 1
            break

    # print(f'#{tc} {result}')
    answer.append(result)

for tc in range(1, T + 1):
    print(f'#{tc} {answer[tc-1]}')
