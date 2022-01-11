string = '(6+5*(2-8)/2)'

isp = {'(' : 0, '+' : 1, '-' : 1,
       '*' : 2, '/' : 2}
icp = {'(' : 3, '+' : 1, '-' : 1,
       '*' : 2, '/' : 2}

stack = []
i = 0
while i < len(string):
    if string[i].isnumeric():
        print(string[i], end='')
    else:
        if not stack:
            stack.append(string[i])

        elif string[i] == ')':
            while stack[-1] != '(':
                print(stack.pop(), end='')
                i += 1
            stack.pop()

        if i >= len(string):
            break

        while icp[string[i]] <= isp[stack[-1]]:
            print(stack.pop(), end='')

        if i != 0 and icp[string[i]] > isp[stack[-1]]:
            stack.append(string[i])

    i += 1

if stack:
    print(stack.pop(), end='')