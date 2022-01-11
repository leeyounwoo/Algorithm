import sys
sys.stdin = open('input.txt')

TC = int(input())

for tc in range(TC):
    string = list(str(input()))
    temp = []

    temp.append(string.pop(0))

    while string:
        if not temp:
            temp.append(string.pop(0))
        if temp[-1] == string[0]:
            temp.pop(-1)
            string.pop(0)
        else:
            temp.append(string.pop(0))

    print(f"#{tc+1} {len(temp)}")

