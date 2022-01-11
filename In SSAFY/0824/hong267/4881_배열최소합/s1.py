import sys

sys.stdin = open('input.txt')

def min_sum(list1, n1, n2):
    global min_nums
    if n1 == n2:
        return 0
    for i in range(n1, n1+1):
        for j in range(n2):
            if

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    min_nums = []
    min_sum(puzzle, 0, N)
    print(min_nums)