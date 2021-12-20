T = 1
while True:
    words = input()
    if words == '.':
        break
    stack = []
    for i in range(len(words)):
        if words[i] == '(':
            stack.append(words[i])
        elif words[i] == ')':
            if len(stack) and stack[-1] == '(':
                stack.pop(-1)
            else:
                print('no')
                break
        elif words[i] == '[':
            stack.append(words[i])
        elif words[i] == ']':
            if len(stack) and stack[-1] == '[':
                stack.pop(-1)
            else:
                print('no')
                break

    else:
        if len(stack):
            print('no')
        else:
            print('yes')