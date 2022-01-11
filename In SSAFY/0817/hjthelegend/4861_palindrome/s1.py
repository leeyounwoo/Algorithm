import sys
sys.stdin = open('input.txt')

def haemoon(words):
    for i in range(n): # 가로 갯수
        result = []
        for j in range(n - m + 1): # 회문의 크기
            if words[i][j:j+m] == words[i][j:j+m][::-1]:
                result.append(words[i][j:j+m])
                return result

    for i in range(n):
        result = []
        for j in range(n-m+1):
            sliced = ''
            for k in range(m):
                sliced += words[j+k][i]
            if sliced == sliced[::-1]:
                result.append(sliced)
                return result


t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    words = []
    for _ in range(n):
        words.append(list(input()))

    print(haemoon(words))