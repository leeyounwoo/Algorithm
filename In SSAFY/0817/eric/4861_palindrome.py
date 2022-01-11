def scan_col(words, M):
    result = ''
    for x in range(len(words[0])):
        for y in range(len(words)-M+1):
            sliced = ''
            for dy in range(M):
                sliced += words[y+dy][x]
            if is_pal(sliced):
                return sliced
    return result

def scan_row(words, M):
    result = ''
    for y in range(len(words)):
        for x in range(len(words[y])-M+1):
            sliced = words[y][x:M+x]
            if is_pal(sliced):
                return sliced
    return result

def is_pal(word):
    if word == word[::-1]:
        return True
    return False

t = int(input())

for tc in range(1, t+1):
    N, M = map(int, input().split())
    words = [input() for _ in range(N)]

    # x축 확인
    result_x = scan_row(words, M)
    # y축 확인
    result_y = scan_col(words, M)

    result = ''
    if result_x:
        result = result_x
    else:
        result = result_y
    print(f'#{tc} {result}')