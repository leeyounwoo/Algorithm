brackets = input()
stack = []

for i in range(len(brackets)):
    if brackets[i] == '(':
        stack.append(brackets[i])
    else:
        if len(stack) == 0:
            print('짝이 안맞아유')
            exit()
        else:
            stack.pop()

if len(stack):
    print('뭔가 남았어유')
else:
    print('True')