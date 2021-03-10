while True:
    try:
        recorder_num = int(input())
        res_list = []
        for i in range(recorder_num):
            inputstr=input()
            if not inputstr:
                continue
            records = inputstr.split()
            absent_num = records.count('absent')
            if absent_num > 1:
                res_list.append('false')
                continue
            for i in range(len(records)):
                if i + 7 <= (len(records)):
                    if records[i:i + 7].count('present') < 4:
                        res_list.append('false')
                        break
                    if records[i] in ['late', 'leaveearly'] and records[i + 1] in ['late', 'leaveearly']:
                        res_list.append('false')
                        break
                else:
                    if i == len(records)-1:
                        res_list.append('true')
                        break
                    if records[i] in ['late', 'leaveearly'] and records[i + 1] in ['late', 'leaveearly']:
                        res_list.append('false')
                        break
        for item in res_list:
            print(item, end=' ')
        print()
    except Exception as e:
        break
