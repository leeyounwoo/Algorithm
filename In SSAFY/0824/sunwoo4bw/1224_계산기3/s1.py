import sys
sys.stdin = open('input.txt')
# 연산자 +, * 두 종류

def isdigit(x):  # 숫자인지 확인- 아까 Forth 문제에서 isdigit
    if x not in operator:
        return True
    else:
        return False

def isp(token):  # in-stack priority: 스택 내에 있을 때의 top 연산자 우선순위
    if token == "*":
        return 2
    elif token == "+":
        return 1
    elif token == "(" :
        return 0

def icp(token):  # in-coming priority: 스택에 들어올 경우 연산자의 우선순위
    if token == "*":
        return 2
    elif token == "+":
        return 1
    elif token == "(" :
        return 3

T = 10
for tc in range(1, T + 1):
    len_tc = int(input())
    input_lst = list(input())
    postfix_complete = []
    stack = []
    operator = ["*", "+", "(", ")"]

    for token in input_lst:
        if isdigit(token):
            postfix_complete.append(token)
        elif token == ')':
            while len(stack) :
                top = stack.pop()
                if top == '(' :
                    break
                postfix_complete.append(top)
        else :
            if len(stack) == 0:
                stack.append(token)
            else :
                while len(stack) :
                    top = stack[-1]
                    if isp(top) < icp(token) :
                        break
                    postfix_complete.append(stack.pop())
                stack.append(token)
    while len(stack) :
        remain = stack.pop()
        postfix_complete.append(remain)

    ans = []
    for sth in postfix_complete :
        if isdigit(sth) :
            ans.append(sth)
        else :
            a, b = int(ans.pop()), int(ans.pop())
            if sth == "*":
                ans.append(b * a)
            elif sth == "+":
                ans.append(b + a)

    print("#{} {}".format(tc, ans.pop()))