import sys
sys.stdin = open('input.txt')

'''
3
123 1
2737 1
32888 2

1. 몇번 바꿀수 있는가를 본다
2. 바꿀수 있는 한도 내에서 가장 왼쪽의 숫자를 가장 큰 숫자로 바꾼다. 단 cnt가 남아있다면 작더라고 바꿔야한다
3. 바꾸는 우선순위는 같은 숫자가 있더라면 더 오른쪽에 있는 숫자가 우선순위
4. cnt 가 남아서 변경할때는 ex 857147 두번째로 왼쪽에 있는 숫자보다 작은것을 우선 탐색해라
'''
T = int(input())


def change_num(a, k):
    n = list(map(int, a))
    cnt = int(k)
    i = 0

    max_num = [0, 0]
    for num in range(0 + i, len(n)):
        if max_num[1] <= n[num]:
            max_num = [n[num], num]


    print(max_num)


for tc in range(T):
    number, cnt = input().split()
    print(number, cnt)
    change_num(number, cnt)
