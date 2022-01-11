string = '2+3*4/5'

def post_fix(string):
    token = ['+', '-', '*', '/']
    stack = []
    ans = ''
    for s in string:
        if not s in token:
            ans += s
        else:
            stack.append(s)

    while stack:
        ans += stack.pop()
    return ans

print(post_fix(string))