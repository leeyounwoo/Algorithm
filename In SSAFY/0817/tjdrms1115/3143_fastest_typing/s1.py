import sys
sys.stdin = open('input.txt')

# 틀렸을 때 어느 위치로 갈 것인지 위치별로 결정하는 함수입니다.
def create_wheretogo(word):

    length = len(word)
    result = [0] * length
    # 모든 위치에 대해서 이전 위치를 결정합니다.
    for i in range(length):
        count = 1
        for j in range(i+1, length):
            # 자신의 바로 뒤에 오는 자기와 같은 문자의 위치가
            # 자기 위치에서 틀렸을 때 돌아갈 위치입니다.
            if word[i] == word[j]:
                result[i] = count
                break
            count += 1
    return result

# 패턴을 체크합니다. word가 체크할 패턴, sentence가 체크당할 문자열입니다.
def boyer_moore_KMP(word, sentence):
    w_len = len(word)
    s_len = len(sentence)
    # 패턴이 존재하는 위치를 저장할 리스트입니다.
    occurences = []

    # 우선 입력받은 패턴에 대해 돌아갈 위치를 지정할 배열을 만듧니다.
    idx_to_go = create_wheretogo(word)

    s_idx = 0
    count = 0
    # 보이어-무어 알고리즘으로 패턴을 찾습니다.
    while s_idx + w_len - 1 < s_len:
        temp_idx = w_len - 1
        i = w_len - 1
        while i >= 0:
            if word[i] == sentence[s_idx + temp_idx]:
                temp_idx -= 1
            # 패턴이 맞지 않으면, 마치 KMP알고리즘처럼 돌아갈 위치를 미리 저장해놓은 배열에서 찾아 돌아갑니다.
            elif idx_to_go[temp_idx] != 0:
                temp_idx += idx_to_go[temp_idx]
                continue
            i -= 1

        # temp_idx가 -1이라면, 패턴 길이만큼 -1이 수행되었다는 의미이기 때문에 패턴이 맞았다는 의미입니다.
        # 패턴의 위치를 저장하고, 변수를 초기화합니다.
        if temp_idx == -1:
            occurences.append(s_idx)
            count += 1
            temp_idx = w_len - 1
        s_idx += temp_idx + 1

    # result = s_len - ((w_len - 1) * count)
    # return result
    # 패턴의 위치를 저장한 배열을 반환합니다.
    return occurences


T = int(input())

answer = []
for tc in range(1, T + 1):

    # 문자열과 패턴을 입력받습니다.
    sentence, word = input().split()

    # 패턴이 들어있는 위치들을 찾습니다.
    result1 = boyer_moore_KMP(word, sentence)

    # 찾은 정보를 바탕으로 최소 횟수를 계산합니다.
    a = len(sentence) - ((len(word) - 1) * len(result1))

    # 결과를 출력합니다.
    answer.append(a)

for tc in range(1, T+1):
    print('#{0} {1}'.format(tc, answer[tc-1]))
