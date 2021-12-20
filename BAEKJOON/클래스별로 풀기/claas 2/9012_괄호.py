for T in range(int(input())):
    words = input()
    stack = []
    for i in range(len(words)):
        if words[i] == '(':
            stack.append(words[i])
        elif words[i] == ')':
            if len(stack) and stack[-1] == '(':
                stack.pop(-1)
            else:
                print('NO')
                break
    else:
        if len(stack):
            print('NO')
        else:
            print('YES')