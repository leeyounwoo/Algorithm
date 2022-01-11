string = '2+3*4/5'
stack = []
operation = []
order = []
level = {'-': 1, '+': 1, '*': 2, '/': 2}
numbers = [str(i) for i in range(10)]
for i in range(len(string)):
    if string[i] in numbers:
        stack.append(int(string[i]))
    else:
        ord_level = level[string[i]]
        if len(order) == 0 or order[len(order)-1] <= ord_level:
            operation.append(string[i])
for i in range(len(operation)):
    stack.append(operation.pop())
print(stack)