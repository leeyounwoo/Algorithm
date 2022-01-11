import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t+1):
    str1 = input()
    str2 = input()

    result = {}

    for x in str1:
        result[x] = 1

    answer = []
    for i in result: # str1에 있는 요소가 str2에 몇번 들어가는지 계산
        count = 0
        for j in str2:
            if i == j:
                count += 1
        answer.append(count)

    max_count = 0
    for i in answer: # 최댓값 계싼
        if max_count < i:
            max_count = i

    print('#{0} {1}'.format(tc, max_count))