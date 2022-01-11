import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    number = input()
    list1 = []
    for num in number:
        list1.append(int(num))
    triplet = run = 0

    for i in range(len(list1)):
        if list1[i] != -10:
            if list1.count(list1[i]) >= 3:
                triplet += 1
                temp = list1[i]
                for _ in range(3):
                    list1[list1.index(temp)] = -10
            else:
                if list1[i] - 1 in list1 and list1[i] + 1 in list1:
                    run += 1
                    list1[list1.index(list1[i]+1)] = -10
                    list1[list1.index(list1[i]-1)] = -10
                    list1[list1.index(list1[i])] = -10

    if triplet + run == 2:
        print(triplet, run, "baby-gin")
    else:
        print("아니다")

