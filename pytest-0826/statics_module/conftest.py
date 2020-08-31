#coding=utf-8
import pytest
import os
import yaml
import requests
from requests.cookies import RequestsCookieJar


def getData():
    path=os.path.dirname(os.path.abspath(__file__))
    with open('application.yaml','r',encoding='utf-8') as f:
        return yaml.load(f)

@pytest.fixture("session")
def login(request):
    datas=getData()
    url=datas.get("url")
    result=requests.get(url)
    jeeplusId=result.cookies['jeeplus.session.id']

    #登录
    username = datas.get("username")
    password = datas.get("password")
    url=url+"a/login"
    payload={'username':username,'password':password}
    cookies = {"jeeplus.session.id": jeeplusId}
    result=requests.post(url,data=payload,cookies=cookies)

    yield (jeeplusId)