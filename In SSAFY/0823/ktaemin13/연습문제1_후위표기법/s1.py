# 중위 표기법 => 후위표기법 변환 문제
string = '2 + 3 * 4 / 5 '

stack = []


# 수식을 읽는 부분
for i in range(len(string)):
    char = string[i]
    if (char == '+' or char == '-'
        or char == '*' or char == '/'):
        stack.append(char)
    else:
        print(char, end='')


# stack 에 남아있는 부분을 pop
while stack:
    print(stack.pop(), end='')
