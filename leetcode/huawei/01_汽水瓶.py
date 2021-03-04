while True:
    num = int(input())
    if not num:
        break
    count = 0
    while True:
        if num - 3 >= 0:
            num -= 2
            count += 1
        elif num == 2:
            count += 1
            break
        else:
            break
    print(count)
