FROM python:3.6.8

RUN pip install --upgrade pip --index-url https://pypi.douban.com/simple

WORKDIR /test1

ADD . /test1

RUN pip install -r requirements.txt --index-url https://pypi.douban.com/simple


#CMD ["pytest", "-q","pytest-0820/test_allure_demo.py","--alluredir","allure-results"]

CMD ["pytest","-s","pytest-0820/test_allure_demo.py", "--html=report.html"]
