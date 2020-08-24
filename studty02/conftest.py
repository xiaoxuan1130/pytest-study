import pytest

# @pytest.hookimpl(hookwrapper=True,tryfirst=True)
# def pytest_runtest_makereport(item,call):
#     print("----------------")
#
#     out =yield
#     print("用例执行结果",out)
#
#     report =out.get_result()
#
#     print("测试报告：%s" %report)
#     print("步骤：%s" %report.when)
#     print("nodeid:%s"%report.nodeid)
#     print("description:%s"%str(item.function.__doc__))
#     print("运行结果：%s"%report.outcome)