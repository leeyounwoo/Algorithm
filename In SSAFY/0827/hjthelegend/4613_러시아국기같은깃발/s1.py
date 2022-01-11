import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    for _ in range(n):
        s = input()

    # n이 4였을때 첫줄 W 둘째줄 B 셋,넷째줄 R
    # 첫쨰 W과 마지막 R은 고정,