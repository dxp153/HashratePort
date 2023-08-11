import pytest
import allure
from common.login_cooking import Token
from interface.switch_companies import SwitchCompanies
import yaml
from common.yaml_translation import yamlUtil


@allure.step("登录8小时")
@pytest.fixture(scope="session")
@pytest.mark.parametrize('para', yamlUtil("../data/login-prarmeter.yml").read_yaml())
def login_cooking(baes_url, para):
    # token为两个参数，第一个为登录成功返回的响应数据，第二个为响应数据中的token参数
    i = 0
    data = para[i]['input']['data']
    headers = para[i]['input']['headers']
    i += 1
    token = [Token().login_cooking(baes_url, data, headers)]
    yield token
