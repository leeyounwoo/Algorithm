import sys
sys.stdin = open('input.txt')

def switch_on_off(arr):

    if arr[0] == 1:
        for i in range(1, switch_count//arr[1] + 1):
            if switch[arr[1]*i-1] == 1:
                switch[arr[1] * i - 1] = 0
            else:
                switch[arr[1] * i - 1] = 1


    elif arr[0] == 2:
        while switch[arr[1]-2] == switch[arr[1]]:

            if arr[1]-3 != 0 and arr[1]+1 != switch_count and switch[arr[1]-2] and switch[arr[1]] == 1: # 여기부터 다시하기
                switch[arr[1] - 2] = switch[arr[1]] = 0

            elif switch[arr[1]-2] and switch[arr[1]] == 0:
                switch[arr[1] - 2] = switch[arr[1]] = 1

        return switch

switch_count = int(input())
switch = map(int, input().split())
N = int(input())
arr = [input().split() for _ in range(N)]
print(arr)

print(switch_on_off(arr))





