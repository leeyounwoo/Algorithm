def solution(schedule):
    answer = 0
    temp123 = 0
    for subject_1 in schedule[0]:
        for subject_2 in schedule[1]:
            for subject_3 in schedule[2]:
                for subject_4 in schedule[3]:
                    for subject_5 in schedule[4]:
                        temp123 += 1
                        time = {'MO': {9: {0: False, 30: False},
                                       10: {0: False, 30: False},
                                       11: {0: False, 30: False},
                                       12: {0: False, 30: False},
                                       13: {0: False, 30: False},
                                       14: {0: False, 30: False},
                                       15: {0: False, 30: False},
                                       16: {0: False, 30: False},
                                       17: {0: False, 30: False},
                                       18: {0: False, 30: False},
                                       19: {0: False, 30: False},
                                       20: {0: False, 30: False},
                                       21: {0: False, 30: False},
                                       22: {0: False, 30: False}
                                       },
                                'TU': {9: {0: False, 30: False},
                                       10: {0: False, 30: False},
                                       11: {0: False, 30: False},
                                       12: {0: False, 30: False},
                                       13: {0: False, 30: False},
                                       14: {0: False, 30: False},
                                       15: {0: False, 30: False},
                                       16: {0: False, 30: False},
                                       17: {0: False, 30: False},
                                       18: {0: False, 30: False},
                                       19: {0: False, 30: False},
                                       20: {0: False, 30: False},
                                       21: {0: False, 30: False},
                                       22: {0: False, 30: False}
                                       },
                                'WE': {9: {0: False, 30: False},
                                       10: {0: False, 30: False},
                                       11: {0: False, 30: False},
                                       12: {0: False, 30: False},
                                       13: {0: False, 30: False},
                                       14: {0: False, 30: False},
                                       15: {0: False, 30: False},
                                       16: {0: False, 30: False},
                                       17: {0: False, 30: False},
                                       18: {0: False, 30: False},
                                       19: {0: False, 30: False},
                                       20: {0: False, 30: False},
                                       21: {0: False, 30: False},
                                       22: {0: False, 30: False}
                                       },
                                'TH': {9: {0: False, 30: False},
                                       10: {0: False, 30: False},
                                       11: {0: False, 30: False},
                                       12: {0: False, 30: False},
                                       13: {0: False, 30: False},
                                       14: {0: False, 30: False},
                                       15: {0: False, 30: False},
                                       16: {0: False, 30: False},
                                       17: {0: False, 30: False},
                                       18: {0: False, 30: False},
                                       19: {0: False, 30: False},
                                       20: {0: False, 30: False},
                                       21: {0: False, 30: False},
                                       22: {0: False, 30: False}
                                       },
                                'FR': {9: {0: False, 30: False},
                                       10: {0: False, 30: False},
                                       11: {0: False, 30: False},
                                       12: {0: False, 30: False},
                                       13: {0: False, 30: False},
                                       14: {0: False, 30: False},
                                       15: {0: False, 30: False},
                                       16: {0: False, 30: False},
                                       17: {0: False, 30: False},
                                       18: {0: False, 30: False},
                                       19: {0: False, 30: False},
                                       20: {0: False, 30: False},
                                       21: {0: False, 30: False},
                                       22: {0: False, 30: False}
                                       }
                                }
                        a = [subject_1, subject_2, subject_3, subject_4, subject_5]
                        for sub in a:
                            temp1 = sub.split()
                            if len(temp1) == 2:
                                day = temp1[0]
                                hour_min = temp1[1].split(':')
                                hour = int(hour_min[0])
                                minute = int(hour_min[1])
                                if minute == 30:
                                    if time[day][hour][30] or time[day][hour+1][0] or time[day][hour+1][30] or time[day][hour + 2][0] or time[day][hour + 2][30] or time[day][hour + 3][0]:
                                        break
                                    time[day][hour][30] = True
                                    time[day][hour+1][0] = True
                                    time[day][hour+1][30] = True
                                    time[day][hour + 2][0] = True
                                    time[day][hour + 2][30] = True
                                    time[day][hour + 3][0] = True
                                else:
                                    if time[day][hour][30] or time[day][hour+1][0] or time[day][hour+1][30] or time[day][hour + 2][0] or time[day][hour + 2][30] or time[day][hour][0]:
                                        break
                                    time[day][hour][0] = True
                                    time[day][hour][30] = True
                                    time[day][hour + 1][0] = True
                                    time[day][hour + 1][30] = True
                                    time[day][hour + 2][0] = True
                                    time[day][hour + 2][30] = True
                            else:
                                day1 = temp1[0]
                                hour_min1 = temp1[1].split(':')
                                hour1 = int(hour_min1[0])
                                minute1 = int(hour_min1[1])
                                if minute1 == 30:
                                    if time[day1][hour1][30] or time[day1][hour1+1][0] or time[day1][hour1+1][30]:
                                        break
                                    time[day1][hour1][30] = True
                                    time[day1][hour1 + 1][0] = True
                                    time[day1][hour1 + 1][30] = True
                                else:
                                    if time[day1][hour1][30] or time[day1][hour1+1][0] or time[day1][hour1][0]:
                                        break
                                    time[day1][hour1][0] = True
                                    time[day1][hour1][30] = True
                                    time[day1][hour1 + 1][0] = True

                                day2 = temp1[2]
                                hour_min2 = temp1[3].split(':')
                                hour2 = int(hour_min2[0])
                                minute2 = int(hour_min2[1])
                                if minute2 == 30:
                                    if time[day2][hour2][30] or time[day2][hour2 + 1][0] or time[day2][hour2 + 1][30]:
                                        break
                                    time[day2][hour2][30] = True
                                    time[day2][hour2 + 1][0] = True
                                    time[day2][hour2 + 1][30] = True
                                else:
                                    if time[day2][hour2][0] or time[day2][hour2][30] or time[day2][hour2 + 1][0]:
                                        break
                                    time[day2][hour2][0] = True
                                    time[day2][hour2][30] = True
                                    time[day2][hour2 + 1][0] = True
                        else:
                            answer += 1

    return answer


print(solution([["MO 12:00 WE 14:30", "MO 12:00", "MO 15:00", "MO 18:00"],
                ["TU 09:00", "TU 10:00", "TU 15:00", "TU 18:00"],
                ["WE 09:00", "WE 12:00", "WE 15:00", "WE 18:00"],
                ["TH 09:30", "TH 11:30", "TH 15:00", "TH 18:00"],
                ["FR 15:00", "FR 15:00", "FR 15:00", "FR 15:00"]]))
