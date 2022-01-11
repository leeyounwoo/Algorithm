string = '2+3*4/5'
stack = []

# 수식을 읽는 부분
for i in range(len(string)):
    if string[i] in ('+', '-', '*', '/'):
        stack.append(string[i])
    else:
        print(string[i], end='')

# stack에 남아있는 부분 pop
while stack:
    print(stack.pop(), end='')