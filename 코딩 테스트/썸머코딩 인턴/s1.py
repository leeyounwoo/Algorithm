def solution(atmos):
    # mask를 착용한 날짜를 담는 배열
    mask = []
    for i in range(len(atmos)):
        # a 는 미세먼지 농도, b는 초미세먼지 농도
        a, b = atmos[i][0], atmos[i][1]
        # 어느 하나라도 나쁨 이상
        if a > 80 or b > 35:
            # 만약 첫 마스크라면 조건 필요 없음
            if not mask:
                mask.append(i)

            # 첫 마스크가 아니라면 재사용 가능 여부 확인
            else:
                # 이전에 추가한 마스크의 날짜
                prev = mask[-1]
                # 이전에 마스크 사용했을 때가 미세먼지 농도, 초미세먼지 농도 모두 매우 나쁨인 경우
                # 새로운 마스크
                if prev == -1:
                    mask.append(i)
                # 그렇지 않은 경우
                else:
                    # 만약 3일이 지난 마스크면 새로운 마스크
                    if i - prev >= 3:
                        mask.append(i)
            # 오늘 미세먼지 농도와 초미세먼지 농도가 매우 나쁨인 경우, 날짜를 -1
            if a >= 151 and b >= 76:
                mask[-1] = -1


    return len(mask)

# print(solution([[140, 90], [177, 75], [95, 45], [71, 31], [150, 30], [80, 35], [72, 33], [166
# , 81], [151, 75]]))
print(solution([[166, 81] ,[166, 81],[166, 81],[166, 81],[166, 81],[166, 81],[166, 81],[166, 81]]))