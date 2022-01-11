import sys
sys.stdin = open('input.txt')

# 팰린드롬 여부를 확인합니다. 파이썬은 확인이 굉장히 쉽습니다.
def check_pal(word):
    if word == word[::-1]:
        return True
    return False

# 가장 긴 회문 문자열을 찾아 그 길이를 반환합니다.
def find_pal_max(N, letters):

    # i방향과 j방향으로 한 번씩 탐색을 합니다.
    max_len = 0
    for i in range(N):
        for j in range(N):
            # i방향 탐색입니다. 현재 위치를 기준으로 끝까지 인덱스를 옮겨가며 회문을 확인합니다.
            for k in range(i, N):
                # 탐색할 회문을 만듧니다.
                tempword = ''
                for l in range(i, k+1):
                    tempword += letters[l][j]
                # 만약에 회문이라면 현재 저장된 길이와 비교합니다.
                if check_pal(tempword):
                    if max_len < len(tempword):
                        max_len = len(tempword)
            # j방향 탐색입니다. 현재 위치를 기준으로 끝까지 인덱스를 옮겨가며 회문을 확인합니다.
            for k in range(j, N):
                # 탐색할 회문을 만듧니다.
                tempword = letters[i][j:k+1]
                # 만약에 회문이라면 현재 저장된 길이와 비교합니다.
                if check_pal(tempword):
                    if max_len < len(tempword):
                        max_len = len(tempword)
    # 찾은 최대 길이를 반환합니다.
    return max_len


# T = int(input())
T = 10

answer = []
for tc in range(1, T+1):

    # 테스트 케이스입니다. 쓰지 않습니다.
    testcase = int(input())
    # 주어진 판의 크기입니다. 고정값입니다.
    N = 100

    # 문자열의 배열을 입력받습니다.
    letters = [input() for _ in range(N)]

    # 최대 회문 길이를 찾습니다.
    result = find_pal_max(N, letters)
    # 결과를 출력합니다.
    answer.append(result)

for tc in range(1, T+1):
    print('#{0} {1}'.format(tc, answer[tc-1]))