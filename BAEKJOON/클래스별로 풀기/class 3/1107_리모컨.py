import sys


def input():
    return sys.stdin.readline().rstrip()


def smallChannel(avail_buttons, channel_length, goal_channel):
    if channel_length <= 1:
        return 1_000_0000
    else:
        for i in range(9, -1, -1):
            if avail_buttons[i]:
                return int(goal_channel) - int(str(i) * (channel_length - 1)) + channel_length - 1

        return 1_000_0000

def bigChannel(avail_buttons, channel_length, goal_channel):
    for i in range(1, 10):
        if avail_buttons[i]:
            if avail_buttons[0]:
                return int(str(i) + '0' * channel_length) - int(goal_channel) + channel_length + 1
            else:
                return int(str(i) * (channel_length + 1)) - int(goal_channel) + channel_length + 1
    return 1_000_0000


def findSmaller(avail_buttons, index):
    ans = index
    for _ in range(10):
        ans -= 1
        if ans == -1:
            ans = 9
        if avail_buttons[ans]:
            return ans
    return 11

def findBigger(avail_buttons, index):
    ans = index
    for _ in range(10):
        ans += 1
        if ans == 10:
            ans = 0
        if avail_buttons[ans]:
            return ans
    return 11

def sameChannel(avail_buttons, channel_length, goal_channel):
    numbers = ['']
    for i in range(len(goal_channel)):
        if avail_buttons[int(goal_channel[i])]:
            cnt = len(numbers)
            for _ in range(cnt):
                temp = numbers.pop(0)

                smaller = findSmaller(avail_buttons, int(goal_channel[i]))
                if smaller != 11:
                    numbers.append(temp + str(smaller))

                numbers.append(temp + goal_channel[i])

                bigger = findBigger(avail_buttons, int(goal_channel[i]))
                if bigger != 11:
                    numbers.append(temp + str(bigger))

        else:
            for j in range(int(goal_channel[i])-1, -1, -1):
                if avail_buttons[j]:
                    small = int(goal_channel[i]) - j
                    break
            else:
                small = 100

            for j in range(int(goal_channel[i])+1, 10):
                if avail_buttons[j]:
                    big = j - int(goal_channel[i])
                    break
            else:
                big = 100

            if small == 100 and big == 100:
                return 1_000_0000

            elif small == 100 and big != 100:
                cnt = len(numbers)
                for _ in range(cnt):
                    temp = numbers.pop(0)

                    smaller = findSmaller(avail_buttons, int(goal_channel[i]) + big)
                    if smaller != 11:
                        numbers.append(temp + str(smaller))

                    numbers.append(temp + str(int(goal_channel[i]) + big))

                    bigger = findBigger(avail_buttons, int(goal_channel[i]) + big)
                    if bigger != 11:
                        numbers.append(temp + str(bigger))

            elif small != 100 and big == 100:
                cnt = len(numbers)
                for _ in range(cnt):
                    temp = numbers.pop(0)

                    smaller = findSmaller(avail_buttons, int(goal_channel[i]) - small)
                    if smaller != 11:
                        numbers.append(temp + str(smaller))

                    numbers.append(temp + str(int(goal_channel[i]) - small))

                    bigger = findBigger(avail_buttons, int(goal_channel[i]) - small)
                    if bigger != 11:
                        numbers.append(temp + str(bigger))

            else:
                if small < big:
                    cnt = len(numbers)
                    for _ in range(cnt):
                        temp = numbers.pop(0)

                        smaller = findSmaller(avail_buttons, int(goal_channel[i]) - small)
                        if smaller != 11:
                            numbers.append(temp + str(smaller))

                        numbers.append(temp + str(int(goal_channel[i]) - small))

                        bigger = findBigger(avail_buttons, int(goal_channel[i]) - small)
                        if bigger != 11:
                            numbers.append(temp + str(bigger))

                elif big < small:
                    cnt = len(numbers)
                    for _ in range(cnt):
                        temp = numbers.pop(0)

                        smaller = findSmaller(avail_buttons, int(goal_channel[i]) + big)
                        if smaller != 11:
                            numbers.append(temp + str(smaller))

                        numbers.append(temp + str(int(goal_channel[i]) + big))

                        bigger = findBigger(avail_buttons, int(goal_channel[i]) + big)
                        if bigger != 11:
                            numbers.append(temp + str(bigger))

                else:
                    cnt = len(numbers)
                    for _ in range(cnt):
                        temp = numbers.pop(0)
                        smaller = findSmaller(avail_buttons, int(goal_channel[i]) + big)
                        if smaller != 11:
                            numbers.append(temp + str(smaller))

                        numbers.append(temp + str(int(goal_channel[i]) + big))

                        bigger = findBigger(avail_buttons, int(goal_channel[i]) + big)
                        if bigger != 11:
                            numbers.append(temp + str(bigger))

                        smaller = findSmaller(avail_buttons, int(goal_channel[i]) - small)
                        if smaller != 11:
                            numbers.append(temp + str(smaller))

                        numbers.append(temp + str(int(goal_channel[i]) - small))

                        bigger = findBigger(avail_buttons, int(goal_channel[i]) - small)
                        if bigger != 11:
                            numbers.append(temp + str(bigger))

    ans = []
    for temp in numbers:
        ans.append(abs(int(goal_channel) - int(temp)))
    return min(ans) + channel_length


sys.stdin = open('input.txt')
now = 100
avail_buttons = [True] * 10
goal_channel = input()
channel_length = len(goal_channel)
n = int(input())
broken_buttons = list(map(int, input().split()))
for i in broken_buttons:
    avail_buttons[i] = False
# 그냥 현재 채널에서 이동하는거
flag_0 = abs(int(goal_channel) - now)

# 현재 채널길이 - 1
flag_1 = smallChannel(avail_buttons, channel_length, goal_channel)

# 현재 채널 길이
flag_2 = sameChannel(avail_buttons, channel_length, goal_channel)

# 현재 채널 길이 + 1
flag_3 = bigChannel(avail_buttons, channel_length, goal_channel)

# print(flag_0, flag_1, flag_2, flag_3)
print(min(flag_0, flag_1, flag_2, flag_3))
