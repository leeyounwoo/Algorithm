import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(10):
    tc, N = input().split()
    arr = list(input().split())
    num_list = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

    # 선택 정렬 사용
    for i in range(int(N) - 1):
        min_idx = i
        for j in range(i + 1, int(N)):
            if num_list.index(arr[min_idx]) > num_list.index(arr[j]): # 해당 arr 값에 대응하는 index 값을 비교하는 if문
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    print(tc)
    print(' '.join(arr))