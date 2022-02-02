import sys

def input():
    return sys.stdin.readline().rstrip()


sys.stdin = open('input.txt')
while True:
    try:
        n = int(input())
        number_str = '1'
        while True:
            number = int(number_str)
            if not number % n:
                print(len(number_str))
                break
            else:
                number_str += '1'

    except:
        break