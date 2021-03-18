"""即**含有`__enter__`和`__exit__`方法的对象就是上下文管理器。**"""


class Foo(object):

    def __init__(self):
        print('实例化一个对象')

    def __enter__(self):
        print('进入')
        return 'enter的返回值'

    def __exit__(self, exc_type, exc_val, exc_tb): # 但是不管怎样都会执行，相当于finally
        print('退出')
        # return True  # 忽略错误
        return False  # 把错误抛出，让with之外的语句去处理


obj = Foo()

with obj as o:
    print(o)
    print('正在执行')

