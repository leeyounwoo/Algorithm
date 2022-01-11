import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    print('#{}'.format(tc), end=" ")
    num, change = map(int, input().split())
    num = str(num)
    li = []
    for i in num:
        li.append(i)

    sorted_li = sorted(li, reverse=True)
    lis = li[:]
    #print(sorted_li) # ['3', '2', '1'] ['7', '7', '3', '2'] ['8', '8', '8', '3', '2']
    for i in range(len(li)):

        if li[i] != sorted_li[i] and change != 0:
            locate = num.rfind(sorted_li[i]) # 32888 4 3
            num1 = num[::-1]
            num1 = num1.replace(sorted_li[i], '0', 1)
            num = num1[::-1]
            #print(num)
            li[i], li[locate] = li[locate], li[i]
            change -= 1
        elif li[i] == sorted_li[i] and change != 0:
            if i == len(li):
                change = 0
                break
            else:
                continue
        if change == 0:
            break

    #print(li) # 맥스순서대로 놓고 첫번째 맥스를 맨앞이랑 바꾸고 두번째 자리는 두번째 맥스랑 바꾸고,,
    total = ''
    for i in li:
        total += str(i)
    print(total) # 82883