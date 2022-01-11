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
    N = int(input())
    batterys = [list(map(int, input().split())) for _ in range(N)]
    arr = [i+1 for i in range(N-1)]
    result = permutation(N-1)
    ans = 100 * N

    for order in result:
        # print(batterys[0][order[0]])
        temp = batterys[0][order[0]]
        for i in range(len(order)-1):
            temp += batterys[order[i]][order[i+1]]
        temp += batterys[order[len(order)-1]][0]
        if temp < ans:
            ans = temp

    print('#{} {}'.format(T, ans))
