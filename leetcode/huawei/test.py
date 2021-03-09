list01=[1,2,3,4]
print(list01[0:2])
print(list01[1:3].index(2))

str01 = 'a bcde'
print(str01.split())
# 倒序
for i in range(len(list01)-1,-1,-1):
    print(list01[i])

str02 = 'aabcde'
str02=str02.replace(str02[0],'')
print(str02)
str02 = 'aabcde'
list_str = list(str02)
del list_str[0]
str02 = ''.join(list_str)
print(str02)

list01 = [0,1,2,3,4,5,6,7]
for i in range(2,8,3):
    print(i)
