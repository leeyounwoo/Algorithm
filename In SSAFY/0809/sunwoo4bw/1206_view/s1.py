import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    num = int(input())
    building = list(map(int, input().split()))

    result_view = 0
    for i in range(2, num-2):   # 양옆 2칸
        while True:             # 양옆 2칸보다 크니
            if building[i] > building[i+1] and building[i] > building[i+2] and building[i] > building[i-1] and building[i] > building[i-2]:
                result_view += 1
                building[i] -= 1  # 세대(층) 차이
            else:
                break
    print('#{0} {1}'.format(tc, result_view))