def push(item):
    stack.append(item)

def pop():
    if len(stack) == 0:
        print('스택이 비어있습니다!')
        return
    return stack.pop()

stack = []
string = input()
for char in string:
    if char == '(':
        push(char)
    else:
        if len(stack) == 0:
            print("오류")
            break
        pop()
if len(stack) != 0:
    print("오류")