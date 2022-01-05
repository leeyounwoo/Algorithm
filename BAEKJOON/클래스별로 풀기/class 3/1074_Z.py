import sys


def functionZ(n, start_i, end_i, start_j, end_j):
    global answer
    global r, c
    # print(n, answer)
    if n == 1:
        if r == start_i and c == start_j:
            return
        elif r == start_i and c == end_j:
            answer += 1
            return
        elif r == end_i and c == start_j:
            answer += 2
            return
        elif r == end_i and c == end_j:
            answer += 3
            return
    else:
        temp = (2 ** (n-1)) ** 2
        mid_i = start_i + (end_i - start_i) // 2
        mid_j = start_j + (end_j - start_j) // 2
        # print(start_i, end_i, start_j, end_j)
        # print('mid', mid_i, mid_j)
        if r <= mid_i and c <= mid_j:
            # print(1, start_i, mid_i, start_j, mid_j)
            functionZ(n-1, start_i, mid_i, start_j, mid_j)
        elif r <= mid_i and c > mid_j:
            answer += temp
            # print(2, start_i, mid_i, mid_j+1, end_j)
            functionZ(n-1, start_i, mid_i, mid_j+1, end_j)
        elif r > mid_i and c <= mid_j:
            answer += temp * 2
            # print(3, mid_i+1, end_i, start_j, mid_j)
            functionZ(n-1, mid_i+1, end_i, start_j, mid_j)
        else:
            answer += temp * 3
            # print(4, mid_i+1, end_i, mid_j+1, end_j)
            functionZ(n-1, mid_i+1, end_i, mid_j+1, end_j)



sys.stdin = open('input.txt')
n, r, c = map(int, input().split())
start_i, end_i, start_j, end_j = 0, 2**n-1, 0, 2**n-1
answer = 0
functionZ(n, start_i, end_i, start_j, end_j)
print(answer)