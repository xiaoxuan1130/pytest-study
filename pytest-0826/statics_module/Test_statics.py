#coding=utf-8
import pytest
import requests,json,os,yaml
from logger import logger


def get_data():
    path = os.path.dirname(os.path.abspath(__file__))
    with open('config.yaml', 'r', encoding='utf-8') as f:
        return list(yaml.safe_load_all(f))

def getEnv():
    path = os.path.dirname(os.path.abspath(__file__))
    with open('application.yaml', 'r', encoding='utf-8') as f:
        return yaml.safe_load(f).get("url")

url=getEnv()

class Test_statics():

    @pytest.mark.parametrize("datas", get_data())
    @pytest.mark.usefixtures("login")
    def test_interface(self, datas,login):
        jeeplusId=login
        cookies = {"jeeplus.session.id":jeeplusId}
        if datas['method'] == 'get':
            r = requests.get(url=url + datas['url'],cookies=cookies)
            logger.info(r.text)
        if datas['method'] == 'post':
            r = requests.post(url=url + datas['url'], json=datas["dict1"])
            logger.info(r.text)
        assert datas['except'] in json.dumps(r.json(), ensure_ascii=False)

    @pytest.mark.usefixtures("login")
    def test_update_info(self,login):
        jeeplusId = login
        cookies = {"jeeplus.session.id": jeeplusId}
        list=get_data()
        uploadUrl=''
        updateUrl=''
        for row in list:
            num=row['num']
            if num==2:
                uploadUrl =row['url']
            if num==3:
                updateUrl=row['url']
        headers = {'Conteny-Type': 'multipart/form-data'}
        files = {"file": ("grapy.png", open("D:\\software\\grapy.png", "rb"), "image/png", {})}
        r=requests.post(url+uploadUrl,files=files,headers=headers,cookies=cookies)
        fileUrl=r.json()["body"]['url']
        ##修改平面图
        # lavatoryGraphList=[]
        # row={
        #     'grapyUrl':fileUrl,
        #     'name':'深圳湾平面图',
        #     'delFlag':'0',
        #     'id':''
        # }
        # lavatoryGraphList.append(row)
        payload={
            "id":'18',
            "lavatoryGraphList[0].grapyUrl":fileUrl,
            "lavatoryGraphList[0].name": '深圳湾平面图',
            "lavatoryGraphList[0].delFlag": '0',
            "lavatoryGraphList[0].id": ''
        }
        r = requests.post(url + updateUrl, cookies=cookies,data=payload)
        json=r.json()
