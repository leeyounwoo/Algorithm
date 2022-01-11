import sys
sys.stdin = open('input.txt')

T = int(input())
def selectionsort(a):
    for i in range(0, len(a)-1):
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]
    return a

num_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for Tc in range(1, T+1):
    Tc, N = input().split()
    N = int(N)
    str_list = list(input().split())

    checked = []

    for i in range(N):
        checked.append(num_list.index(str_list[i]))
    result = selectionsort(checked)

    for i in range(N):
        result[i] = num_list[result[i]]
    print("{}".format(Tc))
    print(*result)