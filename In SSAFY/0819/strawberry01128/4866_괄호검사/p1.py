import sys
sys.stdin = open('input.txt')

def poham_test(text):
    # 오류가 나는경우 1. 괄호의 수가 맞지않다.
    # 2.{(}) 난 막으려는데 누군가 가로막는다.
    for i in text:
        if  i =='{' or i == '(':
            gwalho.append(i) # 창문 연사람 이름 적어
        elif i =='}' or i ==')':
            if len(gwalho) > 0: #창문 닫은려는데 연사람 있어?
                ppop = gwalho.pop()           # 창문 연사람 색출해내
            else: # 창문 닫으려는데 연사람이 없네?(잘못)
                return 0
            if i == '}' and ppop == '(': #영희가 닫았는데 누가 창문열었어 철수가 열었네
                return 0                 # 그럼 영희 창문은 열려있잖아(잘못)
            if i == ')' and ppop == '{':
                return 0

    if len(gwalho) == 0: # 열고 잘 닫았다.
        return 1
    else: #열었는데 닫질않았다.(잘못)
        return 0
T= int(input())
for test_case in range(1,T+1):
    text = input()
    gwalho = []
    print('#{} {}'.format(test_case,poham_test(text)))
    # 오류가 나는경우 1. 괄호의 수가 맞지않다.
    # if text.count('(') != text.count(')'):
    #     return 1

    # 2.{(}) 난 막으려는데 누군가 가로막는다.


    # # 오류가 나는경우 1. 괄호의 수가 맞지않다.
    # a = 0
    # b = 0
    # # if text.count('(') != text.count(')'):
    # #     return 0
    # # 2.{(}) 난 막으려는데 누군가 가로막는다.
    # for i in text:
    #     if i == '{':
    #         b += 1
    #     elif i == '(':
    #         a += 1
    #     elif i == '}':
    #         b -= 1
    #         if b < 0:
    #             return 0
    #     elif i == ')':
    #         # 이거를 추가해줘야 }{ 같은 거꾸로치는 박수 꼼수짓 못함
    #         a -= 1
    #         if a < 0:
    #             return 0
    #     if  b!= 0 and i == '}'
    #       return 0
    #     elif a!= 0 and i == ')'
    #       return 0
