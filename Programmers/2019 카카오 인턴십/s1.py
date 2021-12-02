from pprint import pprint
def solution(board, moves):
    answer = 0
    length = len(board)
    array = [[0] * length for _ in range(length)]
    # pprint(array)
    for i in range(length):
        for j in range(length):
            array[i][j] = board[j][i]
    # pprint(array)
    basket = []
    for move in moves:
        for j in range(length):
            if array[move-1][j]:
                basket.append(array[move-1][j])
                array[move-1][j] = 0
                break
        # print('move', move)
        # print(basket)
        # print()
        if len(basket) >= 2 and basket[len(basket)-1] == basket[len(basket)-2]:
            basket.pop()
            basket.pop()
            answer += 2
    return answer


print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))