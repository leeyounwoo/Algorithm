import sys
sys.stdin = open('input.txt')

T = int(input())

def pascal_triangle(n):
    pascal = [[1]]

    for i in range(1, n):
        lst = [1]
        m = 0
        while m+1 < len(pascal[i-1]):
            lst.append(pascal[i-1][m]+pascal[i-1][m+1])
            m += 1
        lst.append(1)
        pascal.append(lst)

    return pascal

for tc in range(T):
    n = int(input())
    triangle = pascal_triangle(n)
    print('#{}'.format(tc+1))
    for i in range(n):
        print(*triangle[i])
