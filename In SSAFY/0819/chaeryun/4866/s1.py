import sys
sys.stdin = open('input.txt')

TC = int(input())

for tc in range(1, TC+1):
    str = input()
    
    stack = []
    for i in range(len(str)):
        if str[i] == "(" or str[i] == "{":                # 열린괄호가 들어오면        
            stack.append(str[i])                          # 스택에 쌓는다
        elif str[i] == ")" or str[i] == "}":              # 닫는괄호가 들어오면                     
            if len(stack) == 0:                           # 스택이 0이면 result = 1                 
                stack = [str[i]]
                break
            elif (str[i] == "}" and stack[-1] !="{"):  
                stack = [str[i]]
                break
            elif (str[i] == ")" and stack[-1] != "("):
                stack = [str[i]]
                break
            else:                                                   
                stack.pop()
    
    if len(stack) == 0:
        result = 1
    else:
        result = 0
    print("#{} {}".format(tc, result))