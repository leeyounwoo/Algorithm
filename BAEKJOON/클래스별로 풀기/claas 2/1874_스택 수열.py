import sys

sys.stdin = open('input.txt')
n = int(input())
numbers = [i+1 for i in range(n)]
# print(numbers)
want = [int(sys.stdin.readline()) for _ in range(n)]
# print(want)

break_flag = False
temp = []
ans = []
for i in range(len(want)):
    # print(want[i])
    # print(temp)
    if want and want[i] in temp:
        if temp[-1] == want[i]:
            temp.pop()
            ans.append('-')
        else:
            ans = "NO"
            break_flag = True
            break
    else:

        while numbers[0] <= want[i]:
            temp.append(numbers.pop(0))
            ans.append('+')
            if not numbers:
                break
        ans.append('-')
        temp.pop()
if break_flag:
    print(ans)
else:
    for i in range(len(ans)):
        print(ans[i])


