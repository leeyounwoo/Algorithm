def solution(n, k, cmd):
    peoples = [i for i in range(n)]
    start = [i for i in range(n)]
    now_index = k
    delete_stack = []
    for command in cmd:
        command_type = command[0]
        if command_type == "D":
            now_index += int(command[-1])
        elif command_type == "U":
            now_index -= int(command[-1])

        elif command_type == "C":
            delete_stack.append([now_index, peoples[now_index]])
            if now_index == len(peoples) - 1:
                peoples.pop()
                now_index = len(peoples) - 1
            else:
                peoples.pop(now_index)
        elif command_type == "Z":
            temp = delete_stack.pop()
            insert_index = temp[0]
            insert_value = temp[1]
            if now_index < insert_index:
                peoples.insert(insert_index, insert_value)
            else:
                peoples.insert(insert_index, insert_value)
                now_index += 1

        print(command)
        print(peoples, now_index)
        print(delete_stack)
        print()
        # print(len(command))


    answer = ''
    for i in range(len(start)):
        if start[i] in peoples:
            answer += 'O'
        else:
            answer += 'X'

    return answer

print(solution(8, 5, ["C", "U 2", "Z"]))
# print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))