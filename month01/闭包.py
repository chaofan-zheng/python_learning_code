def add(a):
    def func01(b):
        return a + b

    return func01


add5 = add(5)
print(add5(5))  # 10
