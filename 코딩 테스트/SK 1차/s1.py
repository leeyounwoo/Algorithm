def solution(money, costs):
    coins = [1, 5, 10, 50, 100, 500]
    costs_for_1 = {i: coins[i] / costs[i] for i in range(len(costs))}
    sorted_cost = sorted(costs_for_1.items(), key=lambda x: x[1], reverse=True)

    new_cost = []
    for i in range(len(sorted_cost)):
        new_cost.append([coins[sorted_cost[i][0]], costs[sorted_cost[i][0]]])

    answer = 0
    for i in range(len(new_cost)):
        a, money = divmod(money, new_cost[i][0])
        answer += a * new_cost[i][1]
        if not money:
            break

    return answer

print(solution(4578, [1, 4, 99, 35, 50, 1000]))