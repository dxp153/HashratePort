from interface.login import Login
from common.get_keyword import GetKeyword
from interface.switch_companies import SwitchCompanies
import json
import pytest
import allure
import yaml
from common.yaml_translation import yamlUtil


@allure.epic("登录接口测试")
class Test_Login:
    """
    接口登录用例
    """
    # with open('../data/login-prarmeter.yml', 'r', encoding='utf-8') as f:
    #     result = yaml.load_all(f.read(), Loader=yaml.FullLoader)

    @allure.story("用户登录")
    # @pytest.mark.parametrize('para', result)
    @pytest.mark.parametrize('para', yamlUtil("../data/login-prarmeter.yml").read_yaml())
    def test_login(self, base_url,  para):
        """
        用户登录
        :return:
        """
        i = 0
        with allure.step(para[i]['case']):
            data = para[i]['input']['data']
            headers = para[i]['input']['headers']
            code1 = para[i]['input']['code']
            msg1 = para[i]['input']['msg']
            i += 1
            response = Login(base_url=base_url).login(data, headers)
            t = response.text
            code = GetKeyword().json_path(json.loads(t), "$.code")
            msg = GetKeyword().json_path(json.loads(t), "$.msg")
            if msg:
                try:
                    assert (code[0] == code1)
                    assert (msg[0] == msg1)
                except AssertionError:
                    print("test_login_01 断言失败")
                    print("code == %s" % code)
                else:
                    print("测试通过 code==%s,%s" % (code, msg))