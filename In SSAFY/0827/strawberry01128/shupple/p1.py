import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    count = int(input())
    words = list(map(str, input().split()))
    half = []
    half_2 = []
    result = []
    for _ in range(count // 2):
        half.append(words.pop())
    for _ in range(count-(count // 2)):
        half_2.append(words.pop())

    for k in range(count):
        if k % 2:
            result.append(half.pop())
        else:
            result.append(half_2.pop())
    print('#{}'.format(tc),end=" ")
    for i in result:
        print(i,end=" ")
    print()
