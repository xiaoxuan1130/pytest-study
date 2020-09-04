FROM python:3.6.8

WORKDIR /test1

ADD . /test1

# 传递参数
ENTRYPOINT ["pytest"]

#CMD ["pytest", "-q","pytest-0820/test_api_02.py","--alluredir","allure-results"]