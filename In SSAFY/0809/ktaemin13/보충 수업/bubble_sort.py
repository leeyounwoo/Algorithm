def bubble_sort(a):
    for i in range(len(a)-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]



N = int(input())
arr = list(map(int, input().split()))
bubble_sort(arr)
print(arr)