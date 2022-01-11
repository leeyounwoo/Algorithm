import sys
sys.stdin = open('input.txt')

def box(n): #4 그려보다가 규칙성 발견..  내앞+내앞앞*2
    table = [1, 3] #첫번째 두번째 미리 넣기

    for i in range(2, n+1): # 2 3 4
        table.append(table[i-1]+table[i-2]*2) #1 0  2 1  3 2
    return table[n-1]

t = int(input())

for tc in range(1, t+1):
    n = (int(input())//10) #10 20 30...
    result = box(n)
    print('#{} {}'.format(tc, result))



    # box = int(input())
    # count = 0
    # for i in range(0, (box//10)+1):
    #     if (box - 10*i) % 20 == 0:
    #         count += (box//10)+1
    #         if (box - 10*i) // 10 > 0:
    #             count += 2*i
    #     else:
    #         continue
    # print('#{} {}'.format(tc, count))
