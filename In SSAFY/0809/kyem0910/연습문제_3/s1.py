import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    max_num = int(input())
    list1 = list(map(int, input().split()))
    for i in range(len(list1)):
        count = 0
        for j in range(i+1, len(list1)):
            if list1[i] <= list1[j]:
                count += 1
        list1[i] = max_num - i - 1 - count
    print(max(list1))
