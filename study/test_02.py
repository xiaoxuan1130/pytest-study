#coding:utf-8
import pytest
##request.param 登录

test_login_data=[("admin","11111"),("admin","")]
test_user_data=["admin","admin1"]
test_user_data1=[{"user":"admin1","psw":"1111"},
                {"user":"admin1","psw":""}]
def login(user,psw):
    print("账号:%s"%user)
    print("密码：%s"%psw)
    if psw:
        return True
    else:
        return False

# @pytest.mark.parametrize("user,psw",test_login_data)
# def test_login(user,psw):
#     result=login(user,psw)
#     assert result==True,"失败原因：密码为空"

@pytest.mark.parametrize("login1",test_login_data,indirect=True)
def test_login1(login1):
    a=login1
    print("测试用例中login的返回值：%s" %a[0])
    assert a!=""

@pytest.mark.webtest
@pytest.mark.parametrize("login2",test_user_data1,indirect=True)
def test_login2(login2):
    a=login2
    print("返回的login2的用户名为：%s" %a)

if __name__ == "__main__":
    #pytest -s -v test_02.py::test_login2
    pytest.main(["-s", "test_02.py"])