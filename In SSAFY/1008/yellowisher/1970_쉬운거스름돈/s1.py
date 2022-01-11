T = int(input())
for tc in range(T):
    money = int(input())
    money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    result = [0, 0, 0, 0, 0, 0, 0, 0]
    print("#{}".format(tc + 1))
    for i in range(len(money_list)):
        cnt = money // money_list[i]
        result[i] += cnt
        money -= cnt * money_list[i]
    print(' '.join(map(str, result)))