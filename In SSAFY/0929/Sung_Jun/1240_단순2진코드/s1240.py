import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    case = [list(map(int, input())) for _ in range(N)]
    code = [[0, 0, 0, 1, 1, 0, 1],
            [0, 0, 1, 1, 0, 0, 1],
            [0, 0, 1, 0, 0, 1, 1],
            [0, 1, 1, 1, 1, 0, 1],
            [0, 1, 0, 0, 0, 1, 1],
            [0, 1, 1, 0, 0, 0, 1],
            [0, 1, 0, 1, 1, 1, 1],
            [0, 1, 1, 1, 0, 1, 1],
            [0, 1, 1, 0, 1, 1, 1],
            [0, 0, 0, 1, 0, 1, 1],
            ]

    num_list = []
    flag = 0
    for case_num in case:
        for i in range(M-1, -1, -1):
            if case_num[i] == 1:
                for j in range(i, i-56, -7):
                    num_list.append(case_num[j-6:j+1])
                flag = 1
                break
        if flag == 1:
            num_list = num_list[::-1]
            break

    result = []
    for num in range(8):
        for j in range(10):
            if code[j] == num_list[num]:
                result.append(j)
                break

    add_sum = 0
    even_sum = 0
    for number in range(7):
        if number % 2:
            add_sum += result[number]
        else:
            even_sum += result[number]

    sum_num = 0
    if not (add_sum + even_sum*3 + result[-1]) % 10:
        sum_num = add_sum + even_sum + result[-1]

    print('#{} {}'.format(tc+1, sum_num))



'''
1. 들어온 배열을 검색하여 반복되는 패턴 찾기
    암호 코드는 8개의 숫자로 구성 되어있다? 56개의 문자열이 필요하다는 소리
    패턴 중 마지막 자리가 0인 숫자는 존재하지 않다. 즉 뒤부터 탐색하되 1을 찾고 8개씩 탐색
    
2. 패턴을 찾았으면 암호 변환코드를 통해 숫자로 변환 변환식에 대입하여 검증
3. 맞다면 단순 숫자들의 합을 구하기
'''
