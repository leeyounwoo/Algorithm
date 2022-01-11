import sys
sys.stdin = open('input.txt')

def selectionsort(a):
    for i in range(0, len(a)-1):
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j] :
                min = j
        a[i], a[min] = a[min], a[i]
    return a

T = int(input())

for tc in range(T):
    N = int(input())
    a_list = list(map(int, input().split()))
    a_list = selectionsort(a_list)  # 정렬
    result = []
    count = 0

    while a_list:
        result.append(a_list.pop())
        result.append(a_list.pop(0))

    print(f"#{tc}", end=' ')
    for i in range(10):
        print(result[i], end=" ")
    print()
