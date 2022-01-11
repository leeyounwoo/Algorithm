import sys
sys.stdin = open("input.txt")
T = int(input())
for tc in range(1, T+1):
    stack = []
    string_list = str(input())
    for i in range(0, len(string_list)):
        if string_list[i] not in stack or stack[-1] != string_list[i]:
            stack.append(string_list[i])
        else:
            if string_list[i] == stack[-1]:
                stack.pop()
    print('#{} {}'.format(tc, len(stack)))
