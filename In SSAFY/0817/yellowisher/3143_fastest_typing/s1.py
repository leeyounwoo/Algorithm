import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    A, B = input().split()
    cnt = 0  # 몇 번 반복됬는지 개수 세기 위한 변수

    for i in range(0, len(A) - len(B) + 1):  # 슬라이딩 윈도우 활용
        if A[i:i + len(B)] == B:
            cnt += 1  # 반복된 개수 카운트

    print("#{} {}".format(tc+1, len(A) - cnt * len(B) + cnt))