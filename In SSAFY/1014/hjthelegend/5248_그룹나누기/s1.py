import sys
sys.stdin = open('input.txt')
t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    # 1번부터 N번까지의 출석번호
    # M장의 신청서
    # 전체 몇개의 조가 생기는지?
    # union-find 알고리즘