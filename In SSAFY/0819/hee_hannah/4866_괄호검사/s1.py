import sys
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    a = input()
    stack = [] #스택만들기
    for i in a: # a안에서
        if i == '(' or i == '{':
            stack.append(i) #일단 넣기
        elif i == '}': # 빼는 순서가 중요하니까 나눠서...
            if len(stack) == 0: # 얘만 남았다면 어차피 오류니까 0아니게 만들고
                stack.append(i)
            elif stack[-1] == '{': #마지막이 {라면 제대로 된거니까
                stack.pop() #빼주고
            else: # ( 이게 남았다면 어차피 오류니까 넣어주기..
                stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                stack.append(i)
            elif stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)

    if len(stack) == 0: #비어있다면 참
        print('#{} 1'.format(tc))
    else: # 거짓
        print('#{} 0'.format(tc))
