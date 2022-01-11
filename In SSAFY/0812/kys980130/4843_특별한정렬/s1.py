import sys
sys.stdin = open("input.txt")

def selection_sort(a):                      # 최솟값부터 정렬하는 함수
    for i in range(0, len(a)-1):
        min = i                             # 맨 처음 값을 최솟값으로 가정
        for j in range(i+1, len(a)):        # i의 다음 수부터 마지막 수까지 반복문 돌리기
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]
    return a
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))     # 2 5 4 9 3 8 1 7 6 10
    sort_numbers = selection_sort(numbers)        # 1 2 3 4 5 6 7 8 9 10
    result = []                                   # 10 1 9 2 8 3 7 4 6 5
    for i in range(10):                           # 10개의 수 만을 출력해야 되므로 반복문 10번 돌리기
        if i % 2 == 0:                            # index가 짝수 일 때 역순 배열
            result.append(sort_numbers[N-1-i//2]) # index는 0부터 시작하기 때문에 전체 개수보다 1 작기 때문 N-1
        else:                                     # index가 홀수일 때 작은 수에서 큰 순서대로 배열
            result.append(sort_numbers[i//2])
    result = " ".join(map(str, result))
    print('#{} {}'.format(tc, result))