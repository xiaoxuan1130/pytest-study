#coding:utf-8

import pytest

#标记失败fail

canshu=[{"user":"admin","psw":""}]

@pytest.mark.parametrize("login2",canshu,indirect=True)
class Test_000():

    def test_01(self,login2):
        result=login2
        assert result==True

    def test_02(self,login2):
        result=login2
        if not result:
            pytest.fail("登录不成功，标记为fail02")
        assert 1==1

    def test_03(self,login2):
        result=login2
        if not result:
            pytest.fail("登录不成功，标记为fail03")
        assert 1==1