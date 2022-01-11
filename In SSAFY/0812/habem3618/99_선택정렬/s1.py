def selectionsort(a):
    for i in range(0, len(a)-1):
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j] :
                min = j
        a[i], a[min] = a[min], a[i]

    return a

a = [1, 9, 15, 4, 28, 45, 33]
print(selectionsort(a))