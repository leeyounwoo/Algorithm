import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    area_num = int(input())
    numbers = [list(map(int, input().split())) for _ in range(area_num)]

    color1 = []
    color2 = []
    for number in numbers:
        start = int(str(number[0])+str(number[1]))
        end = int(str(number[2])+str(number[3]))
        for area in range(start, end+1):
            if number[1] <= area%10 <= number[3] and number[0] <= area//10 <= number[2]:
                if number[-1] == 1:
                    color1.append(area)
                else:
                    color2.append(area)

    result = 0
    for check in list(set(color1)):
        if check in list(set(color2)):
            result += 1
    print('#{} {}' .format(tc+1, result))
