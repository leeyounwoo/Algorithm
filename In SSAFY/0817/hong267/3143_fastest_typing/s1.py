import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    A, B = input().split()
    a = len(A) # banana  asakusa
    b = len(B) # bana    sa

    result = 0
    i = 0
    while i < a:
        if A[i:i+b] == B:
            result += 1
            i = i + b # 인덱스를 검사한 범위 다음으로 옮김
        else:
            i += 1 # B 문자열이 아니면 인덱스 하나씩 증가
            result += 1

    print('#{0} {1}'.format(tc, result))
