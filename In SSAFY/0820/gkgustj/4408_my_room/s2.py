def find_room(room):
    # 방으로 돌아간 학생을 표시하기 위한 변수
    student = [i for i in range(N)]
    # 방으로 돌아가는데 걸리는 시간을 저장하는 변수
    time = 0

    # N명의 학생들에 대해서
    for i in range(N):
        # i가 이미 방으로 돌아갔다면 break
        if i not in student:
            break

        student.remove(i)

        # 현재 사용중인 복도를 표시
        for j in range(room[i][0], room[i][1]+1):
            corridor[j] = 1

        # 동시에 복도를 사용할 수 있는 학생이 있는지 확인
        for k in range(i+1, N):
            success = 0
            for l in range(room[k][0], room[k][1]+1):
                # 만약 복도가 이미 사용 중이라면, 반복문 종료
                if corridor[l]:
                    break
                # 복도가 사용 중이 아니라면, success를 1더하고 계속
                else:
                    corridor[l] = 1
                    success += 1

                # success가 room[k][1]-room[k][0]+1이라면 반복문이 모두 돌아간 것
                # 즉, 학생이 동시에 방으로 돌아간 것
                if success == room[k][1]-room[k][0]+1:
                    student.remove(k)

        # i가 방에 돌아갔으므로 시간 + 1
        time += 1

    return time


T = int(input())

for t in range(1, T+1):
    N = int(input())

    room =[]
    # 학생들의 방 위치를 복도를 기준으로 저장
    '''
    stu_room 1 3 5 7 ... 399
    corridor 0 1 2 3 ... 199
    stu_room 2 4 6 8 ... 400
    '''
    for n in range(N):
        a, b = (map(int, input().split()))
        temp = []
        for a_b in (a, b):
            if a_b % 2:
                a_b = (a_b - 1) // 2
            else:
                a_b = (a_b - 2) // 2
            temp.append(a_b)
        room.append(temp)

    # 사용 중인 복도를 표시할 리스트
    corridor = [0]*200

    time = find_room(room)

    print('#{} {}'.format(t, time))