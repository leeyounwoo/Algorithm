import sys

sys.stdin = open('input.txt')
words = input()
temp = ''
numbers = []
for i in range(len(words)):
    if words[i] != '+' and words[i] != '-':
        temp += words[i]
        if i == len(words) - 1:
            numbers.append(int(temp))
    else:
        numbers.append(int(temp))
        numbers.append(words[i])
        temp = ''
# print(numbers)
ans = 0
temp = 0
flag = False
for i in range(len(numbers)):
    if numbers[i] == '+':
        continue
    elif numbers[i] == '-':
        ans -= temp
        temp = 0
        flag = True

    else:
        if flag:
            temp += numbers[i]
        else:
            ans += numbers[i]
    # print(numbers[i])
    # print('temp', temp)
    # print('ans', ans)
print(ans - temp)
