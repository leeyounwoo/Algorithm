import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    #ai의 입력된 수들을 인덱스로 호출하기 위해 split하지 않음
    ai = list(map(int, input()))
    num_list = [0] * 10
    max_index, max_num = 0, 0

    for card in range(N):
        num_list[ai[card]] += 1

    #큰 수부터 출력하기 위해 range범위 조정
    for cnt in range(len(num_list)-1, -1, -1):
        if num_list[cnt] > max_index:
            max_index = num_list[cnt]
            max_num = cnt

    print('#{} {} {}'.format(tc+1, max_num, max_index))