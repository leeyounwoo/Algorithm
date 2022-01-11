import sys
sys.stdin = open('input.txt')
# str2 안에 str1과 일치하는 부분이 있는지 찾으래
# str1 in str2
# str1  - N str 2 -M

T = int(input())
for tc in range(1, T + 1):
    str1 = input()
    str2 = input()
    N = len(str1)
    M = len(str2)

    # 첫 번째 방법
    # if str1 in str2:
    #     result = 1
    # else:
    #     result = 0

    # 두 번째 방법
    result = 0
    for i in range(M-N+1): # 7 -> 0 1 2 3 4 5 6
        if str1 == str2[i:i+N] : #[0:0+4] [1:1+4]
            result = 1

    print('#{} {}'.format(tc, result))

