#coding:utf-8
import os
import pytest
import yaml
import requests
import json

from logger import logger


def realYaml():
    path = os.path.dirname(os.path.abspath(__file__))
    with open('config.yaml', 'r', encoding='utf-8') as f:
        return list(yaml.safe_load_all(f))

class Test_api():

    @pytest.mark.parametrize("datas",realYaml())
    @pytest.mark.webtest
    def test_graphStyle(self,datas):
        r=requests.get(url=datas['url'])
        logger.info("返回值为",json.dumps(r.json(), ensure_ascii=False))
        assert datas['except'] in json.dumps(r.json(), ensure_ascii=False)

    @pytest.mark.parametrize("datas", realYaml())
    def test_api(self,datas):
        if datas['method']=='get':
            r = requests.get(url=datas['url'])
        if datas['method']=='post':
            r=requests.post(url=datas['url'],json=datas["dict1"])
            logger.info(r.text)
        assert datas['except'] in json.dumps(r.json(), ensure_ascii=False)
