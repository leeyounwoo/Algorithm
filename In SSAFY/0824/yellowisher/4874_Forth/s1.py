import sys
sys.stdin = open('input.txt')

def calculate(tokens):
    stack = []
    try:
        for token in tokens:
            if token == '+':
                stack.append(stack.pop()+stack.pop())
            elif token == '-':
                stack.append(-(stack.pop()-stack.pop()))
            elif token == '*':
                stack.append(stack.pop()*stack.pop())
            elif token == '/':
                div = stack.pop()
                stack.append(stack.pop()//div)
            elif token == '.':
                ans = stack.pop()
                if len(stack) != 0:
                    return "error"
                return ans
            else:
                stack.append(int(token))
    except:
        return "error"

T = int(input())
for tc in range(T):
    arr = list(input().split())
    result = calculate(arr)
    print("#{} {}".format(tc + 1, result))