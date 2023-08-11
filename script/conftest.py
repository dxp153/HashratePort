import pytest
import allure
from common.login_cooking import Token
from interface.switch_companies import SwitchCompanies


@allure.step("登录8小时")
@pytest.fixture(scope="session")
def login_cooking():
    data = {
        "username": "15797629873",
        "password": "dddd1234",
        "grant_type": "password",
        "captcha": "123"
    }
    headers = {
        "Content-Length": "71",
        "Host": "183.240.23.97",
        "Authorization": "Basic eXVuc2h1b2lvOnl1bnNodW9pbw==",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    # token为两个参数，第一个为登录成功返回的响应数据，第二个为响应数据中的token参数
    token = Token().login_cooking(data, headers)
    yield token
