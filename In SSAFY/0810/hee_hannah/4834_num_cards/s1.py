import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    list_a = []
    for i in input():
        list_a.append(int(i))
        dic = {}
        for j in list_a:
            if j not in dic:
                dic[j] = 1
            else:
                dic[j] += 1
        for key, value in dic.ltems():


    print('#{} {} {}'.format(tc,max(dic.items()))