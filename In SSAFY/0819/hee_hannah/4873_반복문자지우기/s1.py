import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    a = list(input())
    stack = []
    for i in range(len(a)):
        if i+1 <= len(a)-1 and a[i] != a[i+1]:
            stack.append(a[i])
        elif i+1 <= len(a)-1 and a[i] == a[i+1]:
            a.pop()
    print(stack)


