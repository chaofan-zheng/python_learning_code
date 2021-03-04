#
# def solution(input_str):
#     lines = input_str.split('\n')
#     # stu_num, ope_num = int(lines[0].split(' ')[0]),int(lines[0].split(' ')[1])
#     mark = lines[1].split(' ')
#     mark = [int(item) for item in mark]
#     ope_list = lines[2:]
#     for operation in ope_list:
#         head = operation.split(' ')[0]
#         num1 = int(operation.split(' ')[1])
#         num2 = int(operation.split(' ')[2])
#         if head == 'Q':
#             print(max(mark[(num1 - 1):num2]))
#         else:
#             mark[num1 - 1] = num2
#
#
#
# input_str = """10 2
# 43 36 1 27 2 4 11 25 32 49
# U 7 57
# Q 1 2"""
# solution(input_str)



while True:
    ope_num = input().split(' ')[1]
    mark_list = input().split(' ')
    mark_list = [int(item) for item in mark_list]
    for i in range(int(ope_num)):
        input_str = input()
        operation = input_str.split(' ')[0]
        num1 = int(input_str.split(' ')[1])
        num2 = int(input_str.split(' ')[2])
        if num1 > num2:
            num1,num2=num2,num1
        if operation == 'Q':
            print(max(mark_list[(num1 - 1):num2]))
        else:
            mark_list[num1-1]=num2

# while True:
#     lines = input().split('\n')
#     mark = lines[1].split(' ')
#     mark = [int(item) for item in mark]
#     ope_list = lines[2:]
#     for operation in ope_list:
#         head = operation.split(' ')[0]
#         num1 = int(operation.split(' ')[1])
#         num2 = int(operation.split(' ')[2])
#         if head == 'Q':
#             print(max(mark[(num1 - 1):num2]))
#         else:
#             mark[num1 - 1] = num2

# 答案
while True:
    try:
        a, b = map(int, input().split())
        grades = list(map(int, input().split()))
        for i in range(b):
            command = input().split()
            if command[0] == "Q":
                start, end = sorted([int(command[1]), int(command[2])])
                print(max(grades[start - 1:end]))
            else: grades[int(command[1]) - 1] = int(command[2])
    except:
        break

