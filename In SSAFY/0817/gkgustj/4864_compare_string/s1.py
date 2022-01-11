import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    str1 = input()
    str2 = input()

    # 고지식한 패턴 검색 알고리즘
    i = 0
    j = 0
    result = 0

    while j <= len(str2)-len(str1):
        if str1[i] == str2[j]:
            while i < len(str1)-1:
                i += 1
                j += 1
                if str1[i] != str2[j]:
                    i = 0
                    j +=1
                    break
                # 위에서 안걸러지고 넘어왔으므로 i가 len(str1)-1이 될 때까지
                # 모든 문자열이 일치
                elif i == len(str1)-1:
                    result = 1
                    break
        else:
            j += 1

    print('#{} {}'.format(t, result))