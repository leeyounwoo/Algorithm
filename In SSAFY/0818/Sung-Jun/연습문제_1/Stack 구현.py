def push(item):
    stack.append(item)
    #함수는 바깥내용을 조작하는것은 좋지않다
    #내부 안에서만 조작하는 함수를 작성하자
def pop():
    if len(stack) == 0:
        print('stack이 비어있습니다!')
        return
    return stack.pop()

stack = []

push(1)
push(2)
push(3)
print(stack)
print(pop())
print(pop())
print(pop())
pop()
