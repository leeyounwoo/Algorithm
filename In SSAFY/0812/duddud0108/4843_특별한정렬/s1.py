import sys

sys.stdin = open('input.txt')

def selection_sort(x):
    for size in reversed(range(len(x))):
        max_i = 0
        for i in range(1, 1+size):
            if x[i] > x[max_i]:
                max_i = i
        x[max_i], x[size] = x[size], x[max_i]

T = int(input())
for tc in range(T):
    N = int(input())
    num_list = list(map(int, input().split()))
    selection_sort(num_list)

    print('#{0}'.format(tc+1), end=' ')
    i = 0
    while i < 10:
        if i % 2:
            print(num_list.pop(0), end=' ')
        else:
            print(num_list.pop(), end=' ')
        i += 1
    print()



