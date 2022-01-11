import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    data = input()
    #철봉 숫자
    steels_list = []
    result = 0

    for i in range(len(data)):
        # '(' 이면 리스트에 넣어주기
        if data[i] == '(':
            steels_list.append('(')
        else: # ')'
            # 가장 나중에 넣은것부터 빼주기
            steels_list.pop()

            # 레이저인 경우, 앞쪽에 있는 쇠막대기 개수만큼 더하기
            if data[i-1] == '(':
                result += len(steels_list)
            else:
                result += 1

    print('#{} {}'.format(tc, result))
