import sys
sys.stdin = open('input.txt')

#선택정렬
#주어진 자료 중 가장 작은 값부터 차례대로 선택하여 위치 교환
# 1. 최소값 찾기
# 2. 그 값을 리스트의 맨 앞에 위치한 값과 교환
# 3. 맨 처음 위치를 제외한 나머지 리스트를 대상으로 위의 과정 반복
def selectionSort(a):
    for i in range(0, len(a)-1) :           # 작업구간의 시작
        min = i                             # 맨 앞을 제일 작다고 가정
        for j in range(i+1, len(a)):
            if a[min]> a[j] :
                min = j
            a[i], a[min] = a[min], a[i]
        return a

T = int(input())           # 3
for tc in range(1, T+1):   # 1,2,3
    N = int(input())
    data = list(map(int, input().split()))
    data = selectionSort(data)
    result = []
    count = 0

    while data:
        result.append(data.pop())
        result.append(data.pop(0))

    print("#{}".format(tc), end=' ')
    for i in range(10):
        print(result[i], end=' ')
    print()








