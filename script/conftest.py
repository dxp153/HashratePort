import pytest
import allure
from common.login_cooking import Token
from configparser import ConfigParser
from common.yaml_translation import yamlUtil
import os


@allure.step("登录8小时")
@pytest.fixture(scope="session")
def login_token():
    # token为两个参数，第一个为登录成功返回的响应数据，第二个为响应数据中的token参数
    config = ConfigParser()
    config.read(os.path.abspath("../pytest.ini"))
    url = config['pytest']['base_url']
    para = yamlUtil("../data/login.yaml").read_yaml()
    token = []
    for i in range(1, len(para)+1):
        data = para[i-1][0]['input']['data']
        headers = para[i-1][0]['input']['headers']
        i += 1
        token.append(Token().login_cooking(url, data, headers))
    yield token
