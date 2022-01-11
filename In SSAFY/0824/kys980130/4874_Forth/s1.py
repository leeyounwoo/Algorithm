import sys
sys.stdin = open("input.txt")
T = int(input())
for tc in range(1, T+1):
    forth = list(input().split())
    num = []
    try:
        for char in forth:
            if char == '.':
                result = num.pop()
                if len(num) != 0:
                    result = 'error'
                break
            elif char == '/':
                num2 = int(num.pop())
                num1 = int(num.pop())
                result = int(num1/num2)
                num.append(result)
            elif char == '*':
                num2 = int(num.pop())
                num1 = int(num.pop())
                result = num1*num2
                num.append(result)
            elif char == '+':
                num2 = int(num.pop())
                num1 = int(num.pop())
                result = num1+num2
                num.append(result)
            elif char == '-':
                num1 = int(num.pop())
                num2 = int(num.pop())
                result = num2-num1
                num.append(result)
            else:
                num.append(char)
    except:
        result = 'error'
    print('#{} {}'.format(tc, result))

