string = '2+3*4/5'
stack = []

# 수식 읽는 부분
for i in range(len(string)):
    if (string[i] == '+' or string[i] == '-' or string[i] == '*' or string[i] == '/'):
        stack.append(string[i])
    else:
        print(string[i], end = "")

# stack에 남아있는 부분 pop
while stack:
    print(stack.pop(), end = "")