import sys
import numpy as np

def cut(test_array, n):
    global ans_0
    global ans_1
    flag = sum(test_array.sum(axis=0))
    if flag == n * n:
        ans_1 += 1
    elif flag == 0:
        ans_0 += 1
    else:
        mid = n//2
        cut(test_array[0:mid, 0:mid], mid)
        cut(test_array[mid:, 0:mid], mid)
        cut(test_array[0:mid, mid:], mid)
        cut(test_array[mid:, mid:], mid)


sys.stdin = open('input.txt')
n = int(input())
arrays = np.array([list(map(int, input().split())) for _ in range(n)])
ans_0 = 0
ans_1 = 0
cut(arrays, n)
print(ans_0)
print(ans_1)