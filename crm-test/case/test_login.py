import pytest

test_user_data=[{"username":"test03","password":"epipe123"}]

@pytest.mark.parametrize("login",test_user_data,indirect=True)
def test_getUser(login):
    a=login

if __name__ == '__main__':
    pytest.main("-s","test_login.py")