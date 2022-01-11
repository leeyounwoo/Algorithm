arr = [-1, 5, 10, 7, -5, 9, 2, 3, 0, 15]
n = len(arr)

for i in range(1 << n):
    total = 0
    # 부분집합이 만들어지는 부분
    for j in range(n):
        if i & (1 << j):
            total += arr[j]
    if total == 0 :
        print('0되는 경우가 있습니다!')

# shift 연산 연습
print(0b0011 << 2) # 0011 : 3 // 12
print(3 << 2)      # // 12

print(10 << 2)     # // 40
print(0b10 << 2)   # // 8