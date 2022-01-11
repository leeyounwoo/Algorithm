import sys
sys.stdin = open('input.txt')
def cycle(num):
    flag = False
    while True:
        for i in range(1,6):
            t = num.pop(0)
            if t - i <= 0:
                num.append(0)
                flag = True
                break
            else:
                num.append(t-i)
        if flag:
            break
    return num

for tc in range(1,11):
    t_num = int(input())
    number = list(map(int, input().split()))
    print(cycle(number))