import pytest

@pytest.mark.usefixtures("start")
class Test_02():

    def test_01(self):
        print("------用例1-----")

    def test_02(self,start):
        print("------用例2-----"+start)