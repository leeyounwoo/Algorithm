import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    string = input()
    stack = []
    backward = []
    for i in len(string):
        if string[i] == '*':
            stack.append(string[i])
        elif string[i] == '+':

        else:
            backward.append(string[i])


