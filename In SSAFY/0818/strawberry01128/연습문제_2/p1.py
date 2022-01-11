import sys
sys.stdin = open('input.txt')

# def push(item):
#     stack.append(item)
#
# def test(item):
#     if item == '(':
#         return push(item)
#     elif item == ')':
#         return stack.pop()
# def testify(item):
#     if len(stack) == 0:
#         return 'correct'
#     else:
#         return '잔여물이 남았습니다'
# stack = []
# for i in range(2):
#     iniput = list(map(str, input()))
#     for j in iniput:
#         test(j)
#
#     print(testify(stack))

#-----------------------교수님코드---------------
stack = []

def is_empty():
    # 만약 스택의 길이가 0이면 True
    if len(stack) != 0:
        return True
    else:
        return False
def check_matching(data) : # '((()))'
    for i in range(len(data)): # 문자열 스캔
        if data[i] == '(':     # 스택에 push (왼쪽괄호)
            stack.append(data[i])
        else:
            # 만약 스택이 비어있는 경우
            if is_empty():
                return False # 전체 짝 안맞음
            stack.pop()
    if not is_empty()
        return False
    return True
