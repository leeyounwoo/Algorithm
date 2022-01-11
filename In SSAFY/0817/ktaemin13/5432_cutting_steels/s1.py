import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    pipe_list = input()

    new_pipe = []

    for pipe_change in pipe_list:
        if pipe_change == '(':
            new_pipe.append(1)
        else:
            new_pipe.append(-1)

    result = 0
    for pipe_piece in new_pipe:

        result += pipe_piece
        if pipe_piece == -1 and result == 0:
            continue

        if result == 0:
            pass


    print(new_pipe)

    print('#{0} {1}'.format(tc+1, new_pipe))
