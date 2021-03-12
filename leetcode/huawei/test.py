list01 = [1, 2, 3, 4]
print(list01[0:2])
print(list01[1:3].index(2))

str01 = 'a bcde'
print(str01.split())
# 倒序
for i in range(len(list01) - 1, -1, -1):
    print(list01[i])

str02 = 'aabcde'
str02 = str02.replace(str02[0], '')
print(str02)
str02 = 'aabcde'
list_str = list(str02)
del list_str[0]
str02 = ''.join(list_str)
print(str02)

list01 = [0, 1, 2, 3, 4, 5, 6, 7]
for i in range(2, 8, 3):
    print(i)

print(23_110 + 11)

list01 = ['a', 'a']
print(list01.count('a'))
print(list01[:1])

del list01[0]
print(list01)
list01 = ['dd', 'da', 'dc', 'dword', 'd']
list01.sort(key=lambda x: -len(x))
print(list01)
print('dd' > 'da')
print()

list01 = ['a', 'a']
print(list01.count('a'))
print(list01[:3])


class A:
    def __init__(self):
        self.a = 'a'

    def functionA(self):
        print('This is functionA')


class B(A):

    def functionA(self):
        print('This is overrode functionA')

    def functionB(self):
        print('This is functionB')


b = B()
b.functionA()
b.functionB()
print(b.a)
