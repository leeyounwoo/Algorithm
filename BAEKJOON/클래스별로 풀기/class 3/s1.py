import sys

def cut(test_array, n):
    global ans_0
    global ans_1
    flag = 0
    for i in range(len(test_array)):
        flag += sum(test_array[i])
    if flag == n * n:
        ans_1 += 1
    elif flag == 0:
        ans_0 += 1
    else:
        array_1 = []
        array_2 = []
        array_3 = []
        array_4 = []
        mid = n//2
        for i in range(len(test_array)):
            if i < mid:
                array_1.append(test_array[i][:mid])
                array_2.append(test_array[i][mid:])
            else:
                array_3.append(test_array[i][:mid])
                array_4.append(test_array[i][mid:])

        cut(array_1, mid)
        cut(array_2, mid)
        cut(array_3, mid)
        cut(array_4, mid)


sys.stdin = open('input.txt')
n = int(input())
arrays = [list(map(int, input().split())) for _ in range(n)]
ans_0 = 0
ans_1 = 0
cut(arrays, n)
print(ans_0)
print(ans_1)