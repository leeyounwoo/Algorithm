go, slip, goal = map(int, input().split())

# 낮에 올라간 만큼 더하고 시작
goal -= go
day_go = go - slip
time, rest = divmod(goal, day_go)
if rest:
    time += 1
print(time + 1)
