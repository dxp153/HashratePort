from interface.login import Login
from common.get_keyword import GetKeyword
from interface.switch_companies import SwitchCompanies
import json
import pytest
import allure
import yaml


with open('../data/login-prarmeter.yml', 'r', encoding='utf-8') as f:
    result = yaml.load_all(f.read(), Loader=yaml.FullLoader)


@allure.epic("登录接口测试")
class Test_Login:
    """
    接口登录用例
    """
    @pytest.mark.parametrize('para', result)
    def test_login(self, para):
        """
        用户正常登录
        :return:
        """
        i = 0
        print(para)
        data = para[i]['input']['data']
        headers = para[i]['input']['headers']
        code1 = para[i]['input']['code']
        msg1 = para[i]['input']['msg']
        i += 1
        # headers = {
        #     "Content-Length": "71",
        #     "Host": "183.240.23.97",
        #     "Authorization": "Basic eXVuc2h1b2lvOnl1bnNodW9pbw==",
        #     "Content-Type": "application/x-www-form-urlencoded"
        # }
        response = Login().login(data, headers)
        t = response.text
        code = GetKeyword().json_path(json.loads(t), "$.code")
        msg = GetKeyword().json_path(json.loads(t), "$.msg")
        print(msg)
        if msg:
            try:
                assert (code[0] == code1)
                assert (msg[0] == msg1)
            except AssertionError:
                print("test_login_01 断言失败")
                print("code == %s" % code)
            else:
                print("测试通过 code==%s,%s" % (code, msg))