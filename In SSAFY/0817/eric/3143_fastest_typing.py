def make_skip_list(pattern):
    skip_list = [0]*len(pattern)
    for idx, char in enumerate(pattern):
        skip_list[idx] = len(pattern) - idx - 1
    return skip_list

# 나쁜 문자 규칙(bad character rule) 적용
def bad_char_rule(pattern, mismatched_idx, mismatched_char):
    skip_list = make_skip_list(pattern)
    shift = 0
    for i in range(len(pattern)-1, -1, -1):
        if pattern[i] == mismatched_char:
            shift = skip_list[i]
            break
    else:
        shift = len(pattern)
    return shift

# 보이어 무어 패턴 매칭
def boyer_moore(string, pattern):
    i = 0 # 현재 패턴의 위치
    occurences = [] # 패턴이 출현하는 위치 저장
    while i <= len(string) - len(pattern):
        shift = 1
        mismatched = False
        # 오른쪽에서 왼쪽으로 패턴 매칭 시작
        for j in range(len(pattern)-1, -1, -1):
            if string[i+j] != pattern[j]:
                shift_bc = bad_char_rule(pattern, j, string[i+j])
                shift = max(shift, shift_bc)
                mismatched = True
                break
        if not mismatched:
            shift = len(pattern)
            occurences.append(i)
        i += shift
    return occurences

T = int(input())

answer = []
for tc in range(1, T + 1):
    sentence, word = input().split()

    result = boyer_moore(sentence, word)

    result = len(result) + len(sentence) - (len(result) * len(word))
    print(f'#{tc} {result}')