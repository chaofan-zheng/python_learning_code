weight = {'3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, '10': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12, '2': 13,
          'joker': 14, 'JOKER': 15}
while True:
    try:
        left, right = input().split('-')
        llist = left.split()
        rlist = right.split()
        rlen = len(rlist)
        llen = len(llist)
        if rlen == 4:
            if llen == 2:
                # 炸弹，王的情况
                if llist[0] == 'joker' or llist[0] == 'JOKER':
                    print(left)
                    continue
                else:
                    print(right)
            if llen == 4:
                if weight[llist[0]] > weight[rlist[0]]:
                    print(left)
                    continue
                else:
                    print(right)
                    continue
            else:
                print(left)
                continue
        elif rlen == 2:
            if rlist[0] == 'joker' or rlist[0] == 'JOKER':
                print(right)
                continue
            elif llen == 4:
                print(left)
                continue
            elif llen == 2:
                if weight[llist[0]] > weight[rlist[0]]:
                    print(left)
                    continue
                else:
                    print(right)
                    continue
            else:
                print('ERROR')
                continue
        else:
            if llen == 4:
                print(left)
                continue
            elif llen == 2:
                if llist[0] == 'joker' or llist[0] == 'JOKER':
                    print(left)
                    continue
                else:
                    print('ERROR')
                    continue
            elif llen == rlen:
                if weight[llist[0]]> weight[rlist[0]]:
                    print(left)
                    continue
                else:
                    print(right)
                    continue
            else:
                print('ERROR')
                continue

    except:
        break

# #Python版
# #一楼正解， 只能是牌中的一种。
# # -*- coding:utf-8 -*-
# import sys
#
# if __name__ == '__main__':
#     while True:
#         tp = sys.stdin.readline().strip()
#         if not tp:
#             break
#         if 'joker JOKER' in tp:
#             print 'joker JOKER'
#         else:
#             strs = ['3','4','5','6','7','8','9','10','J','Q','K','A','2','joker','JOKER']
#             s1,s2 = tp.split('-')
#             ss1 = s1.split(' ')
#             ss2 = s2.split(' ')
#             len1 = len(ss1)
#             len2 = len(ss2)
#             if len1 ==4 and len2!=4:
#                 print s1
#             elif len2==4 and len1!=4:
#                 print s2
#             elif len1==len2:
#                 ind1 = strs.index(ss1[0])
#                 ind2 = strs.index(ss2[0])
#                 if ind1>ind2:
#                     print s1
#                 elif ind1<ind2:
#                     print s2
#             else:
#                     print 'ERROR'
