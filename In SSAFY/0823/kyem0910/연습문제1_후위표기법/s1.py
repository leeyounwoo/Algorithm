string = '2+3*4/5'

stack = []
collection = ['+', '-', '*', '/']
for char in string:
    if char in collection:
        stack.append(char)
    else:
        print(char, end = "")

while stack:
    print(stack.pop(), end = "")