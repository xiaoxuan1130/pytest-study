import pytest


class TestClass:
    def test_01(self):
        x="this"
        assert 'w' in x

if __name__ == '__main__':
    pytest.main(['-v', 'test_class.py'])