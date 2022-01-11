array = [7, 23, 11, 9, 34, 22, 585, 234, 77, 45, 28, 16]

def selectionSort(a):
    for i in range(0, len(a)-1):
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:
                min = j
            a[i], a[min] = a[min], a[i]

    return a

print(selectionSort(array))