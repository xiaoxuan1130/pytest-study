#coding:utf-8

import pytest

# @pytest.fixture()
# def login():
#     print("输入账号，密码登录")
#     return "success"

#mark单个标签
# def pytest_configure(config):
#    config.addinivalue_line(
#        "markers", "webtest"   # test 是标签名
#         )

#mark多个标签
# def pytest_configure(config):
#     marker_list = ["test1","test2","test3"]  # 标签名集合
#     for markers in marker_list:
#         config.addinivalue_line(
#             "markers", markers
#         )


@pytest.fixture(scope="session")
def login1(request):
    user=request.param
    print("登录账号:%s登录密码：%s" % (user[0],user[1]))
    return user

@pytest.fixture(scope="session")
def login2(request):
    user=request.param["user"]
    psw=request.param["psw"]
    print("登录账号：%s,登录密码：%s" % (user,psw))
    if psw:
        return True
    else:
        return False
