import sys
sys.stdin = open('input.txt')

Test = int(input())

for test_case in range(1,Test+1):
    box = []
    result = []
    case = 0
    N, sumsum = list(map(int, input().split()))
    for box_case in range(1,N+1):
        box.append(box_case)

    for i in range(1 << N):
        for j in range(N):
            if i & (1 << j):
                print(box[j],end=" ")
        print()
                # if sum(box[j]) == sumsum:
                #     case += 1
    print(case)

