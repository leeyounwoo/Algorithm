import sys

sys.stdin = open('input.txt')
n = int(input())
stairs = [int(input()) for _ in range(n)]
# 계단의 개수가 2개 이하인 경우, 모두 건널 수 있음
if n <= 2:
    print(sum(stairs))
# 계단의 개수가 3개 이상인 경우
else:
    # 첫 번째 인덱스: 이번 경우를 건너뜀 (이전 경우의 수에서 두 번째와 세 번째 중 최대값)
    # 두 번째 인덱스: 이전에 건너지 않고 이번이 처음으로 건너는 경우
    # 세 번째 인덱스: 이전에 건넜고 이번에 두 번째로 건너는 경우
    prev = [stairs[0], stairs[1], stairs[0] + stairs[1]]
    for i in range(2, n):
        ans = [max(prev[1], prev[2]), prev[0] + stairs[i], prev[1] + stairs[i]]
        prev = ans[:]
    print(max(ans[1], ans[2]))
