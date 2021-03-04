"""
链接：https://www.nowcoder.com/questionTerminal/3897c2bcc87943ed98d8e0b9e18c4666
来源：牛客网

输入包括多组测试数据。
每组输入第一行是两个正整数N和M（0 < N <= 30000,0 < M < 5000）,分别代表学生的数目和操作的数目。
学生ID编号从1编到N。
第二行包含N个整数，代表这N个学生的初始成绩，其中第i个数代表ID为i的学生的成绩
接下来又M行，每一行有一个字符C（只取‘Q’或‘U’），和两个正整数A,B,当C为'Q'的时候, 表示这是一条询问操作，他询问ID从A到B（包括A,B）的学生当中，成绩最高的是多少
当C为‘U’的时候，表示这是一条更新操作，要求把ID为A的学生的成绩更改为B。
"""



while True:
    try:
        list01 = input().split()
        stu_num , ope_num = list01[0],list01[1]
        mark = input().split()
        mark = [int(item) for item in mark]
        for i in range(int(ope_num)):
            command = input().split()
            head = command[0]
            num1,num2 = sorted([int(command[1]),int(command[2])])
            if head == 'Q':
                print(max(mark[(num1 - 1):num2]))
            else:
                mark[num1 - 1] = num2
    except:
        break
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

