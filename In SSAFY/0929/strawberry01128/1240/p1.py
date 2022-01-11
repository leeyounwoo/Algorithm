import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    password_tower = []
    real_p = []
    amho = []
    count = 0
    code = []
    answer = 0
    result = [['0','0','0','1','1','0','1'],['0','0','1','1','0','0','1'],
              ['0', '0', '1', '0', '0', '1', '1'],['0','1','1','1','1','0','1'],
              ['0', '1', '0', '0', '0', '1', '1'],['0','1','1','0','0','0','1'],
              ['0', '1', '0', '1', '1', '1', '1'],['0','1','1','1','0','1','1'],
              ['0', '1', '1', '0', '1', '1', '1'],['0','0','0','1','0','1','1']]
    flag = False
    line, length = map(int,input().split())
    for _ in range(line):
        password = list(input())
        if '1' in password:
            if password_tower == []:
                password_tower = password
    password_tower.reverse()
    for k in password_tower:

        if k == '1':
            flag = True
        if flag == True:
            real_p.append(k)
            count += 1
        if count == 56:
            break
    real_p.reverse()
    for p in range(8):
        number = real_p[7*p:7*(p+1)]
        for k in range(10):
            if number == result[k]:
                amho.append(k)

    for k in range(len(amho)):
        if not k % 2:
            code.append(amho[k]*3)
        else:
            code.append(amho[k])
    if not sum(code) % 10:
        answer = sum(amho)
    else:
        answer = 0
    print('#{} {}'.format(tc,answer))




