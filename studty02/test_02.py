import pytest

def login(username,password):
    return{"code":0,"msg":"success!"}

test_datas=[
    ({"username":"xiaoxuan1","password":"123456"},"success!"),
    ({"username":"xiaoxuan2","password":"123456"},"success!"),
    ({"username":"xiaoxuan3","password":"123456"},"success!"),
]

@pytest.mark.parametrize("test_input,expected",
                         test_datas,
                         ids=[
                             "输入正确账号，密码，登录成功",
                             "输入错误账号，密码，登录失败",
                             "输入正确账号，密码，登录成功",
                         ]
                         )
def test_login(test_input,expected):
    result=login(test_input["username"],test_input["password"])
    assert result["msg"]==expected