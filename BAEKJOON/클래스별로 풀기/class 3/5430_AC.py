import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()


sys.stdin = open('input.txt')
for T in range(int(input())):
    func = list(input())
    # print(func)
    n = int(input())
    strings = input()

    array = deque(strings[1:-1].split(','))
    # print(T, array)
    for i in range(len(func)):
        # print(func[i])
        if func[i] == 'R':
            array.reverse()
            # print(array)
        else:
            # print('123')
            if len(array) <= 0 or array[0] == '':
                # print('45')
                print('error')
                break
            else:
                array.popleft()
    else:
        print('[', end='')
        for i in range(len(array)):
            print(array[i], end='')
            if i != len(array)-1:
                print('', end=',')
        print(']')
