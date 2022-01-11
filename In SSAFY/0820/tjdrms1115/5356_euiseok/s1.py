import sys
sys.stdin = open('input.txt')

T = int(input())

answer = []
for tc in range(1, T + 1):

    # 문자열들을 입력받아서 한 배열 안에 저장합니다.
    words = []
    for _ in range(5):
        words.append(input())

    # 세로로 읽은 결과를 저장하기 위해 result 변수를 생성합니다.
    result = ''
    idx = 0
    while words:

        # idx에 해당하는 위치의 문자열을 차례대로 result에 추가합니다.
        for i in words:
            result += i[idx]
        # idx를 다음 위치로 옮깁니다.
        idx += 1

        # idx가 자기 길이 바깥을 가리키고 있는 단어들을 리스트에서 제거합니다.
        idx2 = 0
        while idx2 < len(words):
            if idx < len(words[idx2]):
                idx2 += 1
            else:
                words.pop(idx2)

    # 결과를 출력합니다.
    answer.append(result)

for tc in range(1, T + 1):
    print('#{} {}'.format(tc, answer[tc - 1]))
