
string = input()

# 후위 표기식으로 바꾸기
stack = []
result = []

for s in string:
    if s == '+':
        while stack:
            result.append(stack.pop())
        stack.append(s)
    elif s == '*':
        stack.append(s)
    else:
        result.append(s)

while stack:
    result.append(stack.pop())

print(result)
