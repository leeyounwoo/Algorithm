import sys

def del_recursive(string):
    new_string = ''
    flag = False
    for i in range(len(string) - 1):
        if string[i] == string[i+1]:
            flag = True
            new_string = string[:i]
            if i < len(string) - 1:
                new_string += string[i+2:]
            new_string = del_recursive(new_string)
    if flag:
        return new_string
    return string

sys.stdin = open('input.txt')
for T in range(1, 1+int(input())):
    string = input()
    ans = del_recursive(string)
    print('#{} {}'.format(T, len(ans)))
