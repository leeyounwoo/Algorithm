import sys
sys.stdin = open('input.txt')

def switch_on_off(switch_count):

    for i in arr:
        a = 0
        b = 0
        gender = i[0]    # i[0]은 남학생(1)/여학생(2)
        num = i[1]       # num은 입력 숫자
        if gender == 1:  # 남학생일 때,
            for j in range(1, (switch_count//num)+1):  # 배수만큼 range 생성
                if switch[j*num-1] == 1:
                    switch[j * num - 1] = 0
                elif switch[j*num-1] == 0:
                    switch[j * num - 1] = 1

        elif gender == 2: # 여학생일 때,
            for r in range(1, num+1):
                if num-1-r >= 0 and num-1+r < switch_count and switch[num-1-r] == switch[num-1+r]:
                    continue
                elif num-1-r < 0 or num-1+r >= switch_count or switch[num-1-r] != switch[num-1+r]:
                    for y in range(num-r, num-1+r):
                        if switch[y] == 1:
                            switch[y] = 0
                        elif switch[y] == 0:
                            switch[y] = 1
                    break

    for i, e in enumerate(switch):
        if i and not (i % 20):
            print()
        print(e, end=' ')

switch_count = int(input())
switch = list(map(int, input().split()))
std = int(input())
arr = [list(map(int, input().split())) for _ in range(std)]
switch_on_off(switch_count)





