import pytest

canshu=[{"user":"admin","psw":""}]

#装饰器usefixtures用来替代test_01(login2)
@pytest.mark.parametrize("login2",canshu,indirect=True)
#@pytest.mark.usefixtures("login2")
def test_01(login2):
    result=login2
    print("执行")

if __name__ == '__main__':
    pytest.main(["-s","test_05.py"])