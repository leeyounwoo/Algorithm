import sys
sys.stdin = open('input.txt')

def m_code():
    while arr[-1] > 0:
        for i in range(1, 6):
            if arr[0] - i <= 0:
                arr.pop(0)
                arr.append(0)
                break
            else:
                arr.append(arr.pop(0) - i)

    return print('#{}'.format(tc+1), *arr)


for tc in range(10):
    N = input()
    arr = list(map(int, input().split()))
    m_code()