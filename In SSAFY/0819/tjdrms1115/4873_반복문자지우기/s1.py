import sys
sys.stdin = open('input.txt')


# 스택 클래스입니다.
class Stack:

    # 스택을 초기화합니다. 속도를 위해 고정 크기를 사용했습니다.
    def __init__(self):
        self.stack = [-1] * 10000
        self.idx = -1

    # 스택이 비어있는지 검사하는 함수입니다.
    def is_empty(self):
        if self.idx == -1:
            return True
        return False

    # 스택 푸시
    def push(self, item):
        self.idx += 1
        self.stack[self.idx] = item

    # 스택 팝
    def pop(self):
        if self.idx == -1:
            return None
        item = self.stack[self.idx]
        self.stack[self.idx] = -1
        self.idx -= 1
        return item

    # 스택 맨 위의 값을 반환하는 함수입니다.
    def peek(self):
        return self.stack[self.idx]


T = int(input())

answer = []
for tc in range(1, T+1):
    # 스택을 초기화합니다.
    stack = Stack()
    # 문자열을 입력받습니다.
    string = input()
    # 문자열의 문자를 하나하나 스택에 넣습니다.
    for char in string:
        # 만약에 넣고자 하는 문자가 스택 맨위 문자와 같다면
        # 문자를 넣는 대신 스택에서 문자 하나를 제거합니다.
        if char == stack.peek():
            stack.pop()
        else:
            stack.push(char)

    # 스택에 남은 문자 갯수가 결과입니다.
    result = stack.idx + 1
    answer.append(result)

for tc in range(1, T+1):
    print('#{} {}'.format(tc, answer[tc-1]))
