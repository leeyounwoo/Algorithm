import sys
sys.stdin = open('input.txt')

T = int(input())         # 3
for tc in range(1, T+1):
    n = int(input())     #5
    nums=input()

    count = [0 for _ in range(10)]   #숫자 먼저 count해줘 [0 0 0 0 1 0 1 1 0 2]
    for i in nums :
        count[int(i)] += 1

    max_idx = 0
    max_v = 0
    for j in range(len(count)):     # count돌면서 max_v 가장 큰 거 찾아줘
        if count[j] >= max_v:       # j - 1 -> max_idx : 1 , max_v 0
            max_v= count[j]
            max_idx = j

    print('#{0} {1} {2}' .format(tc, max_idx, max_v))
    # card_nums_list = []
    # for i in input():
    #     card_nums_list.append(int(i))  #[4, 9, 6, 7, 9] [0, 8, 2, 7, 1] [7, 7, 9, 7, 9, 4, 6, 5, 4, 3]



# 가장 많이 등장한 숫자가 뭐니, 그 개수는?
# 만약 개수가 같으면 숫자가 큰 쪽을 출력
