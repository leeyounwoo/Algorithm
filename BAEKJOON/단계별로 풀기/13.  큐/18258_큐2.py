from collections import deque
import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
numbers = deque()
for _ in range(n):
    words = list(map(str, input().split()))
    if len(words) == 2:
        command, num = words[0], int(words[1])
        numbers.append(num)
    else:
        command = words[0]
        length = len(numbers)
        if command == "size":
            print(len(numbers))
        elif command == "empty":
            if length:
                print(0)
            else:
                print(1)
        else:
            if not length:
                print(-1)
            else:
                if command == "pop":
                    print(numbers.popleft())
                elif command == "front":
                    print(numbers[0])
                else:
                    print(numbers[-1])
