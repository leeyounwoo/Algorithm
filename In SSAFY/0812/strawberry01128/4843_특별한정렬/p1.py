import sys
sys.stdin = open('input.txt')
T = int(input())
for test_case in range(1,T+1):
    num_su = int(input())
    sutja_list = list(map(int, input().split()))

    for _ in range(1, num_su):
        for j in range(0,num_su-1):
            if sutja_list[j] < sutja_list[j+1]:
                sutja_list[j+1], sutja_list[j] = sutja_list[j], sutja_list[j+1]
    for j in range(1,int(num_su),2):

        sutja_list.insert(j, sutja_list.pop())
    print('#{}'.format(test_case),end=" "); print(*sutja_list[0:10])


