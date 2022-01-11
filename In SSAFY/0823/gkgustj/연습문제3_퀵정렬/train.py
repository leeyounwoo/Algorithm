def quicksort(a, begin, end):
    if begin < end:
        p = paritition(a, begin, end)
        quicksort(a, begin, p-1)
        quicksort(a, p+1, end)


def paritition(a, begin, end):
    pivot = (begin + end) // 2
    L = begin
    R = end

    while L < R:
        while (a[L] < a[pivot] and L < R):
            L += 1
        while (a[R] >= a[pivot] and L < R):
            R -= 1

        if L < R:
            if L == pivot:
                pivot = R

            a[L], a[R] = a[R], a[L]

    a[pivot], a[R] = a[R], a[pivot]
    return R


a = [69, 10, 30, 2, 16, 8, 31, 22]
quicksort(a, 0, 7)

print(a)