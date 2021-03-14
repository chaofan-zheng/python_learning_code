def verify_permission(func):
    print('权限验证')  # 进行权限验证的新功能

    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


def verify_activeness(func):
    print('激活认证')

    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


# def login(username):
#     print(f'{username}登录成功')
#
#
# login = verify_permission(login)
# login('Aiden')  # 权限验证，Aiden登录成功


# @verify_permission(verify_activeness)
# def login(username):
#     print(f'{username}登录成功')
# 权限验证
# 激活认证
# Aiden登录成功

@verify_activeness
@verify_permission
def login(username):
    print(f'{username}登录成功')  # 要反一下的，permission先执行


login('Aiden')  # 权限验证，Aiden登录成功
