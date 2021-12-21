import sys

sys.stdin = open('input.txt')
n = int(sys.stdin.readline())
queue = []
for i in range(n):
    command = str(sys.stdin.readline())
    if command[0:2] == 'pu':
        queue.append(int(list(command.split())[1]))
    elif command[0:2] == 'po':
        if queue:
            print(queue.pop(0))
        else:
            print(-1)
    elif command[0:2] == 'si':
        print(len(queue))
    elif command[0:2] == 'em':
        if queue:
            print(0)
        else:
            print(1)
    elif command[0:2] == 'fr':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif command[0:2] == 'ba':
        if queue:
            print(queue[-1])
        else:
            print(-1)