FROM python:3.6.8

WORKDIR /test1

ADD . /test1

RUN pip3 install -r requirements.txt  

CMD ["pytest", "-q","pytest-0820/test_api_02.py","--alluredir","allure-results"]