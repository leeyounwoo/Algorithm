import sys
sys.stdin = open('input.txt')

T = int(input())

def is_palindrome(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr[i])-M+1):
            pal = arr[i][j:j+M]
            if pal == pal[::-1]: # 거꾸로 비교
                print("#{} {}".format(tc + 1, pal))

for tc in range(T):
    garo = []   # 가로 배열
    N, M = map(int, input().split())
    for i in range(N):
        garo.append(input())
    # print(garo)
    is_palindrome(garo)

    sero = []   # 세로 배열
    for i in range(N):
        new_word = ''
        for j in range(N):
            new_word += garo[j][i]
        sero.append(new_word)
    # print(sero)
    is_palindrome(sero)

