import sys

sys.stdin = open('input.txt')
n = int(sys.stdin.readline())
stack = []
for i in range(n):
    command = str(sys.stdin.readline())
    if command[0:2] == 'pu':
        stack.append(list(command.split())[1])
    elif command[0:2] == 'po':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command[0:2] == 'si':
        print(len(stack))
    elif command[0:2] == 'em':
        if stack:
            print(0)
        else:
            print(1)
    elif command[0:2] == 'to':
        if stack:
            print(stack[-1])
        else:
            print(-1)
