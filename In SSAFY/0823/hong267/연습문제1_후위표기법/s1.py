string = '2+3*4/5'

stack = []
i = 0
while i < len(string):
    if string[i].isdigit():
        print(string[i], end='')
        i += 1
    else:
        stack.append(string[i])
        i += 1

for _ in range(len(stack)):
    print(stack.pop(), end='')
