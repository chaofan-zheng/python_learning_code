def test(*args, **kwargs):
    print(args, kwargs)


tuple01 = ('a', 'b')
dict01 = {'name': 'Aiden', 'age': 18}
test(*tuple01, **dict01)
# 等同于
test('a', 'b', name='Aiden', age=18)
# ('a', 'b') {'name': 'Aiden', 'age': 18}
# ('a', 'b') {'name': 'Aiden', 'age': 18}
