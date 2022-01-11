string = '2+3*4/5'
stack = []

for i in range(len(string)):
    char = string[i]
    if char in '+-*/':
        stack.append(char)
    else:
        print(char, end='')

while stack:
    print(stack.pop(), end='')