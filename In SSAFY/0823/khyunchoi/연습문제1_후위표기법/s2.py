string = '2+3*4/5'
new_string = ''
# [isp, icp]
token_dict = {
    '*': [2, 2],
    '/': [2, 2],
    '+': [1, 1],
    '-': [1, 1],
    '(': [0, 3],
}

stack = []
for char in string:
    if char in '0123456789':
        new_string += char
    else:
        if len(stack) == 0:
            stack.append(char)
        else:
            while not token_dict[stack[-1]][0] < token_dict[char][1]:
                new_string += stack.pop()
            stack.append(char)