#coding=utf-8

import pytest
import allure
import os,json
import yaml
import requests
from logger import logger


def get_data():
    path = os.path.dirname(os.path.abspath(__file__))
    with open('config.yaml', 'r', encoding='utf-8') as f:
        return list(yaml.safe_load_all(f))

def getEnv():
    path = os.path.dirname(os.path.abspath(__file__))
    with open('application.yaml', 'r', encoding='utf-8') as f:
        return yaml.load(f).get("url")

url=getEnv()

@allure.story("平面图接口测试")
class Test_api():

    @allure.step("接口")
    @pytest.mark.parametrize("datas", get_data())
    def test_interface(self,datas):
        if datas['method'] == 'get':
            r = requests.get(url=url+datas['url'])
            logger.info(r.text)
        if datas['method'] == 'post':
            r = requests.post(url=url+datas['url'], json=datas["dict1"])
            logger.info(r.text)
        assert datas['except'] in json.dumps(r.json(), ensure_ascii=False)

