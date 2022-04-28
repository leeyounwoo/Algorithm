def make_u_v(p):
    left_cnt = 0
    right_cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            left_cnt += 1
        else:
            right_cnt += 1
        if left_cnt != 0 and left_cnt == right_cnt:
            u = p[:i + 1]
            v = p[i + 1:]
            return {'u': u, 'v': v}


def isRight(p):
    stack = []
    for i in range(len(p)):
        if p[i] == '(':
            stack.append(p[i])
        else:
            if not stack:
                return False
            else:
                stack.pop()
    if stack:
        return False
    else:
        return True


def recursion(p):
    ans = ''
    u_v_dict = make_u_v(p)
    u, v = u_v_dict['u'], u_v_dict['v']
    if isRight(u):
        ans += u
        if v != '':
            ans += recursion(v)
        return ans
    else:
        temp = '('
        if v != '':
            temp += recursion(v)
        temp += ')'

        for s in list(u)[1:-1]:
            if s == '(':
                temp += ')'
            else:
                temp += '('

        return temp

def solution(p):
    answer = recursion(p)

    return answer

print(solution("()))((()"))