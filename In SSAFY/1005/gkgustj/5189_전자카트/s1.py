import sys
sys.stdin = open('input.txt')

def use_battery(lst):
    total = 0

    for i in range(0, len(lst)-1):
        total += battery[lst[i]][lst[i+1]]
    
    return total


def find_path(k):
    result = []
    picked = []

    def recursion(count):
        if count == k:
            result.append(tuple(picked))
        else:
            for i in range(2, N+1):
                if i not in picked:
                    picked.append(i)
                    recursion(count+1)
                    picked.pop()
    
    recursion(0)
    return result
    

T = int(input())

for t in range(1, T+1):
    N = int(input())
    battery = [[0 for _ in range(N+1)]]

    for _ in range(N):
        battery.append([0] + list(map(int, input().split())))

    min_battery = float('inf')

    for path in find_path(N-1):
        path = [1] + list(path) + [1]
        min_battery = min(min_battery, use_battery(path))

    print('#{} {}'.format(t, min_battery))