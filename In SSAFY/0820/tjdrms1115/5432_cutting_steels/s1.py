import sys
sys.stdin = open('input.txt')

T = int(input())

answer = []
for tc in range(1, T+1):
    # 처리할 문자열을 입력받습니다.
    string = input()
    # 현재 자를 수 있는 쇠막대기의 개수를 저장할 변수를 생성합니다.
    rodnum = 0
    # 총 쇠막대기 조각을 저장할 변수를 생성합니다.
    result = 0
    for i in range(1, len(string)):
        # '(('가 나오면 중첩된 쇠막대기 개수를 1개 올립니다.
        if string[i-1:i+1] == '((':
            rodnum += 1
        # '))'가 나오면 중첩된 쇠막대기 개수를 1개 내리고 쇠막대기 조각을 1개 더합니다.
        elif string[i-1:i+1] == '))':
            rodnum -= 1
            result += 1
        # '()'가 나오면 중첩된 쇠막대기 개수만큼 쇠막대기 조각을 1개 더합니다.
        elif string[i-1:i+1] == '()':
            result += rodnum

    # 결과를 출력합니다.
    answer.append(result)

for tc in range(1, T+1):
    print('#{} {}'.format(tc, answer[tc-1]))
