def check_matching(list):
    check_list = []
    for check in list:
        if check == '(':
            check_list.append(check)
        else:
            if len(check_list) !=0:
                c = check_list.pop()
                if c+check != '()':
                    return False
            else:
                return False
    if len(check_list) != 0:
        return False
    else:
        return True

a = '()()((()))'
b = '((( )((((( )( )((( )( ))((( ))))))'


print(check_matching(a))
print(check_matching(b))