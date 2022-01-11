import sys
sys.stdin = open('input.txt')


def forth(char):
    stack = []
    for check in char:
        if check == '.':
            if len(stack) == 1:
                return stack[0]
            else:
                return 'error'
        if check.isdigit():
            stack.append(int(check))
        else:
            try:
                a = stack.pop()
                b = stack.pop()
                if check == '+':
                    stack.append(b + a)
                elif check == '*':
                    stack.append(b * a)
                elif check == '/':
                    stack.append(b // a)
                elif check == '-':
                    stack.append(b - a)
                elif check == '**':
                    stack.append(b ** a)
            except:
                return 'error'


T = int(input())
for tc in range(T):
    char = list(map(str, input().split()))
    print('#{} {}'.format(tc+1, forth(char)))

# T = int(input())
# for tc in range(T):
#     char = list(map(str, input().split()))
#     print(char)
#
#     stack = []
#     for check in char:
#         if c





