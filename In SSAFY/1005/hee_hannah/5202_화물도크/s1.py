import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    print('#{}'.format(tc), end=" ")
    n = int(input())
    truck = []
    for i in range(n):
        s, e = map(int, input().split())
        truck.append([s, e]) # 일단 트럭 안에 시작시간, 끝시간 담고
    # print(truck) [[14, 23], [2, 19], [1, 22], [12, 24], [21, 23], [6, 15], [20, 24], [1, 4], [6, 15], [15, 16]]
    truck.sort(key=lambda x: x[1]) # 람다를 사용하여 끝시간을 기준으로 정렬
    # print(truck) # [[1, 4], [6, 15], [6, 15], [15, 16], [2, 19], [1, 22], [14, 23], [21, 23], [12, 24], [20, 24]]
    fin = truck.pop(0)[1] # 첫번째를 기준으로
    cnt = 1
    while len(truck) > 0: # 트럭이 남아잇을때까지
        start, end = truck.pop(0)
        if fin <= start: # 끝나는 시간 보다 새로운 시작시간이 이상이라면
            fin = end # 끝을 바꿔주고
            cnt += 1 # 카운트
        if len(truck) == 0:
            break
    print(cnt)






    # hour = [0] * 24
    # total= []
    # while len(truck) > 0:
    #     num = 0
    #     for i in range(n):
    #         if hour[truck[i][0]:truck[i][1]] == [0]*(truck[i][1]-truck[i][0]): # 4~13 10칸
    #             num += 1
    #             hour[truck[i][0]:truck[i][1]] = [1] * (truck[i][1] - truck[i][0])
    #         elif hour[truck[i][0]:truck[i][1]] != [0]*(truck[i][1]-truck[i][0]):
    #             continue
    #     truck.pop(0)
    #     total.append(num)
    #     if len(truck) == 0:
    #         break
    # print(total)
    # print(max(total))

