# 중위표기법 - > 후위표기법 변환 문제

string = '2+3*4/5'

stack = []

for i in range(len(string)):
    char = string[i]
    if (char == '+' or char == '-' or char == '*' or char == '/'):
        stack.append(char)
    else:
        print(char, end="")

# stack에 남아있는 부분 pop
while stack:
    print(stack.pop(), end="")