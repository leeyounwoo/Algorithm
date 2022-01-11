import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    a = input()
    print(len(a))
    count = 0
    for i in range(1, len(a)+1):
        if i+1 <= len(a) and a[i] == '(' and a[i+1] == ')':
            count += 1
    print('#{} {}'.format(tc, len(a)-count))
