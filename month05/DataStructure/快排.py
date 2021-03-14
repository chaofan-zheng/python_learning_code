def quick_sort(li, first, last):
    if first >= last:
        return
    position = sort(li, first, last)
    quick_sort(li, first, position - 1)
    quick_sort(li, position + 1, last)


def sort(li, first, last):
    base = li[first]
    lcur = first + 1
    rcur = last
    while True:
        while li[lcur] <= base and lcur <= rcur:
            lcur += 1
        while li[rcur] >= base and lcur <= rcur:
            rcur -= 1
        if lcur < rcur:
            li[lcur], li[rcur] = li[rcur], li[lcur]
        else:
            li[rcur], li[first] = li[first], li[rcur]
            return rcur


list01 = [1, 2, 45, 65456, 423, 4, 14, 3, 2, 4, 3]
quick_sort(list01, 0, len(list01)-1)
print(list01)

