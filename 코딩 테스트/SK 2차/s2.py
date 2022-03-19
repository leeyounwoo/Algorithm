from pprint import pprint

def solution(arr, processes):
    print(arr)
    for i in range(len(processes)):
        print(processes[i])
    time = {t: [] for t in range(20)}
    array = {index:[] for index in range(len(arr))}
    for i in range(len(processes)):
        command = processes[i].split()
        for c_i in range(1, len(command)):
            command[c_i] = int(command[c_i])

        for c_i in range(command[3], command[4]+1):
            array[c_i].append(command)
        for t in range(command[1], command[1] + command[2]):
            time[t].append(i)
            # if command[0] == "read":
            #     time[t].append([command[0], int(command[3]), int(command[4])])
            # else:
            #     time[t].append([command[0], int(command[3]), int(command[4]), int(command[5])])
    # pprint(time)
    for index in range(len(arr)):
        array[i].sort(key=lambda x: x[1])
    pprint(array)
    for i in range(1, 20):
        for key in range(len(arr)):
            for command in array[key]:
                if command[1] == i:
                    print('find', i, command)
                    if command[0] == "write":
                        pass
                    else:
                        flag =
                        for f_i in range(command[3], command[4]+1):

    answer = []
    return answer

# 정답: ["24","3415","4922","12492215","13"]
print(solution(["1","2","4","3","3","4","1","5"], ["read 1 3 1 2","read 2 6 4 7","write 4 3 3 5 2","read 5 2 2 5","write 6 1 3 3 9", "read 9 1 0 7"]))
# print(solution())