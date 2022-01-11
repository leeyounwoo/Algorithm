import sys
sys.stdin = open('input.txt')

def permutation(k):
    '''
    :param k: 뽑아야 하는 개수
    :return:
    '''
    result = [] # 전체 순열의 집합
    picked = [] # 지금까지 뽑은 원소의 집합

    def recursion(count):
        # count == 현재까지 뽑은 개수
        if count == k:
            result.append(tuple(picked))
        else:
            for i in range(len(arr)):
                if arr[i] not in picked:
                    picked.append(arr[i])
                    recursion(count+1)
                    picked.pop()

    recursion(0)
    return result


for T in range(1, 1+int(input())):
    n = int(input())
    arrays = [list(map(int, input().split())) for _ in range(n)]
    arr = [i for i in range(n)]
    result = permutation(n)
    ans = 10 * n
    for order in result:
        temp = 0
        for i in range(n):
            temp += arrays[i][order[i]]
        if temp < ans:
            ans = temp
    print('#{} {}'.format(T, ans))