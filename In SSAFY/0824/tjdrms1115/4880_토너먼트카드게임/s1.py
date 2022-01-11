import sys
sys.stdin = open('input.txt')


# 가위바위보 함수입니다.
# 1 : 가위, 2 : 바위, 3 : 보
def rsp(p1, rsp1, p2, rsp2):
    rsp1 -= 1
    rsp2 -= 1
    # 아래 조건이면 p2가 이기므로 p2의 정보를 반환합니다.
    if (rsp1+1) % 3 == rsp2:
        return [p2, rsp2+1]
    # 이외의 경우에는 p1의 정보를 반환합니다.
    else:
        return [p1, rsp1+1]


# 분할 정복 알고리즘입니다.
# 전체 배열 크기 N, 주어진 배열 card,
# 배열의 왼쪽 인덱스 l, 오른쪽 인덱스 r을 매개변수로 받습니다.
def divide_and_conquer(N, card, l, r):
    # 만약 r-l이 1보다 작으면(정상인 경우 0), 하위배열의 크기가 1이므로
    # 해당 인덱스와 값을 반환합니다.
    if r-l < 1:
        return l, card[l]
    else:
        # 중앙값을 설정합니다.
        m = (l+r)//2
        # 중앙값을 통해 두 부분으로 분할하여
        # 분할정복을 수행합니다.
        idx1, card1 = divide_and_conquer(N, card, l, m)
        idx2, card2 = divide_and_conquer(N, card, m+1, r)
        # 수행 결과를 통해 정복 합니다.
        # 이번 문제에서 정복은 가위바위보입니다.
        return rsp(idx1, card1, idx2, card2)


# 테스트 케이스를 입력받습니다.
T = int(input())

# 답을 저장할 리스트입니다.
answer = []
# 테스트 케이스 수 만큼 코드를 실행합니다.
for tc in range(1, T+1):

    # 전체 인원수 및 가위바위보 정보를 갖는 배열을 입력받습니다.
    N = int(input())
    card = list(map(int, input().split()))

    # 분할정복을 통해 최종 승리자를 찾습니다.
    result = divide_and_conquer(N, card, 0, N-1)

    # 승리한 사람의 번호를 출력합니다.
    result = result[0] + 1
    answer.append(result)

for tc in range(1, T + 1):
    print('#{} {}'.format(tc, answer[tc-1]))
