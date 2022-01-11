import sys
sys.stdin = open('input.txt')

T = int(input())

def bubble_sort(num):
    for i in range(len(num)-1, 0, -1):		# 범위의 끝 위치
        for j in range(0,i):
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]
    return num


for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))

    num = bubble_sort(num)                # 버블정렬 이용
    result = []

    for i in range(5):                    # 주의 ) 10개만 출력! N//2 해서 틀림
        result.append(num[len(num)-1-i])    # 정렬된 리스트 가장 큰 값 추출 후 추가
        result.append(num[i])               # 정렬된 리스트 가장 작은 값 추출

    result = ' '.join(map(str, result))
    print('#{} {}'.format(tc, result))