import sys
sys.stdin = open('input.txt')

# 16진수 1자리 -> 2진수 4자리
# ex) 47FE -> 010.....

dict = {
    'A': 10, 'B': 11, 'C':12, 'D':13, 'E':14, 'F':15,
}

t = int(input())
for tc in range(1, t+1):
    n, number = input().split()

    answer = ''
    result = 0
    n = int(n)
    # 47FE
    for i in range(n):
        if number[i] in dict:
            result = int(dict[number[i]])
        else:
            result = int(number[i])

        for i in range(3, -1, -1): # 3, 2, 1, 0
            # 나머지 더하기
            answer += str(result // (2**i)) # 8, 4, 2, 1
            # result에 나머지 남기기
            result %= (2**i)

    print('#{} {}'.format(tc, answer))
