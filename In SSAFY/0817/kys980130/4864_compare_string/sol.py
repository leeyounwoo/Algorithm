T = int(input())
for tc in range():
    s1 = input()
    s2 = input()

    # s1의 길이만큼 슬라이딩 윈도우 생성
    window = len(s1)

    # s1의 길이만큼 하나씩 확인
    for i in range(len(s2)-window+1):
        # 일치하면
        if s1 == s2[i:i+window]:
            result = 1
            break

    print('#{} {}'.format(tc, result))
