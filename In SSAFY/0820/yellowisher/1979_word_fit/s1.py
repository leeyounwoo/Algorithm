import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    stack = [[] for _ in range(15)]
    max_num = 0

    for i in range(5):
        s = list(input())
        max_num = max(len(s), max_num)

        for j in range(len(s)):
            stack[j].append(s[j])

    print("#{} ".format(tc + 1), end = '')
    for i in range(max_num):
        print(''.join(stack[i]), end = '')
    print()
