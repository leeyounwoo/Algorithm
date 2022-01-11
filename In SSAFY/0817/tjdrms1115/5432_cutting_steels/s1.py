import sys
sys.stdin = open('input.txt')


class Stack:

    def __init__(self):
        self.MAX_SIZE = 100000
        self.stack = [-1] * self.MAX_SIZE
        self.idx = -1

    def push(self, c):
        self.idx += 1
        self.stack[self.idx] = c

    def pop(self):
        item = self.stack[self.idx]
        self.stack[self.idx] = -1
        self.idx -= 1
        return item

    def isEmpty(self):
        if self.idx < 0:
            return True
        return False

    def isFull(self):
        if self.idx >= self.MAX_SIZE:
            return True
        return False


T = int(input())

answer = []
for tc in range(1, T + 1):

    input_seq = input()

    stack = Stack()

    result = 0
    for i in input_seq:
        if i == '(':
            stack.push(i)
        elif i == ')':
            count = 0
            a = stack.pop()
            while a != '(':
                if a == 0:
                    count += 1
                else:
                    count += a - 1
                a = stack.pop()
            if count == 0:
                stack.push(count)
            else:
                result += count + 1
                stack.push(count + 1)

    answer.append(result)

for tc in range(1, T + 1):
    print('#{0} {1}'.format(tc, answer[tc-1]))
