import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()


sys.stdin = open('input.txt')
for T in range(int(input())):
    func = list(input())
    n = int(input())
    strings = input()

    array = deque(strings[1:-1].split(','))
    flag = True
    for i in range(len(func)):
        if func[i] == 'R':
            if flag:
                flag = False
            else:
                flag = True

        else:
            if len(array) <= 0 or array[0] == '':
                print('error')
                break
            else:
                if flag:
                    array.popleft()
                else:
                    array.pop()

    else:
        if not flag:
            array.reverse()
        print('[', end='')
        for i in range(len(array)):
            print(array[i], end='')
            if i != len(array)-1:
                print('', end=',')
        print(']')
