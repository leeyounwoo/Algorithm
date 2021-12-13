x, y, w, h = map(int, input().split())
left = x
right = w - x
top = h - y
bottom = y
ans = min(left, right, top, bottom)
print(ans)