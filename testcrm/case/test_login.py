import pytest,json,logging
from testcrm.logger.Loggers import Loggers
log=Loggers(level=logging.INFO,className="test_login")
test_user_data=[{"username":"test003","password":"epipe123"}]

@pytest.mark.parametrize("login",test_user_data,indirect=True)
@pytest.mark.webtest
def test_getCustomerList(login):
    request=login
    url="http://192.168.3.171:8182/ucloud-crm/a/customerinfo/customerInfo/data?type=0"
    r=request.post(url)
    code=r.status_code
    result=json.loads(r.text)
    totals=result.get("total")
    datas=result.get("rows")
    log.logger.info("返回总条数为%s"%totals)
    # for data in datas:
    #     log.logger.info(str(data))

@pytest.mark.parametrize("login",test_user_data,indirect=True)
def test_getCustomerById(login):
    request=login
    url="http://192.168.3.171:8182/ucloud-crm/a/customerinfo/customerInfo/data?type=0&id=95de2f2c5ad141ea826299eff1d93551"
    r=request.post(url)
    code = r.status_code
    result=json.loads(r.text)
    data=result.get("rows")[0]
    log.logger.info("根据id获取信息%s"%str(data))




if __name__ == '__main__':
    #pytest.main(["-s", "test_login.py"])
    pytest.main(["-s", "test_login.py", "-m='not webtest'"])