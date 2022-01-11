import sys
sys.stdin = open('input.txt')

T= int(input())
for test_case in range(1,T+1):
    text = input()
    ans = 0
    a = 0
    b = 0
    # 2.{(}) 난 막으려는데 누군가 가로막는다.
    for i in text:
        if i == '{':
            b += 1
        elif i == '(':
            a += 1
        elif i == '}':
            b -= 1
            if b < 0:
                ans = 0
        elif i == ')':
            # 이거를 추가해줘야 }{ 같은 거꾸로치는 박수 꼼수짓 못함
            a -= 1
            if a < 0:
                ans = 0

        if b != 0 and i == ')':
            ans = 0
        elif a != 0 and i == '}':
            ans = 0
        if a == 0 and b == 0:
            ans = 1
    print('#{} {}'.format(test_case, ans))