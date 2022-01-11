import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    containers = sorted(list(map(int, input().split())), reverse=True)
    trucks = sorted(list(map(int, input().split())), reverse=True)

    print(containers, trucks)
    answer = 0
    for i in range(M):
        temp = 0
        for container in containers:
            if trucks[i] >= container >= temp:
                temp = container
        if temp != 0:
            containers.remove(temp)
        answer += temp

    print("#{} {}".format(tc, answer))
