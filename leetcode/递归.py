"""
    递归
"""


def di_gui(n):
    print(n, "<===1====>")
    if n > 0:
        di_gui(n - 1)
    print(n, '<===2====>')


di_gui(5)  # 外部调用后打印的结果是？
# 5 <===1====>
# 4 <===1====>
# 3 <===1====>
# 2 <===1====>
# 1 <===1====>
# 0 <===1====>
# 0 <===2====>
# 1 <===2====>
# 2 <===2====>
# 3 <===2====>
# 4 <===2====>
# 5 <===2====>
# 递归的执行过程：首先，递归会执行“去”的过程，只需要满足终止条件，就会一直在函数内，带着更新的参数，调用函数自身，
# 注意：到内部调用函数， 以下面的代码不会被执行，而是暂停阻塞；
# 此时 随着函数每调用一次自身，还没有触发 返回值和到达终止条件，等同于在原来的基础上不断“向下/向内”开辟新的内存空间，记住，每次调用一次函数，就不是处在同一空间（想象下《盗梦空间》里的情景，梦中梦，都是处于不同的空间）

# 什么时候“递”去的过程结束？记住有两种情况>>> 一是：当前这层空间函数全部执行结束（终止条件），二是：执行到了return 返回值，直接返回；
# 第二种，有返回值的递归的方法
class DiGuiCalculate:
    def di_gui(self, n):
        if n < 1:
            return 0
        return n + self.di_gui(n - 1)


di_gui_calculate = DiGuiCalculate()
print(di_gui_calculate.di_gui(10))