import sys
sys.stdin = open('input.txt')


for _ in range(10):   # 테스트케이스 10번
    test_len = int(input())  # test_len = 건물 수
    # total_list = list()      # 건물 높이 리스트 초기
    # for _ in range(255):
    #   total_list.append([0 for i in range(test_len)])
    total_list = [[0 for i in range(test_len)] for _ in range(255)] # 건물 높이 리스트 초기
    building_height_list =  input().split(" ")

    for i in range(test_len):
        for k in range(int(building_height_list[i])):
            total_list[k][i] = 1

    rtv_count = 0

    for floor in total_list:
        for idx, val in enumerate(floor):
            if val == 1 and floor[idx-2] == 0 and floor[idx-1] == 0 and floor[idx+1] == 0 and floor[idx+2] == 0 :
                rtv_count += 1

    print("#1 {}".format(rtv_count))