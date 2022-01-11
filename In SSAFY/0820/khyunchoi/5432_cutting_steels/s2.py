import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    brackets = input()
    cnt_list = []

    result = 0
    for i in range(len(brackets)-1):
        if brackets[i:i+2] == '((':          # 쇠막대기 생성
            cnt_list.append(1)
        elif brackets[i:i+2] == '()':        # 쇠막대기 자르기
            for j in range(len(cnt_list)):
                cnt_list[j] += 1
        elif brackets[i:i+2] == '))':        # 다 잘린 쇠막대기 pop
            result += cnt_list.pop()

    print('#{} {}'.format(tc, result))