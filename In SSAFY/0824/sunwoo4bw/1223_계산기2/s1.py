import sys
sys.stdin = open('input.txt')
# 연산자 +, * 두 종류

def isdigit(x):  # 숫자인지 확인- 아까 Forth 문제에서 isdigit
    if x not in operator:
        return True
    else:
        return False

def icp(token):  # in-coming priority: 스택에 들어올 경우 연산자의 우선순위
    if token == "*":
        return 2
    elif token == "+":
        return 1

def isp(token):  # in-stack priority: 스택 내에 있을 때의 top 연산자 우선순위
    if token == "*":
        return 2
    elif token == "+":
        return 1

def postfix(m_expression):  # m_expression: 수식
    for token in m_expression:
        if isdigit(token) == True:  # 숫자인 경우
            postfix_complete.append(token)  # 후위표기식에 넣어

        elif token in operator:  # 숫자가 아닌 경우 -> 연산자
            priority = icp(token)  # 우선순위 비교

            # 스택 top의 연산자의 우선순위가 나보다 작을 때까지 pop
            while len(stack) > 0:  # stack이 비어있지 않을 때까지
                top = stack[-1]
                if isp(top) <= priority:
                    break

                    # 우선순위가 top 연산자의 우선순위보다 높니
                postfix_complete.append(stack.pop())  # stack에서 pop하고 complete에 담기
            stack.append(token)  # 토큰의 연산자를 stack에 push

    while len(stack) > 0:  # stack에 뭐가 있니
        remain = stack.pop()  # pop하고
        postfix_complete.append(remain)  # 출력

    return postfix_complete  # 출력!

T = 10
for tc in range(1, T + 1):
    len_tc = int(input())
    input_lst = list(input())  # 중위표기식으로 된 애
    postfix_complete = []  # 후위표기식으로 바꾼 애
    stack = []
    operator = ["*", "+"]

    result = postfix(input_lst)
    stack2 = []
    for token in result:
        if isdigit(token):
            stack2.append(token)
        else:
            a, b = int(stack2.pop()), int(stack2.pop())
            if token == "*":
                stack2.append(b * a)
            elif token == "+":
                stack2.append(b + a)

    realresult = stack2.pop()
    print("#{} {}".format(tc, realresult))