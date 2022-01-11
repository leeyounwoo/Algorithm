import sys
sys.stdin = open('input.txt')

TC = int(input())

# for tc in range(TC):
#     pattern = str(input())
#     origin = str(input())
#     if pattern in main:
#         print(f"#{tc+1} 1")
#     else:
#         print(f"#{tc+1} 0")

for tc in range(TC):
    flag = False
    pattern = str(input())
    origin = str(input())
    for i in range(len(origin) - len(pattern) + 1):
        temp = 0
        for j in range(len(pattern)):
            if origin[i+j] == pattern[j]:
                temp += 1
            else:
                break
        if temp == len(pattern):
            flag = True

    if flag:
        print(f"#{tc + 1} 1")
    else:
        print(f"#{tc + 1} 0")


