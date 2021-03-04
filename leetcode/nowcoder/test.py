import numpy as np

a = np.repeat(np.arange(5).reshape([1,-1]),10,axis = 0)+10.0
b = np.random.randint(5, size= a.shape)
c = np.argmin(a*b, axis=1)
b = np.zeros(a.shape)
b[np.arange(b.shape[0]), c] = 1
print(b)
print((3,2)<('a','b'))

# python2 和python3 有哪些区别：
# https://www.zhihu.com/question/19698598
bit = input("Enter a binary digit:")
if bit == 0 or bit == 1: # 千万不能这么写，bit==0 or bit ==1
    print ("your input is" ,bit)
else:
    print ("your input is invalid")