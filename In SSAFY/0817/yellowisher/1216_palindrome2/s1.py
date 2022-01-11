import sys
sys.stdin = open('input.txt')

def is_palindrome(arr):
    max_num = 0
    for i in range(100):
        for j in range(100):
            for k in range(100):
                pal = arr[i][j:j+k]
                if pal == pal[::-1]:
                    if max_num < len(pal):
                        max_num = len(pal)
    return max_num

for _ in range(10):
    tc = int(input())

    garo = []   # 가로 배열
    for i in range(100):
        garo.append(input())
    result1 = is_palindrome(garo)

    sero = []   # 세로 배열
    for i in range(100):
        new_word = ''
        for j in range(100):
            new_word += garo[j][i]
        sero.append(new_word)
    result2 = is_palindrome(sero)

    print("#{} {}".format(tc, max(result1, result2)))
