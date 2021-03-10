while True:
    try:
        index = int(input())
        ope = int(input())
        list01 = []
        for i in range(ope):
            list01.append(input())
        begin_word = list01[index]
        del list01[index]
        list01.sort()
        list01.sort(key=lambda x: -len(x))
        i = 0
        while list01 and i < len(list01):
            if list01[i][0] == begin_word[-1]:
                begin_word += list01[i]
                del list01[i]
                i = 0
                continue
            else:
                i += 1
        print(begin_word)
    except:
        break
